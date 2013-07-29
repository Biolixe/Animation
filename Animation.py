#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import pygame
except ImportError:
    print("Erreur 001 : Le module pyGame est introuvable")
try:
    from ctypes import *
except ImportError:
    print("Erreur 002 : Le module ctypes est introuvable")
try:
    import os
except ImportError:
    print("Erreur 003 : Le module os est introuvable")

    
class Animation:
    def __init__(self, typeObject, nameObject):
        self.fileCorrectlyOpen = []
        self.typeObject = typeObject
        self.nameObject = nameObject
        self.curdir = os.getcwd()
        if self.typeObject == "C": #Character
            self.animKeywordsDir = self.curdir + "/Data/Game/Characters/animKeywords.txt"
        if self.typeObject == "O": #Object
            self.animKeywordsDir = self.curdir + "/Data/Game/Objects/animKeywords.txt"
        if self.typeObject == "W": #Weapon
            self.animKeywordsDir = self.curdir + "/Data/Game/Weapons/animKeywords.txt"
        if self.typeObject == "M": #Magic
            self.animKeywordsDir = self.curdir + "/Data/Game/Magic/animKeywords.txt"
        if self.typeObject == "G": #GUI
            self.animKeywordsDir = self.curdir + "/Data/Game/GUI/animKeywords.txt"            
        try:
            self.animKeywords = open(self.animKeywordsDir,"r")
            self.animKeywords = self.animKeywords.readlines()
            self.inc = 0
            while self.inc != len(self.animKeywords):
                self.animKeywords[self.inc] = self.animKeywords[self.inc].replace("\n","")
                self.inc += 1
            self.fileCorrectlyOpen.append(True)
        except FileNotFoundError:
            print("Erreur 004 : Le fichier animKeywords est introuvable")
            self.fileCorrectlyOpen.append(False)
        if self.typeObject == "C":
            self.objectDir = self.curdir + "/Data/Game/Characters/" + self.nameObject + "/Sprites/"
        if self.typeObject == "O":
            self.objectDir = self.curdir + "/Data/Game/Objects/" + self.nameObject + "/Sprites/"
        if self.typeObject == "W":
            self.objectDir = self.curdir + "/Data/Game/Weapons/" + self.nameObject + "/Sprites/"
        if self.typeObject == "M":
            self.objectDir = self.curdir + "/Data/Game/Magic/" + self.nameObject + "/Sprites/"
        if self.typeObject == "G":
            self.objectDir = self.curdir + "/Data/Game/GUI/" + self.nameObject + "/Sprites/"
        self.animFileDir = self.objectDir + "AnimationFile.txt"
        if self.typeObject == "C":
            self.globalFileDir = self.curdir + "/Data/Game/Characters/GLOBAL/Sprites/AnimationFile.txt"
        if self.typeObject == "O":
            self.globalFileDir = self.curdir + "/Data/Game/Objects/GLOBAL/Sprites/AnimationFile.txt"
        if self.typeObject == "W":
            self.globalFileDir = self.curdir + "/Data/Game/Weapons/GLOBAL/Sprites/AnimationFile.txt"
        if self.typeObject == "M":
            self.globalFileDir = self.curdir + "/Data/Game/Magic/GLOBAL/Sprites/AnimationFile.txt"
        if self.typeObject == "G":
            self.globalFileDir = self.curdir + "/Data/Game/GUI/GLOBAL/Sprites/AnimationFile.txt"
        try:
            self.animFile = open(self.animFileDir,"r")
            self.globalAnimFile = open(self.globalFileDir,"r")
            self.fileCorrectlyOpen.append(True)
        except FileNotFoundError:
            print("Erreur 005 : Le fichier AnimationFile.txt est introuvable / Objet inexistant")
            self.fileCorrectlyOpen.append(False)
        if False in self.fileCorrectlyOpen:
            print("Erreur 006 : Impossible de construire les animations, fichier(s) manquant(s)")
        else:
            self.buildDatabase()
            
    def buildDatabase(self):
        self.animFileR = self.animFile.readlines()
        self.globalAnimFileR = self.globalAnimFile.readlines()
        self.animFile.close()
        self.animDB = {}
        self.globalAnimDB = {}
        self.inc = 0
        self.inc2 = 0
        self.inc3 = 0
        self.currentLine = "" #Ligne entière qui parcourt le ficher Animation
        self.currentAnim = "" #Ne contient que la référence de l'animation
        while self.inc != len(self.animFileR):
            self.currentLine = self.animFileR[self.inc].replace("\n","")
            
            if self.currentLine[0] == "&": #Clés officielles
                self.inc2 = 0
                self.inc3 = 0
                while self.currentLine[self.inc2] != "=":
                    self.inc2 += 1
                self.currentAnim = self.currentLine[0:self.inc2] #On récupère seulement la référence de l'animation
                while self.inc3 != len(self.animKeywords):
                    if self.animKeywords[self.inc3] == self.currentAnim and self.currentAnim not in self.animDB:
                        self.tempAnimDB = self.currentLine.replace("=","").replace("}","")
                        self.tempAnimDB = self.tempAnimDB[len(self.currentAnim)::]
                        self.animDB[self.currentAnim] = self.tempAnimDB
                    self.inc3 += 1

            if self.currentLine[0] == "@": #Clés custom
                self.inc2 = 0
                self.inc3 = 0
                while self.currentLine[self.inc2] != "=":
                    self.inc2 += 1
                self.currentAnim = self.currentLine[0:self.inc2] #On récupère seulement la référence de l'animation
                while self.inc3 != len(self.animKeywords):
                    if self.currentAnim not in self.animDB:
                        self.tempAnimDB = self.currentLine.replace("=","").replace("}","")
                        self.tempAnimDB = self.tempAnimDB[len(self.currentAnim)::]
                        self.animDB[self.currentAnim] = self.tempAnimDB
                    self.inc3 += 1
            self.inc += 1

        self.inc = 0
        self.inc2 = 0
        self.inc3 = 0
        
        while self.inc != len(self.globalAnimFileR):
            self.globalCurrentLine = self.globalAnimFileR[self.inc].replace("\n","")
            if self.globalCurrentLine[0] == "&": #Clés officielles
                self.inc2 = 0
                self.inc3 = 0
                while self.globalCurrentLine[self.inc2] != "=":
                    self.inc2 += 1
                self.globalCurrentAnim = self.globalCurrentLine[0:self.inc2]
                while self.inc3 != len(self.animKeywords):
                    if self.animKeywords[self.inc3] == self.globalCurrentAnim and self.globalCurrentAnim not in self.globalAnimDB:
                        self.globalAnimDB[self.globalCurrentAnim] = self.globalCurrentLine.replace(self.globalCurrentAnim,"").replace("=","").replace("}","")
                    self.inc3 += 1
            self.inc += 1

    def loadAnim(self, keyword):
        self.picList = []
        self.animList = []
        self.reversed = False
        self.animContinue = False
        self.globalBool = False
        try:
            self.doAnim = self.animDB[keyword]
            if "-global" in self.doAnim:
                self.keywordGlobal = self.doAnim.replace(" -global","")
                self.numberGlobal = self.keywordGlobal[-1::]
                self.keywordGlobal = self.keywordGlobal.replace(" -","")
                self.keywordGlobal = self.keywordGlobal.replace(self.numberGlobal,"")
                self.doAnim = self.globalAnimDB[self.keywordGlobal].replace("$",self.numberGlobal)
                self.globalBool = True
            if "-reversed" in self.doAnim:
                self.keywordReversed = self.doAnim.replace(" -reversed","")
                if self.keywordReversed == "":
                    print("Erreur 009 : Impossible de générer un -reversed sur l'objet")
                else:
                    if self.globalBool == False:
                        self.doAnim = self.animDB[self.keywordReversed]
                    else:
                        self.doAnim = self.globalAnimDB[self.keywordReversed].replace("$",self.numberGlobal)
                    self.reversed = True
            self.inc = 0
            while self.inc != len(self.doAnim):
                if self.doAnim[self.inc] == "(":
                    self.startFolder = self.inc
                if self.doAnim[self.inc] == ")":
                    self.endFolder = self.inc
                if self.doAnim[self.inc] == "[":
                    self.startPics = self.inc
                if self.doAnim[self.inc] == "]":
                    self.endPics = self.inc
                self.inc += 1
            self.animFolder = self.doAnim[self.startFolder+1:self.endFolder]
            self.animPics = self.doAnim[self.startPics+1:self.endPics]
            self.animContinue = True #Si tout s'est bien passé
            
        except KeyError:
            print("Erreur 007 : Clé d'animation introuvable / imcompatible avec l'objet")
            
        if self.animContinue == True: #On charge toutes les images du mot-clé
            self.animFolder = self.curdir + self.animFolder
            self.inc = 0
            self.precPic = 0 #Position curseur de l'image précédente
            while self.inc != len(self.animPics):
                if self.animPics[self.inc] == ",":
                    self.picList.append(self.animPics[self.precPic:self.inc])
                    self.precPic = self.inc + 1 #On modifie la position du curseur de la ligne
                if self.inc == len(self.animPics) - 1: #Récupérer la dernière image
                    self.picList.append(self.animPics[self.precPic:self.inc+1])
                self.inc += 1
            self.inc = 0
            while self.inc != len(self.picList):
                self.currentLoad = 'pygame.image.load(self.animFolder + "/" + self.picList[self.inc])'
                if self.reversed == True:
                    self.currentLoad = " pygame.transform.flip(" + self.currentLoad + ",True,False)"
                self.animList.append(eval(self.currentLoad))
                self.inc += 1
            self.inc = 0
            return self.animList
        else:
            print("Erreur 008 : Impossible de continuer, clé d'animation nécéssaire")

    def test(self, fpsmax=30): #Permet de tester l'animation chargée (FONCTION DEVELOPPEUR)
        
        self.black = 0, 0, 0 #Définit la couleur noire
        self.white = 255, 255, 255 #Définit la couleur blanche
        self.blue = 0, 0, 255 #Définit la couleur bleue
        self.red = 255, 0, 0 #Définit la couleur rouge
        self.yellow = 255, 255, 0 #Définit la couleur jaune
        self.colorNB = 0
        self.clock = pygame.time.Clock()
        pygame.init()
        self.width = windll.user32.GetSystemMetrics (0)
        self.height = windll.user32.GetSystemMetrics (1)
        screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.background = pygame.image.load("BG.png")
        self.inc = 0
        self.switch = False
        self.x = self.width/2
        self.y = self.height/2
        pygame.key.set_repeat(1000,1)
        while 1:
            self.event = pygame.event.poll()
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if self.event.key == pygame.K_SPACE:
                    self.colorNB += 1
                    if self.colorNB == 5:
                        self.colorNB = 0
            if self.colorNB == 0:
                self.colorBG = self.black
            if self.colorNB == 1:
                self.colorBG = self.white
            if self.colorNB == 2:
                self.colorBG = self.blue
            if self.colorNB == 3:
                self.colorBG = self.red
            if self.colorNB == 4:
                self.colorBG = self.yellow
            screen.fill(self.colorBG)
            screen.blit(self.animList[self.inc], (self.x,self.y))
            self.inc += 1
            if self.inc == len(self.animList):
                self.inc = 0
            pygame.display.flip()
            self.clock.tick(fpsmax)

