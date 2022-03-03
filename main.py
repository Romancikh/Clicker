from classes import *
from time import time

sound = False
work_bn = 0
state = 'mm'
click_power = 1
click_per_sec = 0
clicks = 0
balance = 0
price = 0
global_time = int(time())
mm_bg = image.load(background_folder + 'main_menu_bg.png')
gm_bg = image.load(background_folder + 'game_bg_active.png')
logo = transform.scale(image.load(enemy_folder + 'virus.png'), (450, 450))
playlist = mixer.Channel(0)
mm_bn = [
    Button(54, 50, 128, 128, 'start_idle', 'start_hover'),
    Button(236, 50, 128, 128, 'info_idle', 'info_hover'),
    Button(418, 50, 128, 128, 'exit_idle', 'exit_hover')
]
op_te = [
    Toggle(50, 400, 128, 128, 'toggle_inactive', 'toggle_selected'),
    Toggle(50, 550, 128, 128, 'toggle_inactive', 'toggle_selected'),
    Toggle(50, 700, 128, 128, 'toggle_inactive', 'toggle_selected')
]
op_bn = [
    Button(418, 50, 128, 128, 'exit_idle', 'exit_hover')
]
gm_bn = [
    Button(418, 50, 128, 128, 'exit_idle', 'exit_hover'),
    Button(75, 400, 450, 450)
]
gm_te = [
    Toggle(236, 50, 128, 128, 'expand', 'collapse')
]
sp_bn = [
    Button(108, 202, 384, 128, 'button_idle', 'button_hover', 'CLICK'),
    Button(108, 390, 384, 128, 'button_idle', 'button_hover', 'ANTI-VIRUS'),
    Button(108, 558, 384, 128, 'button_idle', 'button_hover', 'CASH'),
    Button(108, 726, 384, 128, 'button_idle', 'button_hover', 'WIN')
]
ck_bn = [
    Button(108, 202, 384, 128, 'button_idle', 'button_hover', '+1'),
    Button(108, 390, 384, 128, 'button_idle', 'button_hover', '+10'),
    Button(108, 558, 384, 128, 'button_idle', 'button_hover', '+100'),
]
as_bn = [
    Button(108, 202, 384, 128, 'button_idle', 'button_hover', '+1/sec'),
    Button(108, 390, 384, 128, 'button_idle', 'button_hover', '+10/sec'),
    Button(108, 558, 384, 128, 'button_idle', 'button_hover', '+100/sec'),
]
ch_bn = [
    Button(108, 202, 384, 128, 'button_idle', 'button_hover', '1☺'),
    Button(108, 390, 384, 128, 'button_idle', 'button_hover', '10☺'),
    Button(108, 558, 384, 128, 'button_idle', 'button_hover', '100☺'),
]
wn_bn = [
    Button(108, 202, 384, 128, 'button_idle', 'button_hover', 'win')
]
music_list = [f'data/music/mus{i + 1}.mp3' for i in range(8)]
now_music = False
money = False


def play_music():
    playlist.set_volume(int(sound) * 0.05)
    global now_music
    from random import choice
    if len(music_list) != 0:
        if not playlist.get_busy():
            now_music = choice(music_list)
            playlist.play(mixer.Sound(now_music))


def do_save():
    from os import listdir, mkdir
    if 'save' in listdir('data'):
        with open('data/save/save.txt', 'w') as file:
            text = str(click_power) + '\n'
            text += str(click_per_sec) + '\n'
            text += str(clicks) + '\n'
            text += str(balance) + '\n'
            text += str(work_bn) + '\n'
            text += str(int(sound)) + '\n'
            file.write(text)
    else:
        mkdir('data/save')
        do_save()


def load_save():
    global click_power, click_per_sec, clicks, balance, work_bn, sound
    from os import listdir
    if 'save' in listdir('data'):
        if 'save.txt' in listdir('data/save'):
            with open('data/save/save.txt') as file:
                text = file.readlines()
                for i in range(len(text)):
                    text[i] = text[i].rstrip('\n')
                click_power = int(text[0])
                click_per_sec = int(text[1])
                if text[2] == 'inf':
                    clicks = float(text[2])
                else:
                    clicks = int(text[2])
                balance = int(text[3])
                work_bn = int(text[4])
                sound = bool(int(text[5]))
        else:
            do_save()
    else:
        do_save()


def show_name():
    name_font = font.Font(font_folder + 'M 8pt.ttf', 100)
    name = name_font.render('VIRUS!!!', True, (0, 0, 0))
    screen.blit(name, (75, 200))


def show_options():
    text_font = font.Font(font_folder + 'M 8pt.ttf', 70)
    sound_text = text_font.render('SOUND', True, (0, 0, 0))
    cheat_text = text_font.render('CHEAT', True, (0, 0, 0))
    right_text = text_font.render('RIGHT', True, (0, 0, 0))
    screen.blit(sound_text, (200, 400))
    screen.blit(right_text, (200, 550))
    screen.blit(cheat_text, (200, 700))


def show_win():
    win_font = font.Font(font_folder + 'M 8pt.ttf', 100)
    win = win_font.render('WIN!!!', True, (150, 255, 150))
    size = win.get_size()
    screen.blit(win, (300 - size[0] // 2, 200))


def show_not_enough():
    global money
    n_e_font = font.Font(font_folder + 'M 8pt.ttf', 40)
    if money:
        n_e = n_e_font.render(f'YOU NEED {price - clicks}', True,
                              (255, 150, 150), (50, 50, 50))
    else:
        n_e = n_e_font.render(f'YOU NEED {price - balance}☺', True,
                              (255, 150, 150), (50, 50, 50))
    size = n_e.get_size()
    screen.blit(n_e, (300 - size[0] // 2, 200))


def show_balance():
    bal_font = font.Font(font_folder + 'M 8pt.ttf', 50)
    bal = bal_font.render(str(balance) + '☺', True, (255, 255, 150))
    screen.blit(bal, (80, 750))


def show_clicks():
    cl_font = font.Font(font_folder + 'M 8pt.ttf', 50)
    cl = cl_font.render(str(clicks), True, (150, 255, 150))
    screen.blit(cl, (40, 50))


def show_all():
    if state == 'mm':
        screen.blit(mm_bg, (0, 0))
        screen.blit(logo, (75, 400))
        show_name()
        for bn in mm_bn:
            bn.show()
    if state == 'options':
        screen.blit(mm_bg, (0, 0))
        show_name()
        show_options()
        for te in op_te:
            te.show()
        for bn in op_bn:
            bn.show()
    if state == 'game':
        screen.blit(gm_bg, (0, 0))
        screen.blit(logo, (75, 400))
        show_clicks()
        for bn in gm_bn:
            bn.show()
        for te in gm_te:
            te.show()
    if state == 'shop':
        screen.blit(gm_bg, (0, 0))
        screen.blit(image.load(gui_folder + 'shop.png'), (50, 180))
        for te in gm_te:
            te.show()
        for bn in sp_bn:
            bn.show()
    if state == 'click':
        screen.blit(gm_bg, (0, 0))
        screen.blit(image.load(gui_folder + 'shop.png'), (50, 180))
        show_balance()
        for te in gm_te:
            te.show()
        for bn in ck_bn:
            bn.show()
    if state == 'anti-virus':
        screen.blit(gm_bg, (0, 0))
        screen.blit(image.load(gui_folder + 'shop.png'), (50, 180))
        show_balance()
        for te in gm_te:
            te.show()
        for bn in as_bn:
            bn.show()
    if state == 'cash':
        screen.blit(gm_bg, (0, 0))
        screen.blit(image.load(gui_folder + 'shop.png'), (50, 180))
        show_balance()
        for te in gm_te:
            te.show()
        for bn in ch_bn:
            bn.show()
    if state == 'win':
        screen.blit(gm_bg, (0, 0))
        screen.blit(image.load(gui_folder + 'shop.png'), (50, 180))
        show_balance()
        for te in gm_te:
            te.show()
        for bn in wn_bn:
            bn.show()
    if state == 'winer':
        screen.blit(mm_bg, (0, 0))
        show_win()
    if state == 'not_enough':
        show_not_enough()


def do_time_click():
    global clicks, global_time
    if int(time()) - 1 == global_time:
        global_time = int(time())
        clicks += click_per_sec


def mouse_action():
    global state, work_bn, gm_bg, balance, click_power, click_per_sec, clicks, price, sound, money
    mp = mouse.get_pressed()
    now_time = 0
    if state == 'mm' and now_time != time():
        if point_inside(mm_bn[2]) and mp[work_bn]:
            do_save()
            quit()
            exit()
        if point_inside(mm_bn[1]) and mp[work_bn]:
            state = 'options'
        if point_inside(mm_bn[0]) and mp[work_bn]:
            state = 'game'
        now_time = time()
    if state == 'options':
        if point_inside(op_bn[0]) and mp[work_bn]:
            do_save()
            state = 'mm'
        if point_inside(op_te[0]) and mp[work_bn]:
            op_te[0].on = not op_te[0].on
            sound = op_te[0].on
        if point_inside(op_te[1]) and mp[work_bn]:
            if op_te[1].on:
                op_te[1].on = not op_te[1].on
                work_bn = 0
            else:
                op_te[1].on = not op_te[1].on
                work_bn = 2
        if point_inside(op_te[2]) and mp[work_bn]:
            op_te[2].on = not op_te[2].on
            clicks = float('inf')
        now_time = time()
    if state == 'game':
        if not gm_te[0].on:
            if point_inside(gm_bn[0]) and mp[work_bn]:
                state = 'mm'
                do_save()
        if point_inside(gm_te[0]) and mp[work_bn]:
            gm_te[0].on = not gm_te[0].on
            gm_bg = image.load(background_folder + 'game_bg_inactive.png')
            state = 'shop'
        if point_inside(gm_bn[1]) and mp[work_bn]:
            clicks += click_power
        now_time = time()
    if state == 'shop':
        if now_time != time():
            if point_inside(gm_te[0]) and mp[work_bn]:
                gm_te[0].on = not gm_te[0].on
                gm_bg = image.load(background_folder + 'game_bg_active.png')
                state = 'game'
        if point_inside(sp_bn[0]) and mp[work_bn]:
            state = 'click'
        if point_inside(sp_bn[1]) and mp[work_bn]:
            state = 'anti-virus'
        if point_inside(sp_bn[2]) and mp[work_bn]:
            state = 'cash'
        if point_inside(sp_bn[3]) and mp[work_bn]:
            state = 'win'
        now_time = time()
    if state == 'click':
        if point_inside(gm_te[0]) and mp[work_bn]:
            state = 'shop'
        if now_time != time():
            if point_inside(ck_bn[0]) and mp[work_bn]:
                if balance >= 10:
                    click_power += 1
                    balance -= 10
                else:
                    state = 'not_enough'
                    price = 10
            if point_inside(ck_bn[1]) and mp[work_bn]:
                if balance >= 100:
                    click_power += 10
                    balance -= 100
                else:
                    state = 'not_enough'
                    price = 100
            if point_inside(ck_bn[2]) and mp[work_bn]:
                if balance >= 1000:
                    click_power += 100
                    balance -= 1000
                else:
                    state = 'not_enough'
                    price = 1000
        now_time = time()
    if state == 'anti-virus':
        if point_inside(gm_te[0]) and mp[work_bn]:
            state = 'shop'
        if now_time != time():
            if point_inside(as_bn[0]) and mp[work_bn]:
                if balance >= 10:
                    click_per_sec += 1
                    balance -= 10
                else:
                    state = 'not_enough'
                    price = 10
            if point_inside(as_bn[1]) and mp[work_bn]:
                if balance >= 100:
                    click_per_sec += 10
                    balance -= 100
                else:
                    state = 'not_enough'
                    price = 100
            if point_inside(as_bn[2]) and mp[work_bn]:
                if balance >= 1000:
                    click_per_sec += 100
                    balance -= 1000
                else:
                    state = 'not_enough'
                    price = 1000
        now_time = time()
    if state == 'cash':
        if point_inside(gm_te[0]) and mp[work_bn]:
            state = 'shop'
        if now_time != time():
            if point_inside(as_bn[0]) and mp[work_bn]:
                if clicks >= 10:
                    balance += 1
                    clicks -= 10
                else:
                    price = 10
                    money = True
                    state = 'not_enough'
            if point_inside(as_bn[1]) and mp[work_bn]:
                if clicks >= 100:
                    balance += 10
                    clicks -= 100
                else:
                    price = 100
                    money = True
                    state = 'not_enough'
            if point_inside(as_bn[2]) and mp[work_bn]:
                if clicks >= 1000:
                    balance += 100
                    clicks -= 1000
                else:
                    money = True
                    price = 1000
                    state = 'not_enough'
        now_time = time()
    if state == 'win':
        if point_inside(gm_te[0]) and mp[work_bn]:
            state = 'shop'
        if now_time != time():
            if point_inside(as_bn[0]) and mp[work_bn]:
                if balance >= 10 ** 9:
                    state = 'winer'
                else:
                    state = 'not_enough'
                    price = 10 ** 9
        now_time = time()
    if state == 'not_enough':
        if now_time != time():
            if mp[work_bn]:
                state = 'shop'
                money = False


while True:
    for action in event.get():
        if action.type == QUIT:
            do_save()
            quit()
            exit()
        elif action.type == MOUSEBUTTONDOWN:
            mouse_action()
    if state == 'mm':
        load_save()
        if work_bn == 2:
            op_te[1].on = True
        op_te[0].on = sound

    play_music()
    do_time_click()
    show_all()
    display.update()
