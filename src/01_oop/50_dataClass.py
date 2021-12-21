"""
# Sumarry
- Syntax
- Frozen
- Optimizations
"""

from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

## Syntax
@dataclass
class Position:
    local:str
    lat:float
    lon:float

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
             
        return 2 * r * asin(sqrt(h))

## Frozen
@dataclass(frozen = True)
class ComptonPosition:
    name: str = "Compton"
    lat:int = 15
    lon:int = 33

## Optimize class
"""
https://docs.python.org/3/reference/datamodel.html#slots

-> style index attributes to search more easy
-> Less memory / Fast access attributes
"""
@dataclass
class environment:
    __slots__ = ['type_env','avg_temperature']
    type_env:str
    avg_temperature:float