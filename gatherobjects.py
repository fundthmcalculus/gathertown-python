from dataclasses import dataclass
from typing import Dict


@dataclass
class Point:
    """Class for keeping track of a location"""
    y: int
    x: int


@dataclass
class Object:
    y: int
    x: int
    id: str
    highlighted: str
    type: int
    height: int
    width: int
    properties: Dict
    scale: int


@dataclass
class Space:
    colored: bool
    spaceId: str
    x: int
    y: int


@dataclass
class Portal:
    x: int
    y: int
    targetMap: str
    targetX: int
    targetY: int
