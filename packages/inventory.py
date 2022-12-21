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


@dataclass
class Details(object):
    """Store sheet details."""

    host: str
    template_name: str


class Inventory(object):
    """Inventory object containing inventory items."""

    def __init__(self, inventory_name: str, image_folder_filepath: str):
        self.inventory_name = inventory_name
        self.inventory = {}
        self.image_folder_filepath = image_folder_filepath
        self.fill_inventory_dict()

    def make_inventory_dataframe(self) -> Any:
        """Write inventory items to pandas dataframe."""
        return pd.read_excel(self.inventory_name, sheet_name='Order')

    def make_details_dataframe(self) -> Any:
        """Write inventory details to pandas dataframe"""
        return pd.read_excel(self.inventory_name, sheet_name='Details')

    def get_item_parameters_from_dataframe(self, name: str) -> tuple:
        """Return parameters for Inventory_Item object."""
        inventory_df = self.make_inventory_dataframe()
        db_item = inventory_df[inventory_df["Artikel"] == name]
        price = float(db_item["Prijs"])
        profit = float(db_item["Winstmarge"])
        number = int(db_item["Geleverd"])
        return name, price, profit, number

    def get_details_from_dataframe(self):
        """Return details from details dataframe."""
        details_df = self.make_details_dataframe()
        host = details_df['Ontvanger'].item()
        template_name = details_df['Template'].item()
        return host, template_name

    def make_inventory_item(self, item_parameters: tuple) -> InventoryItem:
        """Make InventoryItem object."""
        name, price, profit, number = item_parameters
        return InventoryItem(name, price, profit, number, self.image_folder_filepath)

    def make_inventory_details(self, details: tuple) -> Details:
        """Make details object."""
        host, template_name = details
        return Details(host, template_name)

    def add_inventory_item(self, item: Any) -> Any:
        """Add Inventory_Item to to inventory."""
        name = item.name
        self.inventory[name] = item

    def fill_inventory_dict(self) -> None:
        """Fill inventory dictionary with items from dataframe."""
        for n in self.get_item_names:
            item_parameters = self.get_item_parameters_from_dataframe(n)
            item = self.make_inventory_item(item_parameters)
            item.set_image()
            self.add_inventory_item(item)

    @property
    def get_inventory_dict(self) -> dict:
        """Return inventory dictionary."""
        return self.inventory

    @property
    def get_item_names(self):
        """Get names from inventory items."""
        return self.make_inventory_dataframe()["Artikel"]

    @property
    def details(self) -> Details:
        details = self.get_details_from_dataframe()
        return self.make_inventory_details(details)


if __name__ == "__main__":
    images_filepath = "./images"
    inventory_name = "Bestelbon.xlsx"

    # make Inventory object
    inventory = Inventory(inventory_name, images_filepath)
    df = inventory.make_details_dataframe()
