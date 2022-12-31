from tkinter import *
from typing import Protocol
import customtkinter


class EntryBoxHandler(Protocol):
    """Basic representation of an entry box handling codec"""

    def read(self, entry_box: customtkinter.CTkEntry):
        """Read entry box."""

    def empty(self):
        """Empty entry box."""

    @property
    def get(self):
        """Get entry box value"""


class InventoryNameEntryBoxHandler():
    """Inventory name entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.inventory_name = entry_box.get()

    def empty(self) -> None:
        pass
    
    @property
    def get(self):
        return self.inventory_name


class PurchaseSheetNameEntryBoxHandler():
    """Purchase sheet name entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.purchase_sheet_name = entry_box.get()

    def empty(self) -> None:
        self.entry_box.delete(0, END)

    @property
    def get(self):
        return self.purchase_sheet_name


class HostNameEntryBoxHandler():
    """Host name entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.host_name = entry_box.get()

    def empty(self) -> None:
        self.entry_box.delete(0, END)

    @property
    def get(self):
        return self.host_name


class TemplateNameEntryBoxHandler():
    """Template name entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.template_name = entry_box.get()

    def empty(self) -> None:
        pass

    @property
    def get(self):
        return self.template_name


class GUI():
    """Handles all element of the gui."""

    HANDLERS = {"InventoryName": InventoryNameEntryBoxHandler(),
                "PurchaseSheetName": PurchaseSheetNameEntryBoxHandler(),
                "HostName": HostNameEntryBoxHandler(),
                "TemplateName": TemplateNameEntryBoxHandler()
                }

    def __init__(self, ENTRY_BOXES):
        self.ENTRY_BOXES = ENTRY_BOXES

    def get_gui_info(self):
        """Retrieve info from gui input elements."""
        for name, handler in self.HANDLERS.items():
            gui_element = self.ENTRY_BOXES[name]
            handler.read(gui_element)
            handler.empty()

    @property
    def InventoryName(self):
        """Get inventory name."""
        return self.HANDLERS["InventoryName"].get

    @property
    def PurchaseSheetName(self):
        """Get purchase sheet name."""
        return self.HANDLERS["PurchaseSheetName"].get

    @property
    def HostName(self):
        """Get host name."""
        return self.HANDLERS["HostName"].get

    @property
    def TemplateName(self):
        """Get template name."""
        return self.HANDLERS["TemplateName"].get
