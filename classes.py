from common import *


class Button:
    def __init__(self, x, y, w, h, idle=None, hover=None, text=None):
        self.pos = [x, y]
        self.size = [w, h]
        self.idle = idle
        if self.idle:
            self.idle = transform.scale(
                image.load(button_folder + self.idle + ".png"), self.size)
        self.hover = hover
        if self.hover:
            self.hover = transform.scale(
                image.load(button_folder + self.hover + ".png"), self.size)
        self.text = text
        if self.text:
            f = font.Font(font_folder + 'M 8pt.ttf', int(h * 0.3))
            size = f.size(self.text)
            self.text = f.render(self.text, True, (0, 0, 0))
            self.text_pos = [x + (w - size[0]) // 2, y + (h - size[1]) // 2]

    def show(self):
        if point_inside(self):
            if self.hover:
                screen.blit(self.hover, self.pos)
        else:
            if self.idle:
                screen.blit(self.idle, self.pos)
        if self.text:
            screen.blit(self.text, self.text_pos)


class Toggle:
    def __init__(self, x, y, w, h, inactive, selected, on=False):
        self.pos = [x, y]
        self.size = [w, h]
        self.on = on
        self.inactive = inactive
        if self.inactive:
            self.inactive = transform.scale(
                image.load(toggle_folder + self.inactive + '.png'), self.size)
        self.selected = selected
        if self.selected:
            self.selected = transform.scale(
                image.load(toggle_folder + self.selected + '.png'), self.size)

    def show(self):
        if self.on:
            if self.selected:
                screen.blit(self.selected, self.pos)
        else:
            if self.inactive:
                screen.blit(self.inactive, self.pos)
