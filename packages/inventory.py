# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:01:02 2022.

@author: Seppe
"""

import pandas as pd
from dataclasses import dataclass
from os import listdir
from typing import Any


@dataclass
class InventoryItem(object):
    """Item in an inventory."""

    name: str
    price: float
    profit: float
    number: int
    image_folder_filepath: str = ""
    image: str = ""

    def create_images_list(self) -> list[str]:
        """Make a list of images inside images-folder."""
        images = [
            im.lower().replace(" ", "") for im in listdir(self.image_folder_filepath)
        ]
        return images

    def find_image(self) -> str:
        """Find name-like image in images folder."""
        images = self.create_images_list()
        name = self.name.lower().replace(" ", "")
        for im in images:
            im_name = im.lower().replace(" ", "")
            if name in im_name:
                return im

    def set_image(self) -> None:
        """Set image of Item object."""
        self.image = self.find_image()


class Inventory(object):
    """Inventory object containing inventory items."""

    def __init__(self, inventory_name: str, image_folder_filepath: str):
        self.db = pd.read_excel(inventory_name)
        self.inventory = {}
        self.image_folder_filepath = image_folder_filepath
        self.fill_inventory_dict()

    def add_inventory_item(self, item: Any) -> Any:
        """Add Inventory_Item to to inventory."""
        name = item.name
        self.inventory[name] = item

    def read_from_inventory_database(self, name: str) -> tuple:
        """Return parameters of Inventory_Item object."""
        db_item = self.db[self.db["Artikel"] == name]
        price = float(db_item["Prijs"])
        profit = float(db_item["Winstmarge"])
        number = int(db_item["Geleverd"])
        return name, price, profit, number

    def fill_inventory_dict(self) -> None:
        """Fill inventory dictionary with items from database."""
        for n in self.db["Artikel"]:
            name, price, profit, number = self.read_from_inventory_database(n)
            item = InventoryItem(
                name, price, profit, number, self.image_folder_filepath
            )
            item.set_image()
            self.add_inventory_item(item)

    @property
    def get_inventory_dict(self) -> dict:
        """Return inventory dictionary."""
        return self.inventory


if __name__ == "__main__":
    images_filepath = "./images"
    inventory_name = "Bestelbon.xlsx"
    inventory_items = Inventory(inventory_name, images_filepath)
    # Inventory.fill_inventory_dict()
    inventary_dict = inventory_items.get_inventory_dict
