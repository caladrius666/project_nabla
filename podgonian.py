# coding: utf-8

import random
from terminal_parameters import *

def create_float_list(list, key):
    ind = list.index(key) + 1
    L = []
    while ind != len(list):
        if type(list[ind]) == float:
            L.append(list[ind])
            ind += 1
        else:
            break
    return L

def nabla_podgon(c_plot, mes1, mes2):
    x = create_float_list(c_plot[0], c_plot[0][1])
    y = create_float_list(c_plot[1], c_plot[1][1])
    desired_quotient = (y[int(mes2)] - y[int(mes1)])/(x[int(mes2)] - x[int(mes1)])
    delta_podgon(c_plot, desired_quotient)
    differ = y[int(mes1)] - c_plot[1][int(mes1)+2]
    for i in range(len(x)):
        c_plot[1][i + 2] += differ
    if args.show_podgon:
        do_show_podgon(c_plot)

def delta_podgon(c_plot, desired_quotient):
    if ('∇' in c_plot[0]) or ('Δ' in c_plot[0]):
        mass_center = get_mass_center(c_plot)
        free_quotient = mass_center[1] - desired_quotient*mass_center[0]
        need_podgon = create_need_podgon_list(c_plot, desired_quotient, free_quotient)
        do_dirty_hack(c_plot, need_podgon)
        do_hide_podgon(c_plot)
        if args.show_podgon:
            if '∇' not in c_plot[0]:
                do_show_podgon(c_plot)

def get_mass_center(c_plot):
    x = create_float_list(c_plot[0], c_plot[0][1])
    y = create_float_list(c_plot[1], c_plot[1][1])
    mass_x = sum(x)/len(x)
    mass_y = sum(y)/len(y)
    return [mass_x, mass_y]

def create_need_podgon_list(c_plot, desired_quotient, free_quotient):
    x = create_float_list(c_plot[0], c_plot[0][1])
    y = create_float_list(c_plot[1], c_plot[1][1])
    need_podgon =[]
    for i in range(len(x)):
        need_podgon.append((desired_quotient*x[i]+free_quotient)-y[i])
    return need_podgon

def do_dirty_hack(c_plot, need_podgon):
    for i in range(len(need_podgon)):
        c_plot[1][i+2] += need_podgon[i]

def do_hide_podgon(c_plot):
    y = create_float_list(c_plot[1], c_plot[1][1])
    if 'brutality' in c_plot[0]:
        brute = float(c_plot[0][c_plot[0].index('brutality') + 1])
    else:
        brute = 250
    yraz = (max(y) - min(y))/brute
    for i in range(len(y)):
        c_plot[1][i+2] += yraz*random.randint(-5, 5)

def do_show_podgon(c_plot):
    x = create_float_list(c_plot[0], c_plot[0][1])
    y = create_float_list(c_plot[1], c_plot[1][1])
    print(x)
    print(y)
