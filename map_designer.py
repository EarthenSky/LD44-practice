# This template is built to make the user no longer need to work with the
# "while loop" that runs pygame when building something simple.
# This template is also made to include a frame independent movement constant,
# as well as some other useful prebuilt code.

import pygame
import math

#--INSTRUCTIONS--#
#
# Writing "~COLOUR~" infront of the tile will change the colour of the tile.
#

SCREEN_SIZE = [1024, 768]
FPS = 60

# Colours -- Arne Palette v20
COLOUR_BLACK = (0, 0, 0)
COLOUR_WHITE = (255, 255, 255)
COLOUR_GRAY = (157, 157, 157)
COLOUR_SEB = (0, 87, 132)
COLOUR_SKB = (49, 162, 242)
COLOUR_CB = (178, 220, 239)
COLOUR_O = (235, 137, 49)
COLOUR_Y = (247, 226, 107)
COLOUR_R = (190, 38, 51)
COLOUR_G = (68, 137, 26)
COLOUR_LG = (163, 206, 39)

# Starts and sets up pygame
pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Simple TileMap Creator")

FONT = pygame.font.SysFont('consolas', 24)

# Runtime constant used to modify movement. (More like readonly.)
delta_time = 0
g_is_edit_mode = False
g_update_menu_text = False

# TODO: press control to copy the colour from a tile.
# TODO: fix bug when size down.
# TODO: make out and input tile maps.

# Map globals
g_map_size_x = 4
g_map_size_y = 4
g_tile_size = 16
g_map_pos_x = 16
g_map_pos_y = 16
g_text_surface = FONT.render("size:{}, x:{}, y:{}".format(16, 4, 4), True, COLOUR_WHITE)

g_menu_mode = "move"
g_insert_string = "1"  # This string holds the info that gets drawn to the tiles.

g_item_list = [["0" for x in range(0, g_map_size_x)] for y in range(0, g_map_size_y)] # -> [y][x]

# This function chanmge the size of the array to
def update_item_list():
    global g_item_list

    # for the horizontal axis
    if len(g_item_list[0]) < g_map_size_x:
        positions = -len(g_item_list[0])+g_map_size_x
        for item in g_item_list:
            item += ["0"]*positions
    elif len(g_item_list[0]) > g_map_size_x: # remove n item(s) from each row. (deleting columns)
        positions = len(g_item_list[0])-g_map_size_x
        for item in g_item_list:
            for i in range(0, positions):
                del item[len(item)-1]

    # for the vertical axis
    if len(g_item_list) < g_map_size_y:  # Add rows until g_item_list & len(g_item_list) are equal
        for i in range(0, g_map_size_y-len(g_item_list)):
            g_item_list.append(["0" for y in range(0, g_map_size_x)])
    elif len(g_item_list) > g_map_size_y:
        for i in range(0, -g_map_size_y+len(g_item_list)):
            del g_item_list[len(g_item_list)-1]

update_item_list()

# This is the flag that controls ending the game.
game_stopped = False

# This function will write the map data to a file.
def write_to_file():
    pass

# This function will load the map data from a file.
def load_from_file():
    pass

def update_text(str):
    global g_text_surface
    g_text_surface = FONT.render(str, True, COLOUR_WHITE)

# This function handles any input.  Called before update.
g_key_up_pressed = False
g_key_down_pressed = False
g_key_left_pressed = False
g_key_right_pressed = False
g_mb_down = False
g_mouse_x = -1
g_mouse_y = -1
def handle_input():
    global game_stopped, g_map_size_x, g_map_size_y, g_tile_size, g_update_menu_text, \
            g_map_pos_x, g_map_pos_y, g_key_up_pressed, g_key_down_pressed, g_key_left_pressed, g_key_right_pressed, \
            g_menu_mode, g_insert_string, g_mb_down, g_item_list, g_mouse_x, g_mouse_y

    # This function draws the insert text the tile under the mouse.
    def draw_insert():
        # Map realtive positions
        grid_xpos = g_mouse_x - g_map_pos_x
        grid_ypos = g_mouse_y - g_map_pos_y

        # Map indexes
        ix = max(0, min(g_map_size_x-1, math.floor(grid_xpos / (g_tile_size+1))))  # max&min -> clamp
        iy = max(0, min(g_map_size_y-1, math.floor(grid_ypos / (g_tile_size+1))))

        g_item_list[iy][ix] = g_insert_string

    # This function gets the sting value at a certain tile.
    def get_tile_value():
        # Map realtive positions
        grid_xpos = g_mouse_x - g_map_pos_x
        grid_ypos = g_mouse_y - g_map_pos_y

        # Map indexes
        ix = max(0, min(g_map_size_x-1, math.floor(grid_xpos / (g_tile_size+1))))  # max&min -> clamp
        iy = max(0, min(g_map_size_y-1, math.floor(grid_ypos / (g_tile_size+1))))

        return g_item_list[iy][ix]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stopped = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # exit all modes
                g_update_menu_text = True
                g_menu_mode = "move"
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL: # Copy colour
                g_insert_string = get_tile_value()
            elif g_menu_mode == "insert":
                if event.key == pygame.K_BACKSPACE:
                    if len(g_insert_string) >= 1:
                        g_insert_string = g_insert_string[0:-1]
                else:
                    g_insert_string += event.unicode # TODO: test that this works ok?
            #elif event.key == pygame.K_l: # Change through layers
            elif event.key == pygame.K_e: # Menu control
                g_update_menu_text = True
                if g_menu_mode == "edit":
                    g_menu_mode = "move"
                else:
                    g_menu_mode = "edit"
            elif event.key == pygame.K_i: # Menu control
                g_update_menu_text = True
                if g_menu_mode == "insert":
                    g_menu_mode = "move"
                else:
                    g_menu_mode = "insert"
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                g_tile_size *= 1.5
                update_text("size:{}, x:{}, y:{}".format(g_tile_size, g_map_size_x, g_map_size_y))
            elif event.key == pygame.K_MINUS:
                g_tile_size /= 1.5
                update_text("size:{}, x:{}, y:{}".format(g_tile_size, g_map_size_x, g_map_size_y))
            elif g_menu_mode == "edit":
                if event.key == pygame.K_DOWN:
                    g_map_size_y+=1;
                    update_text("size:{}, x:{}, y:{}".format(g_tile_size, g_map_size_x, g_map_size_y))
                    update_item_list()
                elif event.key == pygame.K_UP:
                    g_map_size_y-=1;
                    if g_map_size_y < 0:
                        g_map_size_y = 0;
                    update_text("size:{}, x:{}, y:{}".format(g_tile_size, g_map_size_x, g_map_size_y))
                    update_item_list()
                elif event.key == pygame.K_LEFT:
                    g_map_size_x-=1;
                    if g_map_size_x < 0:
                        g_map_size_x = 0;
                    update_text("size:{}, x:{}, y:{}".format(g_tile_size, g_map_size_x, g_map_size_y))
                    update_item_list()
                elif event.key == pygame.K_RIGHT:
                    g_map_size_x+=1;
                    update_text("size:{}, x:{}, y:{}".format(g_tile_size, g_map_size_x, g_map_size_y))
                    update_item_list()
            else:
                if event.key == pygame.K_UP:
                    g_key_up_pressed = True
                elif event.key == pygame.K_DOWN:
                    g_key_down_pressed = True
                elif event.key == pygame.K_LEFT:
                    g_key_left_pressed = True
                elif event.key == pygame.K_RIGHT:
                    g_key_right_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                g_key_up_pressed = False
            elif event.key == pygame.K_DOWN:
                g_key_down_pressed = False
            elif event.key == pygame.K_LEFT:
                g_key_left_pressed = False
            elif event.key == pygame.K_RIGHT:
                g_key_right_pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            g_mb_down = True
            draw_insert()
        elif event.type == pygame.MOUSEBUTTONUP:
            g_mb_down = False
        elif event.type == pygame.MOUSEMOTION:
            g_mouse_x = event.pos[0]
            g_mouse_y = event.pos[1]
            if g_mb_down == True: # Check if mouse is inside a box while button is down
                draw_insert()

    # Handle map movement booleans
    if not g_is_edit_mode:
        if g_key_up_pressed:
            g_map_pos_y += g_tile_size*delta_time*10
        elif g_key_down_pressed:
            g_map_pos_y -= g_tile_size*delta_time*10
        elif g_key_left_pressed:
            g_map_pos_x += g_tile_size*delta_time*10
        elif g_key_right_pressed:
            g_map_pos_x -= g_tile_size*delta_time*10

# this function cts the colour code from a string and returns the regular version
# of the string & colour as a tuple: (string, colour)
def cut_colour_code(string):
    if string.find('~') == -1:
        return (string, COLOUR_SEB)  # return default colour
    else:
        state = "main"
        save_string = ""
        for ch in string:
            if state == "save" and ch == '~':
                colour = COLOUR_BLACK
                ss = save_string.lower()
                if ss == "white": colour = COLOUR_WHITE
                elif ss == "grey" or ss == "gray": colour = COLOUR_GRAY
                elif ss == "red": colour = COLOUR_R
                elif ss == "blue": colour = COLOUR_SEB
                elif ss == "yellow": colour = COLOUR_Y
                elif ss == "orange": colour = COLOUR_O
                elif ss == "green": colour = COLOUR_G
                elif ss == "lg": colour = COLOUR_LG
                elif ss == "cb": colour = COLOUR_CB
                return (string.replace('~{}~'.format(save_string),''), colour)
            elif state == "main" and ch == '~':
                state = "save"
            elif state == "save":
                save_string += ch

def draw_tiles():
    font_tmp = pygame.font.SysFont('consolas', int(g_tile_size/2))
    for y in range(g_map_size_y):
        for x in range(g_map_size_x):
            xpos = g_map_pos_x + (g_tile_size+1)*x
            ypos = g_map_pos_y + (g_tile_size+1)*y

            txt, tcol = cut_colour_code(g_item_list[y][x]) # this

            # Draw tile
            pygame.draw.rect(DISPLAY_SURFACE, tcol, (xpos, ypos, g_tile_size, g_tile_size))

            # Draw text
            ts = font_tmp.render( txt, True, COLOUR_SKB )
            DISPLAY_SURFACE.blit( ts, (xpos, ypos) )

# This function draws the menu bar and all its info
MENU_BAR_HEIGHT = 64
g_ts = FONT.render("Mode: move", True, COLOUR_CB)
def draw_menu_bar():
    global g_update_menu_text, g_ts

    bar_col = COLOUR_SEB
    txt_col = COLOUR_CB
    txt = "Mode: {}".format(g_menu_mode)

    if g_menu_mode == "edit":
        bar_col = COLOUR_O
        txt_col = COLOUR_Y
    elif g_menu_mode == "insert":
        bar_col = COLOUR_R
        txt_col = COLOUR_O

    # Draw under part of bar.
    rect = (0, SCREEN_SIZE[1]-MENU_BAR_HEIGHT, SCREEN_SIZE[0], MENU_BAR_HEIGHT)
    pygame.draw.rect(DISPLAY_SURFACE, bar_col, rect)

    # Check if text needs to be re-rendered
    if g_update_menu_text:
        g_ts = FONT.render(txt, True, txt_col)
        g_update_menu_text = False

    # Draw text
    DISPLAY_SURFACE.blit( g_ts, (4, SCREEN_SIZE[1]-MENU_BAR_HEIGHT+4) )

    # Draw insert text
    its = FONT.render("insert_string: " + g_insert_string, True, txt_col)
    DISPLAY_SURFACE.blit( its, (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-MENU_BAR_HEIGHT+4) )

# This is for drawing stuff.  Called before update
def draw():
    DISPLAY_SURFACE.fill( COLOUR_BLACK )

    draw_tiles()
    draw_menu_bar()

    DISPLAY_SURFACE.blit( g_text_surface, (0,0) )

# This is the "do game math" function.  Put any math or functional code here.
def update():
    pass

# This is the gameloop section of code.
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

print("DEBUG: Application Complete.")
