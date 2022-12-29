from tkinter import *
import customtkinter
from enum import Enum


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
