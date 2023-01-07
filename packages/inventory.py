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
    number_received: int
    image_folder_filepath: str = "./images"
    image: str = ""

    def create_images_list(self) -> list[str]:
        """Make a list of images from images-folder."""
        images = [
            im for im in listdir(self.image_folder_filepath)
        ]
        return images

    def find_image(self) -> str:
        """Find image with same name as InventoryItem from images_list."""
        images = self.create_images_list()
        name = self.name.lower().replace(" ", "")
        for im in images:
            im_name = im.lower().replace(" ", "").split('.')[0]
            if name == im_name:
                return im

    def set_image(self) -> None:
        """Set image of InventoryItem object."""
        self.image = self.find_image()


@dataclass
class Address():
    """Store Address information."""

    street: str
    city: str


@dataclass
class Host():
    """Store information about host."""

    name: str
    company_name: str
    address: Address
    phone_number: str


@dataclass
class Details(object):
    """Store sheet details."""

    host: str
    purchase_sheet_name: str


class Inventory(object):
    """Inventory object containing inventory items."""

    inventory: dict = {}

    def __init__(self, inventory_name: str, image_folder_filepath: str = "./images"):
        self.inventory_name = inventory_name
        self.image_folder_filepath = image_folder_filepath

    def retrieve_inventory_items_from_excel(self) -> pd.DataFrame:
        """Write inventory items to pandas dataframe."""
        return pd.read_excel(self.inventory_name, sheet_name='Order')

    def retrieve_inventory_item_parameters(self, item_name: str) -> tuple:
        """Return parameters for Inventory_Item object."""
        inventory_df = self.retrieve_inventory_items_from_excel()
        db_item = inventory_df[inventory_df["Artikel"] == item_name]
        price = float(db_item["Prijs"])
        profit = float(db_item["Winstmarge"])
        number = int(db_item["Aantal Ontvangen"])
        return item_name, price, profit, number

    def construct_inventory_item(self, item_parameters: tuple) -> InventoryItem:
        """Make InventoryItem object."""
        name, price, profit, number = item_parameters
        return InventoryItem(name, price, profit, number, self.image_folder_filepath)

    def construct_inventory_details(self, details: tuple) -> Details:
        """Make details object."""
        host, purchase_sheet_name = details
        return Details(host, purchase_sheet_name)

    def add_inventory_item(self, item: InventoryItem) -> None:
        """Add Inventory_Item to inventory instance variable."""
        name = item.name
        self.inventory[name] = item

    def store_AllItems_in_inventory(self) -> None:
        """Fill inventory dictionary with items from dataframe."""
        for n in self.get_AllItems_names:
            item_parameters = self.retrieve_inventory_item_parameters(n)
            item = self.construct_inventory_item(item_parameters)
            item.set_image()
            self.add_inventory_item(item)

    @property
    def AllItems(self) -> dict:
        """Return inventory dictionary."""
        self.store_AllItems_in_inventory()
        return self.inventory

    @property
    def get_AllItems_names(self):
        """Get names from inventory items."""
        return self.retrieve_inventory_items_from_excel()["Artikel"]

    @property
    def details(self):
        """Get inventory details"""
        return self.DETAILS

    @details.setter
    def set_details(self, details: tuple) -> None:
        """Set inventory details"""
        self.DETAILS = self.construct_inventory_details(details)

    def __len__(self):
        """Get the amount of inventory items"""
        return len(self.retrieve_inventory_items_from_excel())
