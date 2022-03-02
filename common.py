from pygame import *

init()
screen = display.set_mode((600, 900), vsync=True)

font_folder = 'data/fonts/'
background_folder = 'data/images/backgrounds/'
enemy_folder = 'data/images/enemies/'
gui_folder = 'data/images/gui/'
button_folder = gui_folder + 'buttons/'
toggle_folder = gui_folder + 'toggles/'


def point_inside(obj):
    mx, my = mouse.get_pos()
    return (obj.pos[0] < mx < obj.pos[0] + obj.size[0] and
            obj.pos[1] < my < obj.pos[1] + obj.size[1])
