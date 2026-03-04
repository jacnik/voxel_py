from settings import (njit, np, glm, math, WIN_RES, BG_COLOR)
from world_objects.chunk import Chunk


class Scene:
    def __init__(self, app):
        self.app = app
        self.chunk = Chunk(self.app)

    def update(self):
        pass

    def render(self):
        self.chunk.render()
