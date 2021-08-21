from ursina import Ursina, camera


class RenderEngine(Ursina):
    def __init__(self, input_handler, update_handler):
        camera.orthographic = True
        camera.fov = 4
        camera.position = (1, 1)
        super().__init__()
        self.input = input_handler
