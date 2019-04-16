## This is a practice game

Disgusting sprawl out of what this game is:

Idea -> Dungeon Game
Inspired by -> Advance wars / fire emblem.
Music Inspiration -> …

Desc:
	This game is like advance wars / fire emblem but there is a bigger emphasis on formations, unit movement, and lengthy world movement. (Massive maps but quick to finish sometimes [for good variety]) Use of spells, and world objects, etc… Central narrative?

Programming:
	Have a map that holds a bunch of classes. Each tile class has a visual id and a functional id. The visual ID corresponds to a space on a image lookup table to draw the image from. The functional ID corresponds to a list of functions that have special & sometimes very specific behaviours. A tile class can have more than one id (an array of ids.) In this case the ids are just used in the order they are positioned. (either ids.)
TODO: test if this is faster: (The code does this by making a stack, then going through each tile and pushing the stack with whatever the number(s) are [this is efficient because when using the + operator with an array, it doesn’t matter if the variable is integer or array[integer]; in the case of the latter the stack will just be filled with many items.] then places a -1 to symbolize “next tile”. After this the stack is unloaded onto the map.)
	There is a map class. The map has two 2d matrices, a top layer and a bottom layer. The top layer has references to the abstract class ‘unit’ which is redefined for each unit (good and bad.) There are function pointers that can be called to do actions for each unit like ‘attack()’ but are redefined in each different unit for different abilities.
There is a sequencing class which deals with dialogue bubbles and story event triggers. This class also talks with the script.lua file which has the information (functions, strings, etc) which show which missions are in which order and have the sequence of events of each mission & how other triggers work.
There is a menu class which controls the menu.
There is a sceneManager class which manages the different scenes and chooses which one should be active (updated & drawn) at a given time.
You can make your own levels by loading the scripts from .scpt files. There is a level editor which generates these. New units can also be defined using this file. -> ? -> maybe not.]
Add a third layer to the map and add fog of war?

Time to Complete the Above in lua (Love2D): ~24 hours straight
Time to Complete the Above in hard c++ (SDL2): … if I get / understand drawing code … ~48 hours straight?

Challenge Time?

Necessary Extras:
	Unit Ai. I dunno quite how to do this so it may be difficult.
( See: https://www.youtube.com/watch?v=1FBGR6vmNeU )
Maybe try having only basic behaviours like finite state machines, i.e: ‘walk towards closest (visible?) enemy’, or ‘target weakest enemy’, specific enemies like ‘target ranged units’, ‘choose one enemy and only attack it’, or ‘run away and use spells’.

Also:
Look into spritebatches, canvases, or things to draw faster / better.

More Mechanics:
    Have the each unit have a specific attack area, scaled based on unit strength, i.e:

    Weak Archer:
    ...x......
    .Axx......
    ...x......

    Strong Archer:
    ...xxx....
    .Axxxx....
    ...xxx....

    Rogue Archer:
    ....x.....
    .A.xxxxxxx
    ....x.....

    Feral Archer:
    .xxx......
    .xAx......
    .xxx......
