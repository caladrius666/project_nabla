# coding: utf-8

from podgonian import *
from terminal_parameters import *
import matplotlib.pyplot as plt
import numpy as np
from meta import *

def plot_show(plot):
    for i in range(len(plot)):
        ax = []
        for j in range(0, len(plot[i]), 2):
            plot_make([plot[i][j], plot[i][j+1]])
            if args.axis:
                do_axis([plot[i][j], plot[i][j+1]], ax)
                ax = do_axis([plot[i][j], plot[i][j+1]], ax)[:]
        if args.axis:
            plt.axis(ax)
        plt.show()

def plot_make(c_plot):
    do_podgon(c_plot)
    do_errors(c_plot)
    do_form(c_plot)
    do_connect_points(c_plot)
    do_approx(c_plot)
    do_labels(c_plot)
    do_utilities(c_plot)

def do_errors(c_plot):
    x, y = get_xy(c_plot)
    if 'err' in c_plot[0]:
        errx = create_float_list(c_plot[0], 'err')
        if len(errx) == 1:
            errx = errx * len(x)
    else:
        errx = [0] * len(x)
    if 'err' in c_plot[1]:
        erry = create_float_list(c_plot[1], 'err')
        if len(erry) == 1:
            erry = erry * len(x)
    else:
        erry = [0] * len(y)
    if ('err' not in c_plot[0]) and ('err' not in c_plot[1]):
        for i in range(len(x)):
            plt.plot(x[i], y[i])
    else:
        for i in range(len(x)):
            plt.errorbar(x[i], y[i], xerr=errx[i], yerr=erry[i], ecolor='k')

def do_approx(c_plot):
    if 'ap' in c_plot[0]:
        x, y = get_xy(c_plot)
        pos = c_plot[0].index('ap') + 1
        degree = int(c_plot[0][pos])
        xraz = (abs(max(x)-min(x)))/15
        a = np.arange(min(x)-xraz, max(x)+xraz, 0.001)
        p = np.poly1d(np.polyfit(x, y, degree))
        plt.plot(a, p(a), color='k')
        if args.show_approx:
            print('Уравнение', np.poly1d(np.polyfit(x, y, degree)))
            print('a=', np.polyfit(x, y, degree, cov = True)[0][0], 'b=', np.polyfit(x, y, degree, cov = True)[0][1])
            print('Δa=', np.polyfit(x, y, degree, cov = True)[1][0][0])
            print()

def do_labels(c_plot):
    plt.xlabel(str(c_plot[0][1]))
    plt.ylabel(str(c_plot[1][1]))
    plt.title(str(c_plot[0][0]))

def do_utilities(c_plot):
    if not(args.hide_grid):
        plt.grid(True)

def get_axis_parameters(c_plot):
    x, y = get_xy(c_plot)
    dx = abs(min(x)-max(x))/15
    dy = abs(min(y)-max(y))/15
    xmax = max(x) + dx
    xmin = min(x) - dx
    ymax = max(y) + dy
    ymin = min(y) - dy
    return [xmin, xmax, ymin, ymax]

def compare_axis_parameters(ax, newax):
    if newax[0] < ax[0]:
        ax[0] = newax[0]
    if newax[1] > ax[1]:
        ax[1] = newax[1]
    if newax[2] < ax[2]:
        ax[2] = newax[2]
    if newax[3] > ax[3]:
        ax[3] = newax[3]

def do_axis(c_plot, ax):
    if ax == []:
        ax = get_axis_parameters(c_plot)
    newax = get_axis_parameters(c_plot)
    compare_axis_parameters(ax, newax)
    return ax

def do_form(c_plot):
    x, y = get_xy(c_plot)
    if 'form' in c_plot[0]:
        pos = c_plot[0].index('form') + 1
        form = c_plot[0][pos]
        for i in range(len(x)):
            plt.plot(x[i], y[i], form)

def do_connect_points(c_plot):
    x, y = get_xy(c_plot)
    if 'cp' in c_plot[0]:
        plt.plot(x, y)

def do_podgon(c_plot):
    if 'nabla' in c_plot[0]:
        pos1 = c_plot[0].index('nabla') + 1
        pos2 = c_plot[0].index('nabla') + 2
        nabla_podgon(c_plot, float(c_plot[0][pos1]), float(c_plot[0][pos2]))
    elif 'delta' in c_plot[0]:
        pos = c_plot[0].index('delta') + 1
        delta_podgon(c_plot, float(c_plot[0][pos]))
