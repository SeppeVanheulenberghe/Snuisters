from tkinter import *
import customtkinter
from enum import Enum
from typing import List
# from dataclasses import dataclass
from packages.inventory import Inventory
from packages.purchase_sheet import Snuisters_Purchase_Sheet


class EntryBox(object):
    """Create button executor """

    NAMES = ["INVENTORY_EXCEL_ENTRY", "OUTFILE_DOCX_ENTRY",
             "HOST_ENTRY", "TEMPLATE_DOCX_ENTRY"]

    def __init__(self, ENTRY_BOXES):
        self.ENTRY_BOXES = ENTRY_BOXES

    def EmptyEntryBox(self, entry_box: customtkinter.CTkEntry) -> None:
        """Empty the given entry boxes."""
        entry_box.delete(0, END)

    def EmptyAllEntryBoxes(self) -> None:
        """Empty all given entry boxes"""
        for box in self.ENTRY_BOXES.values():
            self.EmptyEntryBox(box)

    def ReadEntryBox(self, entry_box):
        """Read entry box."""
        return entry_box.get()

    @property
    def GetInventoryName(self) -> str:
        """Get name of inventory xlsx file"""
        INVENTORY_NAME = self.ENTRY_BOXES["INVENTORY_EXCEL_ENTRY"].get()
        return INVENTORY_NAME

    @property
    def GetPurchaseSheetName(self) -> str:
        """Get name of purchase sheet docx"""
        OUTFILE_DOCX_ENTRY = self.ENTRY_BOXES["OUTFILE_DOCX_ENTRY"].get()
        return OUTFILE_DOCX_ENTRY

    @property
    def GetHostName(self) -> str:
        """Get host name"""
        HOST = self.ENTRY_BOXES["HOST_ENTRY"].get()
        return HOST

    @property
    def GetTemplateName(self) -> str:
        """Get name of template docx"""
        TEMPLATE_NAME = self.ENTRY_BOXES["TEMPLATE_DOCX_ENTRY"].get()
        return TEMPLATE_NAME


def CreatePurchaseSheet(ENTRY_BOXES):
    """Create the purchase sheet"""
    IMAGES_FILEPATH = "./images"

    # CREATE EntryBox OBJECT
    entry_box = EntryBox(ENTRY_BOXES)

    # READ DETAILS
    INVENTORY_NAME = entry_box.GetInventoryName
    PURCHASE_SHEET_NAME = entry_box.GetPurchaseSheetName
    HOST = entry_box.GetHostName
    TEMPLATE_NAME = entry_box.GetTemplateName
    DETAILS = (HOST, TEMPLATE_NAME, PURCHASE_SHEET_NAME)

    # MAKE Inventory OBJECT
    inventory = Inventory(INVENTORY_NAME, IMAGES_FILEPATH)
    inventory.set_details = DETAILS

    # CREATE PURCHASE SHEET
    purchase_sheet = Snuisters_Purchase_Sheet(inventory)
    purchase_sheet.create(PURCHASE_SHEET_NAME, TEMPLATE_NAME)
