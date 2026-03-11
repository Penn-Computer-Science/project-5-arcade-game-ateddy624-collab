#Imports
import tkinter as tk
import time
from tkinter import font
import random

WIDTH = 600
HEIGHT = 400
ROWS = 4
COLS = 8
CELL = 32
enemy_move_speed = 4
restart_text = "RESTART"
flashID = None
ax1 = 0
ax2 = 0
ay1 = 0
ay2 = 0

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

def make_player_sprite_2():
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

def make_player_sprite_3():
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

def make_capturing_enemy_sprite_1():
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
        "0000000538444448350000000",
        "0000000534177714350000000",
        "0000000000222220000000000",
        "0000000002000002000000000",
        "0000000002000002000000000",
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

def make_capturing_enemy_sprite_2():
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
        "0000000538444448350000000",
        "0000000534177714350000000",
        "0000000000222220000000000",
        "0000000002000002000000000",
        "0000000002000002000000000",
        "0000000600000000060000000",
        "0000000766000006670000000",
        "0000000077666667700000000",
        "0000000000777770000000000"
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

def make_capturing_enemy_sprite_3():
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
        "0000000538444448350000000",
        "0000000534177714350000000",
        "0000000000222220000000000",
        "0000000002000002000000000",
        "0000000002000002000000000",
        "0000000600000000060000000",
        "0000000766000006670000000",
        "0000060077666667700600000",
        "0000076000777770006700000",
        "0000006000000000006000000",
        "0000007600000000067000000",
        "0000000766000006670000000",
        "0000000077666667700000000",
        "0000000000777770000000000"
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

def make_capturing_enemy_sprite_4():
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
        "0000000538444448350000000",
        "0000000534177714350000000",
        "0000000000222220000000000",
        "0000000002000002000000000",
        "0000000002000002000000000",
        "0000000600000000060000000",
        "0000000766000006670000000",
        "0000060077666667700600000",
        "0000076000777770006700000",
        "0000006000000000006000000",
        "0000007600000000067000000",
        "0006000766000006670006000",
        "0007600077666667700067000",
        "0000600000777770000060000",
        "0000760000000000000670000",
        "0000076000000000006700000",
        "0000006000000000006000000",
        "0000007660000000667000000",
        "0000000776666666770000000",
        "0000000007777777000000000",
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

def make_hit_capturing_enemy_sprite():
    global WIDTH, HEIGHT

    pattern = [
        "0200000000021200000000020",
        "0520000000218120000000250",
        "0552000000218120000002550",
        "0555550002189812000555550",
        "0655555555189815555555560",
        "0065550055555555500555600",
        "0000650600555550060560000",
        "0000065006059506005600000",
        "0000006550059500556000000",
        "0000000065529255600000000",
        "0000000006529256000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000005059505000000000",
        "0000000050009000500000000",
        "0000000055555555500000000",
        "0000000556666666550000000",
        "0000000567777777650000000",
        "0000000567444447650000000",
        "0000000000333330000000000",
        "0000000003000003000000000",
        "0000000003000003000000000",
        "0000000000000000000000000",
        "0000000000000000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "5":
                img.put("#351c75", (x,y))
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

def make_hit_capturing_enemy_sprite_1():
    global WIDTH, HEIGHT

    pattern = [
        "0200000000021200000000020",
        "0520000000218120000000250",
        "0552000000218120000002550",
        "0555550002189812000555550",
        "0655555555189815555555560",
        "0065550055555555500555600",
        "0000650600555550060560000",
        "0000065006059506005600000",
        "0000006550059500556000000",
        "0000000065529255600000000",
        "0000000006529256000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000005059505000000000",
        "0000000050009000500000000",
        "0000000055555555500000000",
        "0000000552222222550000000",
        "0000000521111111250000000",
        "0000000521888881250000000",
        "0000000000999990000000000",
        "0000000005000005000000000",
        "0000000005000005000000000",
        "0000000000000000000000000",
        "0000000000000000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "5":
                img.put("#351c75", (x,y))
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

def make_hit_capturing_enemy_sprite_2():
    global WIDTH, HEIGHT

    pattern = [
        "0200000000021200000000020",
        "0520000000218120000000250",
        "0552000000218120000002550",
        "0555550002189812000555550",
        "0655555555189815555555560",
        "0065550055555555500555600",
        "0000650600555550060560000",
        "0000065006059506005600000",
        "0000006550059500556000000",
        "0000000065529255600000000",
        "0000000006529256000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000005059505000000000",
        "0000000050009000500000000",
        "0000000055555555500000000",
        "0000000552222222550000000",
        "0000000521111111250000000",
        "0000000521888881250000000",
        "0000000000999990000000000",
        "0000000005000005000000000",
        "0000000005000005000000000",
        "0000000600000000060000000",
        "0000000766000006670000000",
        "0000000077666667700000000",
        "0000000000777770000000000",
        "0000000000000000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "5":
                img.put("#351c75", (x,y))
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

def make_hit_capturing_enemy_sprite_3():
    global WIDTH, HEIGHT

    pattern = [
        "0200000000021200000000020",
        "0520000000218120000000250",
        "0552000000218120000002550",
        "0555550002189812000555550",
        "0655555555189815555555560",
        "0065550055555555500555600",
        "0000650600555550060560000",
        "0000065006059506005600000",
        "0000006550059500556000000",
        "0000000065529255600000000",
        "0000000006529256000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000005059505000000000",
        "0000000050009000500000000",
        "0000000055555555500000000",
        "0000000552222222550000000",
        "0000000521111111250000000",
        "0000000521888881250000000",
        "0000000000999990000000000",
        "0000000005000005000000000",
        "0000000005000005000000000",
        "0000000600000000060000000",
        "0000000766000006670000000",
        "0000060077666667700600000",
        "0000076000777770006700000",
        "0000006000000000006000000",
        "0000007600000000067000000",
        "0000000766000006670000000",
        "0000000077666667700000000",
        "0000000000777770000000000",
        "0000000000000000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "5":
                img.put("#351c75", (x,y))
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

def make_hit_capturing_enemy_sprite_4():
    global WIDTH, HEIGHT

    pattern = [
        "0200000000021200000000020",
        "0520000000218120000000250",
        "0552000000218120000002550",
        "0555550002189812000555550",
        "0655555555189815555555560",
        "0065550055555555500555600",
        "0000650600555550060560000",
        "0000065006059506005600000",
        "0000006550059500556000000",
        "0000000065529255600000000",
        "0000000006529256000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000000529250000000000",
        "0000000005059505000000000",
        "0000000050009000500000000",
        "0000000055555555500000000",
        "0000000552222222550000000",
        "0000000521111111250000000",
        "0000000521888881250000000",
        "0000000000999990000000000",
        "0000000005000005000000000",
        "0000000005000005000000000",
        "0000000600000000060000000",
        "0000000766000006670000000",
        "0000060077666667700600000",
        "0000076000777770006700000",
        "0000006000000000006000000",
        "0000007600000000067000000",
        "0006000766000006670006000",
        "0007600077666667700067000",
        "0000600000777770000060000",
        "0000760000000000000670000",
        "0000076000000000006700000",
        "0000006000000000006000000",
        "0000007660000000667000000",
        "0000000776666666770000000",
        "0000000007777777000000000",
        "0000000000000000000000000",
        "0000000000000000000000000"
    ]

    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width = w, height = h)
    
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "5":
                img.put("#351c75", (x,y))
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
hit_capt_enemy_img = make_hit_capturing_enemy_sprite()
player_laser_img = make_player_laser_sprite()
enemy_laser_img = make_enemy_laser_sprite()
capturing_enemy_1_img = make_capturing_enemy_sprite_1()
capturing_enemy_2_img = make_capturing_enemy_sprite_2()
capturing_enemy_3_img = make_capturing_enemy_sprite_3()
capturing_enemy_4_img = make_capturing_enemy_sprite_4()
hit_capturing_enemy_1_img = make_hit_capturing_enemy_sprite_1()
hit_capturing_enemy_2_img = make_hit_capturing_enemy_sprite_2()
hit_capturing_enemy_3_img = make_hit_capturing_enemy_sprite_3()
hit_capturing_enemy_4_img = make_hit_capturing_enemy_sprite_4()


player = canvas.create_image(WIDTH//2, HEIGHT-40, image = player_img, anchor="center")
capt_player = canvas.create_image(WIDTH//2, HEIGHT-80, image = capt_player_img, anchor = "center")
base_enemy = canvas.create_image(WIDTH//2, HEIGHT-120, image = basic_enemy_img, anchor = "center")
shoot_enemy = canvas.create_image(WIDTH//2, HEIGHT-160, image = shoot_enemy_img, anchor = "center")
capt_enemy = canvas.create_image(WIDTH//2, HEIGHT-200, image = capt_enemy_img, anchor = "center")
hit_capt_enemy = canvas.create_image(WIDTH//2, HEIGHT-240, image = hit_capt_enemy_img, anchor = "center")
play_laser = canvas.create_image(WIDTH//2, HEIGHT - 280, image = player_laser_img, anchor = "center")
enemy_laser = canvas.create_image(WIDTH//2, HEIGHT-320, image = enemy_laser_img, anchor = "center")
capturing_enemy_1 = canvas.create_image(WIDTH//1.5, HEIGHT-120, image = capturing_enemy_1_img, anchor = "center")
capturing_enemy_2 = canvas.create_image(WIDTH//1.5, HEIGHT-160, image = capturing_enemy_2_img, anchor = "center")
capturing_enemy_3 = canvas.create_image(WIDTH//1.5, HEIGHT-220, image = capturing_enemy_3_img, anchor = "center")
capturing_enemy_4 = canvas.create_image(WIDTH//1.5, HEIGHT-280, image = capturing_enemy_4_img, anchor = "center")
hit_capturing_enemy_1 = canvas.create_image(WIDTH//2.5, HEIGHT-120, image = hit_capturing_enemy_1_img, anchor = "center")
hit_capturing_enemy_2 = canvas.create_image(WIDTH//2.5, HEIGHT-160, image = hit_capturing_enemy_2_img, anchor = "center")
hit_capturing_enemy_3 = canvas.create_image(WIDTH//2.5, HEIGHT-220, image = hit_capturing_enemy_3_img, anchor = "center")
hit_capturing_enemy_4 = canvas.create_image(WIDTH//2.5, HEIGHT-280, image = hit_capturing_enemy_4_img, anchor = "center")


enemy_list = [capt_player_img, basic_enemy_img, shoot_enemy_img, capt_enemy_img, hit_capt_enemy_img]
enemies = [] # a list to store our enemies

def create_enemy_formation():
    global enemies
    enemies.clear()
    start_x = 100
    start_y = 60

    for r in range(ROWS):
        for c in range (COLS):
            x = start_x + c * CELL
            y = start_y + r * CELL

            e = canvas.create_image(x, y, image = random.choice(enemy_list), anchor = "nw")

            enemies.append(e)

def move_enemies():
    global enemy_dx, enemy_move_speed

    hit_wall = False
    for e in enemies:
        x1, y1, x2, y2 = canvas.bbox(e)
        
        if x2 >= WIDTH-10 and enemy_dx > 0:
            hit_wall = True
        elif x1 <= 10 and enemy_dx < 0:
            hit_wall = True

    if hit_wall:
        enemy_dx = -enemy_dx
        for e in enemies:
            canvas.move(e, 0, 150)
    else:
        for e in enemies:
            canvas.move(e, enemy_dx, 0)

def move_left(event):
    px1, py1, px2, py2 = canvas.bbox(player)
    if px1 <= 30:
        pass
    else:
        canvas.move(player, -15, 0)

def move_right(event):
    px1, py1, px2, py2 = canvas.bbox(player)
    if px1 >= (WIDTH-42):
        pass
    else:
        canvas.move(player, 15, 0)

root.bind("a", move_left)
root.bind("<Left>", move_left)
root.bind("d", move_right)
root.bind("<Right>", move_right)

lasers = []

def shoot(event):
    global play_laser
    
    if len(lasers)>1:
        return
        
    #BOUNDING BOXES
    px1, py1, px2, py2 = canvas.bbox(player)
    l = canvas.create_image((px1+px2)//2, py1, image = player_laser_img, anchor = "s")
    
    lasers.append(l)

def collision(a, l):
    """global capt_enemy, capturing_enemy_1, capturing_enemy_2, capturing_enemy_3, capturing_enemy_4
    if a != capt_enemy and capturing_enemy_1 and capturing_enemy_2 and capturing_enemy_3 and capturing_enemy_4:
        ax1, ay1, ax2, ay2 = canvas.bbox(a) #alien BBox
        lx1, ly1, lx2, ly2 = canvas.bbox(l) #laser BBox
    """
    global ax1, ay1, ax2, ay2
    ax1, ay1, ax2, ay2 = canvas.bbox(a) #alien BBox
    lx1, ly1, lx2, ly2 = canvas.bbox(l) #laser BBox

    return ax1 < lx2 and ax2 > lx1 and ay1 < ly2 and ay2 > ly1 #Returns true when there is overlap

def ship_capture():
    pass

def second_ship():
    pass

root.bind("<space>", shoot)

alive = True

def blink():
    global restart_text, flashID
    counter = 0
    current_color = canvas.itemcget(restart_text, "fill")
    if current_color == "#000000":
        canvas.itemconfig(restart_text, fill = "#FFFFFF")   
    elif current_color == "#FFFFFF":
        canvas.itemconfig(restart_text, fill = "#000000")
    flashID = root.after(900, blink)

def game_loop():
    global alive, lasers, flashID, restart_text, ax1, ax2, ay1, ay2, enemies
    global capt_enemy, capturing_enemy_1, capturing_enemy_2, capturing_enemy_3, capturing_enemy_4
    global hit_capt_enemy, hit_capturing_enemy_1, hit_capturing_enemy_2, hit_capturing_enemy_3, hit_capturing_enemy_4

    if not alive:
        canvas.delete("all")
        canvas.create_text(WIDTH//2, HEIGHT//2, text = "GAME OVER", fill = "white", font = ("Terminal", 36))
        restart_text = canvas.create_text(WIDTH//2, HEIGHT//1.5, text = "RESTART", fill = "#000000", tags = "restart_button", font = ("Terminal", 24))
        blink()
        canvas.tag_bind("restart_button", "<Button-1>", restart)
        return
    

    move_enemies()
    

    #make our lasers move

    for l in lasers[:]: # "[:]" creates a phantom copy of the list, so that we affect the copy of a list, not the real list
        canvas.move(l, 0, -25)
        x1, y1, x2, y2 = canvas.bbox(l)
        if y2 < 0:
            canvas.delete(l)
            lasers.remove(l)

    
    #Laser VS. Alien

    for l in lasers[:]:
        for e in enemies[:]:
            if collision(l, e):
                if e != capt_enemy:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    break
                elif e != capt_enemy and e != capturing_enemy_1:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    break
                elif e != capt_enemy and capturing_enemy_1 and capturing_enemy_2:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    break
                elif e != capt_enemy and capturing_enemy_1 and capturing_enemy_2 and capturing_enemy_3:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    break
                elif e != capturing_enemy_4:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    break

                elif e == capt_enemy:
                    ex1, ey1, ex2, ey2 = canvas.bbox(e)
                    x=(ex1+ex2)//2
                    y=(ey1+ey2)//2
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                   
                    capt_enemy = canvas.create_image(x, y, image = hit_capt_enemy_img, anchor = "center")
                    enemies.append(capt_enemy)

                elif e == capturing_enemy_1:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    x=(ax1+ax2)//2
                    y=(ay1+ay2)//2
                    capturing_enemy_1 = canvas.create_image(x, y, image = capturing_enemy_1_img, anchor = "center")
                    
                elif e== capturing_enemy_2:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    x=(ax1+ax2)//2
                    y=(ay1+ay2)//2
                    capturing_enemy_2 = canvas.create_image(x, y, image = capturing_enemy_2_img, anchor = "center")
                    
                elif e== capturing_enemy_3:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    x=(ax1+ax2)//2
                    y=(ay1+ay2)//2
                    capturing_enemy_3 = canvas.create_image(x, y, image = capturing_enemy_3_img, anchor = "center")
                    
                elif e== capturing_enemy_4:
                    canvas.delete(l)
                    canvas.delete(e)
                    if l in lasers:
                        lasers.remove(l)
                    if e in enemies:
                        enemies.remove(e)
                    x=(ax1+ax2)//2
                    y=(ay1+ay2)//2
                    capturing_enemy_4 = canvas.create_image(x, y, image = capturing_enemy_4_img, anchor = "center")
                    
    
    #End Game Condition

    for e in enemies:
        ex1, ey1, ex2, ey2 = canvas.bbox(e)
        px1, py1, px2, py2 = canvas.bbox(player)

        if ey2 >= py1:
            alive = False
    
    
    root.after(40, game_loop)

#Start Game and Reset

def start():
    global player

    #Create the player
    player = canvas.create_image(WIDTH//2, HEIGHT-40, image = player_img, anchor="center")
    game_loop()

def restart(event):
    global alive, enemy_dx, enemies, flashID
    canvas.delete("all")
    lasers.clear()
    enemies.clear()
    
    alive = True
    enemy_dx = enemy_move_speed

    if flashID is not None:
        root.after_cancel(flashID)
        flashID = None
        
    # 2. Reset text and start a fresh loop
    canvas.itemconfig(restart_text, fill="white")
    
    canvas.delete("all")
    enemies = []
    
    create_enemy_formation()
    start()

root.bind("r", restart)
#Score System




#High Score System


restart(flashID)

root.mainloop()