from colr import color
import os
import random

colors = ['#FDBE96', '#A6E3E9', '#CBF1F5', '#E3FDFD', '#DDE7F2', '#B9BBDF', '#C79ECF']

def generateTree(path): 
    global colors
    tree = ""

    for root, dirs, files in os.walk(path):
        root = root.replace(path, "")
        level = root.count(os.sep)

        if level == 0:
            tree += color('{}\n'.format(path), fore=colors[0])
            for file in files:
                tree += color('{}|--'.format("  "*level), fore=colors[0])
                tree += color('{}\n'.format(file), random.choice(colors[1:]))

        else:
            tree += color('|{0}{1}\n'.format("--"*level, root), fore=colors[0], style='bright')
            for file in files:
                tree += color('|{}|--'.format("  "*level), fore=colors[0])
                tree += color('{}\n'.format(file), random.choice(colors[1:]))

        tree += color('|\n', fore=colors[0])
    return tree


def searchFile(dir_path, filename):
    global colors
    text = ""

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if filename in file:
                text += color('\n{}'.format(os.path.join(root,file)), random.choice(colors[1:]))
    return text


def main():
    settings = {}
    settings['path'] = os.getcwd()

    if settings.get('file_name', 0):
        output = searchFile(settings['path'], settings['file_name'])
        print(output)

    elif settings.get('path', 0):
        output = generateTree(settings['path'])
        print(output)
 

if __name__ == "__main__":   
    main()