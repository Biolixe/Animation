Animation
=========

Python module to load anim scripts

<b>How to use it :</b>

First, import the module in your Python Script like this :

import Animation

or

from Animation import *

or

import Animation as newModuleName

Then, you'll need to create 2 files : "AnimKeywords.txt" and "AnimationFile.txt"

AnimKeywords.txt is a file where all keywords used for the game are defined

AnimationFile.txt is a file where all Images Locations and atributes are defined

<b>The module return a Surface List, you can make an animation in a loop like this :</b>


	Anim = Animation.Animation(Type,Object)

	character = Anim.loadAnim(keyword)

	screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

	x = 500

	y = 500

	while 1:

		screen.blit(character[inc], (x,y))
	
		inc += 1
