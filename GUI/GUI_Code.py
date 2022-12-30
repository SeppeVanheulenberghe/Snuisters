from tkinter import *
from typing import Protocol
import customtkinter
from dataclasses import dataclass


class EntryBoxHandler(Protocol):
    """Basic representation of an entry box handling codec"""

    def read_entry_box(self):
        """Read entry box."""

    def empty_entry_box(self):
        """Empty entry box."""


class InventoryNameEntryBoxHandler():
    """Inventory name entry box handler."""

    def __init__(self, entry_box: customtkinter.CTkEntry) -> None:
        self.entry_box = entry_box

    def read_entry_box(self):
        """Read entry box."""
        return self.entry_box.get()

    def empty_entry_box(self):
        """Empty entry box."""
        self.entry_box.delete(0, END)


class PurchaseSheetNameEntryBoxHandler():
    """Purchase sheet name entry box handler."""

    def __init__(self, entry_box: customtkinter.CTkEntry) -> None:
        self.entry_box = entry_box

    def read_entry_box(self):
        """Read entry box."""
        return self.entry_box.get()

    def empty_entry_box(self):
        """Empty entry box."""
        self.entry_box.delete(0, END)


class HostNameEntryBoxHandler():
    """Host name entry box handler."""

    def __init__(self, entry_box: customtkinter.CTkEntry) -> None:
        self.entry_box = entry_box

    def read_entry_box(self):
        """Read entry box."""
        return self.entry_box.get()

    def empty_entry_box(self):
        """Empty entry box."""
        self.entry_box.delete(0, END)


class TemplateNameEntryBoxHandler():
    """Template name entry box handler."""

    def __init__(self, entry_box: customtkinter.CTkEntry) -> None:
        self.entry_box = entry_box

    def read_entry_box(self):
        """Read entry box."""
        return self.entry_box.get()

    def empty_entry_box(self):
        """Empty entry box."""
        pass


class EntryBoxHandler(object):
    """Get information from entry boxes"""

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
