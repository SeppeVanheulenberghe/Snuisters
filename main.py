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
from packages.purchase_sheet import Purchase_Sheet


images_filepath = "./images"
inventory_name = "Bestelbon.xlsx"

# make Inventory object
inventory = Inventory(inventory_name, images_filepath)
template_name = inventory.details.template_name
inventory_dict = inventory.get_inventory_dict
# inventory = Inventory(inventory_name, images_filepath).get_inventory_dict

# write purchase sheet
purchase_sheet = Purchase_Sheet(inventory_dict)
purchase_sheet.create("Bestelbon.docx", template_name)
