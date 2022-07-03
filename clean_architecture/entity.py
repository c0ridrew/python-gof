from dataclasses import dataclass
from typing import List


@dataclass()
class Ingredient:
    name: str
    calorie: int
    is_cut: bool = False
    is_cooked: bool = False


@dataclass()
class Seasoning:
    name: str
    calorie: int
    is_added: bool = False


@dataclass()
class Curry:
    name = "curry"
    calorie: int
    ingredints: List[Ingredient]
    seasonings: List[Seasoning]


@dataclass()
class Nikujyaga:
    name = "nikujyaga"
    calorie: int
    ingredints: List[Ingredient]
    seasonings: List[Seasoning]
