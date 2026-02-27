#Imports
import tkinter as tk
import time
from tkinter import font
import random

WIDTH = 600
HEIGHT = 400

def make_player_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "0000000000011100000000000",
        "0000000000013100000000000",
        "0000000000113110000000000",
        "0000000000133310000000000",
        "0000000001133311000000000",
        "0000000001222221000000000",
        "0000000011112111100000000",
        "0000000000111110000000000",
        "0000000000011100000000000",
        "0004000000011100000004000",
        "0004000000011100000004000",
        "0004000000011100000004000",
        "0004000000013100000004000",
        "0044400000113110000044400",
        "0044400001133311000044400",
        "0014100011111111100014100",
        "0011100111240421110011100",
        "0011111112400042111111100",
        "0012111114012104111112100",
        "0012111110021200111112100",
        "0012400011012101100042100",
        "0012400041400041400042100",
        "0044400000110110000044400",
        "0444400000414140000044440",
        "4442400000004000000042444"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#efefef", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#4285f4", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
    
    return img

def make_capturted_player_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "0000000000011100000000000",
        "0000000000013100000000000",
        "0000000000113110000000000",
        "0000000000133310000000000",
        "0000000001133311000000000",
        "0000000001222221000000000",
        "0000000011112111100000000",
        "0000000000111110000000000",
        "0000000000011100000000000",
        "0004000000011100000004000",
        "0004000000011100000004000",
        "0004000000011100000004000",
        "0004000000013100000004000",
        "0044400000113110000044400",
        "0044400001133311000044400",
        "0014100011111111100014100",
        "0011100111240421110011100",
        "0011111112400042111111100",
        "0012111114012104111112100",
        "0012111110021200111112100",
        "0012400011012101100042100",
        "0012400041400041400042100",
        "0044400000110110000044400",
        "0444400000414140000044440",
        "4442400000004000000042444"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#434343", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#9900ff", (x,y))
            elif pattern[y][x] == "4":
                img.put("#666666", (x,y))
    
    return img

def make_basic_enemy_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "0222220000000000000222220",
        "0424240000000000000424240",
        "0444340000000000000434440",
        "0443440011111111100443440",
        "0434441111111111111444340",
        "0444444311111111134444440",
        "0444447431111111347444440",
        "1111111743111113471111111",
        "1331111177311137711111331",
        "0113111117731377111113110",
        "0011111111773771111111100",
        "0000011111144411111100000",
        "0000011111114111111100000",
        "0000011111441441111100000",
        "0000011144444444411100000",
        "0000011466666666641100000",
        "0000011667666666661100000",
        "0000031676666666661300000",
        "0000031676666666661300000",
        "0000043666666666663400000",
        "0000043663344433663400000",
        "0000014333444443334100000",
        "0000001444443444441000000",
        "0000000444443444440000000",
        "0000000044343434400000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#b7e1cd", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "5":
                img.put("#4285f4", (x,y))
            elif pattern[y][x] == "6":
                img.put("#1cfffa", (x,y))
            elif pattern[y][x] == "7":
                img.put("#c0feff", (x,y))
    
    return img

def make_shooting_enemy_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "0000000000000000000000000",
        "0022220000005000000222200",
        "0002222000058500002222000",
        "0000222207011107022220000",
        "0000021777711177771200000",
        "0000002177311137712000000",
        "0000002177311137712000000",
        "0000000217311137120000000",
        "0000000217311137120000000",
        "0000000217311137120000000",
        "0000000217311137120000000",
        "0000000011711171100000000",
        "0000000011711171100000000",
        "0000000011111111100000000",
        "0000000011111111100000000",
        "0000000014111114100000000",
        "0000000014311134100000000",
        "0000000014433344100000000",
        "0000000014666664100000000",
        "0000000014466644100000000",
        "0000000001444441000000000",
        "0000000000114110000000000",
        "0000000000011100000000000",
        "0000000000001000000000000",
        "0000000000001000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#b7e1cd", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ff9900", (x,y))
            elif pattern[y][x] == "6":
                img.put("#1cfffa", (x,y))
            elif pattern[y][x] == "7":
                img.put("#c0feff", (x,y))
    
    return img

def make_capturing_enemy_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "0200000000021200000000020",
        "0520000000218120000000250",
        "0552000000218120000002550",
        "0555550002189812000555550",
        "0555555555189815555555550",
        "0055550055555555500555500",
        "0000550500555550050550000",
        "0000055005055505005500000",
        "0000005550055500555000000",
        "0000000055505055500000000",
        "0000000005505055000000000",
        "0000000000505050000000000",
        "0000000000505050000000000",
        "0000000000505050000000000",
        "0000000005055505000000000",
        "0000000050005000500000000",
        "0000000055555555500000000",
        "0000000553333333550000000",
        "0000000534444444350000000",
        "0000000534777774350000000",
        "0000000000666660000000000",
        "0000000006000006000000000",
        "0000000006000006000000000",
        "0000000000000000000000000",
        "0000000000000000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "5":
                img.put("#4285f4", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#666666", (x,y))
            elif pattern[y][x] == "4":
                img.put("#b7b7b7", (x,y))
            elif pattern[y][x] == "1":
                img.put("#ff9900", (x,y))
            elif pattern[y][x] == "6":
                img.put("#1cfffa", (x,y))
            elif pattern[y][x] == "7":
                img.put("#c0feff", (x,y))
            elif pattern[y][x] == "8":
                img.put("#ffff00", (x,y))
            elif pattern[y][x] == "9":
                img.put("#fff2cc", (x,y))
    
    return img

def make_player_laser_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "010",
        "131",
        "141",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "141",
        "131",
        "010"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#ff0000", (x,y))
            elif pattern[y][x] == "2":
                img.put("#ea4335", (x,y))
            elif pattern[y][x] == "3":
                img.put("#ff5252", (x,y))
            elif pattern[y][x] == "4":
                img.put("#ffafaf", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ffffff", (x,y))
    
    return img

def make_enemy_laser_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "010",
        "131",
        "141",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "151",
        "141",
        "131",
        "010"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#00ff00", (x,y))
            elif pattern[y][x] == "2":
                img.put("#3fff26", (x,y))
            elif pattern[y][x] == "3":
                img.put("#6bff50", (x,y))
            elif pattern[y][x] == "4":
                img.put("#8fff80", (x,y))
            elif pattern[y][x] == "5":
                img.put("#ffffff", (x,y))
    
    return img

root = tk.Tk()
root.title("Galaga")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg = "#000000")
canvas.pack()

player_img = make_player_sprite()
capt_player_img = make_capturted_player_sprite()
basic_enemy_img = make_basic_enemy_sprite()
shoot_enemy_img = make_shooting_enemy_sprite()
capt_enemy_img = make_capturing_enemy_sprite()
player_laser_img = make_player_laser_sprite()
enemy_laser_img = make_enemy_laser_sprite()
#enemy_img = make_enemy_sprite()

player = canvas.create_image(WIDTH//2, HEIGHT-40, image = player_img, anchor="center")
capt_player = canvas.create_image(WIDTH//2, HEIGHT-80, image = capt_player_img, anchor = "center")
base_enemy = canvas.create_image(WIDTH//2, HEIGHT-120, image = basic_enemy_img, anchor = "center")
shoot_enemy = canvas.create_image(WIDTH//2, HEIGHT-160, image = shoot_enemy_img, anchor = "center")
capt_enemy = canvas.create_image(WIDTH//2, HEIGHT-200, image = capt_enemy_img, anchor = "center")
play_laser = canvas.create_image(WIDTH//2, HEIGHT - 240, image = player_laser_img, anchor = "center")
enemy_laser = canvas.create_image(WIDTH//2, HEIGHT-280, image = enemy_laser_img, anchor = "center")

root.mainloop()
