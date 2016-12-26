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

def get_xy(c_plot):
    x = create_float_list(c_plot[0], c_plot[0][1])
    y = create_float_list(c_plot[1], c_plot[1][1])
    return [x, y]
