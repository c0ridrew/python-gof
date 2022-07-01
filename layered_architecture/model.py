from abc import ABC
from dataclasses import dataclass
from typing import List

class Food(ABC):
  name: str
  calorie: int
  is_cut: bool
  is_cooked: bool


class Vegetable(Food):
  pass


class Meat(Food):
  pass


@dataclass()
class Curry():
  ingredients: List[Food]
  calorie: int
  amount: int
  spicy: int


class Chef():
  def cut_vegetables(vegetables: List[Vegetable]):
    for vegetable in vegetables:
      vegetable.is_cut = True
      print(f"cut {vegetable.name}")

  def cut_meats(meats: List[Meat]):
    for meat in meats:
      meat.is_cut = True
      print(f"cut {meat.name}")

  def cook_with_pan():
    print("cook with pan")

  def boil_water():
    print("boil water")

def main():
  pass

