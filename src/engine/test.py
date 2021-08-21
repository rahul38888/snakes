from ursina import *

matrix = None
index = (0, 0)
height = 15
width = 10


def input(key):
    if key == "space":
        matrix[index[0]][index[1]].color = color.green


if __name__ == '__main__':
    app = Ursina()

    matrix = [[Entity(model="sphere", color=color.red, scale=(0.5, 0.5, 0.5),
                      position=((j - width // 2) * 0.5, (i - height // 2) * 0.5), visible=True)
               for j in range(width)] for i in range(height)]

    app.run()
