# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:40:17 2022.

-------------------------------------------------------
This file write creates a purchase sheet (.docx)
with items imported from a database (.xlsx)
-------------------------------------------------------

@author: Seppe
"""

from packages.inventory import Inventory
from packages.purchase_sheet import Snuisters_Purchase_Sheet


IMAGES_FILEPATH = "./images"
INVENTORY_NAME = "Bestelbon.xlsx"

# make Inventory object
inventory = Inventory(INVENTORY_NAME, IMAGES_FILEPATH)
template_name = inventory.details.template_name
inventory_dict = inventory.AllItems

# write purchase sheet
purchase_sheet_name = inventory.details.purchase_sheet_name
purchase_sheet = Snuisters_Purchase_Sheet(inventory)
purchase_sheet.create(purchase_sheet_name, template_name)
