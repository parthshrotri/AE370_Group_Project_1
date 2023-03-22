import numpy as np
from ..dynamics.body import Body
from ..properties import prop
from rk4 import Simulator

# Define system bodies
sun = Body(prop.mass_sun, )
mercury = Body(prop.mass_mercury,)
venus = Body(prop.mass_venus,)
earth = Body(prop.mass_earth,)
mars = Body(prop.mass_mars,)
jupiter = Body(prop.mass_jupiter, )
saturn = Body(prop.mass_saturn, )
uranus = Body(prop.mass_uranus, )
neptune = Body(prop.mass_neptune,)

