## Game tools

### Why use them?
- ease of development
- faster feature implementation
- more focus on the creative part and less on the coding

do you prefer this?
[picturehere]()

Or this?
[picturehere]()


### Game engine examples

- Interactive text based games [inkle](https://www.inklestudios.com/ink/web-tutorial/)
    - [80 days](https://www.youtube.com/watch?v=yU5hF6pHd0Q)
    - [Overboard](https://www.youtube.com/watch?time_continue=25&v=KKAh1Nm7iUE&feature=emb_logo)

- 2d Engine for lua [Love](https://love2d.org/wiki/Main_Page)
    - [SimpleVideoTutorial](https://www.youtube.com/watch?v=u6GWjojPQiM) 
    [Also cool trick to manipulate dictiorany while iterating through it at 50min. Trick is to iterate backwords]: #

- RogueLike engine python [Tcod](https://python-tcod.readthedocs.io/en/latest/installation.html)
    - [Tutorial](https://rogueliketutorials.com/tutorials/tcod/v2/)
    - [VideoTutorial](https://www.youtube.com/watch?v=r47iWInWJp4)

- 2d Engine for python [Pygame](https://web.archive.org/web/20220223214213/https://www.pygame.org/docs/)
    - [BegginerTutorial](https://pythonprogramming.net/pygame-python-3-part-1-intro/)
    - [PlatformerTutorial](https://www.youtube.com/watch?v=YWN8GcmJ-jA)
    [vscode pygame problems :https://stackoverflow.com/questions/50569453/why-does-it-say-that-module-pygame-has-no-init-member
]: # 
- 3d Engine for python [Panda3D](https://docs.panda3d.org/1.10/python/index)
    - [Tutorial](https://arsthaumaturgis.github.io/Panda3DTutorial.io/)
    - [PlatformerTutorial](https://www.youtube.com/watch?v=QtzuxPUJ_Qc)

- Combination https://www.youtube.com/watch?v=vY0Sk93YUhA

### General tips:
Using a file format for loading levels , like CSV (Comma Separated Values). This will help with level creation, since we dont have to recompile every time

BREAK UP YOUR CODE. It helps with problem solving and when working with a big game it becomes vital

When iterating and we want to manipulate a list we end up with an error. A classic solution is to use a flag for every item we want to delete later, at another pass (this is effiecient cause we deallocate a lot of memory together). Another solution is to count backwards to resolve the error.

For collision detection there are many tricks to use to understand how it occured.
One is to use flags and logic, and the decide how to react
Another is to break up the axis and the movement

### Making the platformer

1. setup for the level
    - make settings
    - make level map
    - make the Tiles

2. setup the level
    - make the level surface
    - load the level from the file
    - draw the level

### How do we make them?
Not the scope of this meeting