class Road:
    _surface_spec_gravity: float = 0.025

    def __init__(self, length, width):

        self._length = length
        self._width = width

    def get_surface_gravity(self, thickness):

        return (self._length * self._width * thickness * self._surface_spec_gravity)

r = Road(20, 5000)
print(f'Масса дорожного покрытия составит: {r.get_surface_gravity(5)} тонн')

