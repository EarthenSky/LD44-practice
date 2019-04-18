# This template is built to make the user no longer need to work with the
# "while loop" that runs pygame when building something simple.
# This template is also made to include a frame independent movement constant,
# as well as some other useful prebuilt code.

import pygame

# This is a 2d vector that holds the size of the screen.
SCREEN_SIZE = [1024, 768]

# Sets the prefered fps.  Mostly affects the speed of the main gameloop,
# although complex calculations may cause the fps to drop.
# Use delta_time to link movement to frame change speed.
FPS = 50

# Starts and sets up pygame
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Name?!")

FONT = pygame.font.SysFont('consolas', 30)

# Runtime constant used to modify movement. (More like readonly.)
delta_time = 0

g_map_size_x = 4
g_map_size_y = 4
g_text_surface = FONT.render("", False, (1, 1, 1))
g_tile_size = 16

g_item_list = []


# This is the flag that controls ending the game.
game_stopped = False

# This function will write the map data to a file.
def write_to_file():
    pass

def update_item_list():
    global g_item_list
    g_item_list = [[0 for x in range(0, g_map_size_x)] for y in range(0, g_map_size_y)]

# This function handles any input.  Called before update.
def handle_input():
    global game_stopped, g_map_size_x, g_map_size_y, g_text_surface
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                g_map_size_y+=1;
                text = "size || x:{}, y:{}".format(g_map_size_x, g_map_size_y)
                g_text_surface = FONT.render(g_debug_text, False, (255, 255, 255))
            elif event.key == pygame.K_DOWN:
                g_map_size_y-=1;
                if g_map_size_y < 0:
                    g_map_size_y = 0;
                text = "size || x:{}, y:{}".format(g_map_size_x, g_map_size_y)
                g_text_surface = FONT.render(g_debug_text, False, (255, 255, 255))
            elif event.key == pygame.K_LEFT:
                g_map_size_x-=1;
                if g_map_size_x < 0:
                    g_map_size_x = 0;
                text = "size || x:{}, y:{}".format(g_map_size_x, g_map_size_y)
                g_text_surface = FONT.render(g_debug_text, False, (255, 255, 255))
            elif event.key == pygame.K_RIGHT:
                g_map_size_x+=1;
                text = "size || x:{}, y:{}".format(g_map_size_x, g_map_size_y)
                g_text_surface = FONT.render(g_debug_text, False, (255, 255, 255))
            elif event.key == pygame.K_plus:
                pass # size of cubes
            elif event.key == pygame.K_minus:
                pass # size of cubes

# This is for drawing stuff.  Called before update
def draw():
    #global g_text_surface
    DISPLAY_SURFACE.fill((0,0,0))
    DISPLAY_SURFACE.blit( g_text_surface, (0,0) )
    for row in g_item_list:
        for id in row:
            DISPLAY_SURFACE.draw() # draw the cube here.

    #pygame.drawstring( )

# This is the "do game math" function.  Put any math or functional code here.
# Called after handle_input.  This function is updated FPS times per second.
# Remember to define any outside defined, non-constant varaibles as "global"
def update():
    #ex.
    #global my_var_non_const
    #my_var_non_const += 1
    #print str(my_var_non_const)
    pass

# This is the gameloop section of code.
# This template is designed so that you don't need to interact with
# this function / section of the code.
def gameloop():
    global delta_time

    # Create the object that handles framerate regulation and delta_time.
    framerate_clock = pygame.time.Clock()
    delta_time = framerate_clock.tick(FPS) / 1000.0

    # This is the start of the gameloop.
    while not game_stopped:
        handle_input()  # First Gameloop Stage.

        update()  # Second Gameloop Stage.

        draw() # Last Gameloop Stage.

        pygame.display.update() # Updates the display with changes.

        # Pause pygame and calculate delta time.
        delta_time = framerate_clock.tick(FPS) / 1000.0
        #print "DEBUG: delta_time = " + str(delta_time) + ", fps -> " + str( framerate_clock.get_fps() )

    # Close pygame before application closes.
    pygame.quit()

gameloop()  # This is pretty much the only instruction run in the global scope.

print "DEBUG: Application Complete."
