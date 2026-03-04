from settings import (njit, np, glm, math, WIN_RES, BG_COLOR)
from meshes.quad_mesh import QuadMesh


class Scene:
    def __init__(self, app):
        self.app = app
        self.quad = QuadMesh(self.app)

    def update(self):
        pass

    def render(self):
        self.quad.render()
