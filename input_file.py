# coding: utf-8

def create_input(path):
    input = open_file(path)
    input = group_lines(input)
    prepare_to_work(input)
    return input

def open_file(path):
    input = open(path, 'r', encoding='utf-8')
    lines = input.readlines()
    lines_ = []
    for i in range(len(lines)):
        if lines[i] != '\n':
            lines_.append(lines[i])
    lines = lines_
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = list(map(str, lines[i].split()))
    return lines

def group_lines(lines):
    iden = []
    for line in lines:
        iden.append(line[0])
    iden2 = []
    for i in iden:
        if i not in iden2:
            iden2.append(i)
    iden = iden2
    for i in range(len(iden)):
        iden[i] = [iden[i]]
    for line in lines:
        for x in iden:
            if x[0] == line[0]:
                x = x.append(line)
    return iden

def prepare_to_work(input):
    for part in input:
        del part[0]
        for elem in part:
            for i in range(len(elem)):
                try:
                    elem[i] = float(elem[i])
                except:
                    pass
