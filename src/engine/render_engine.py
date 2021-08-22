from ursina import *


class RenderEngine(Ursina):
    def __init__(self, input_handler, update_handler, size):
        # window.windowed_size = Vec2(size[0],size[1])
        camera.orthographic = True
        camera.fov = 4
        camera.position = (1, 1)

        self.bg = Entity(parent=scene, model='quad', texture='shore', scale=(16, 8), z=0)
        # self.plane = Entity(model="plane", scale=size, origin=(-size[0]//2, -size[1]//2, 0 ), color=color.black)
        self.bg.update = update_handler
        self.input = input_handler
        super().__init__()


