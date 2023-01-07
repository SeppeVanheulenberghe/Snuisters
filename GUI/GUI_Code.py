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


class HostAddressStreetEntryBoxHandler():
    """HostAddressStreet entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.host_address_street = entry_box.get()

    def empty(self) -> None:
        self.entry_box.delete(0, END)

    @property
    def get(self):
        return self.host_address_street


class HostAddressCityEntryBoxHandler():
    """HostAddressCity entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.host_address_city = entry_box.get()

    def empty(self) -> None:
        self.entry_box.delete(0, END)

    @property
    def get(self):
        return self.host_address_city


class HostPhoneNumberEntryBoxHandler():
    """HostPhoneNumber entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.host_phone_number = entry_box.get()

    def empty(self) -> None:
        self.entry_box.delete(0, END)

    @property
    def get(self):
        return self.host_phone_number


class HostCompanyNameEntryBoxHandler():
    """HostCompanyName entry box handler."""

    def read(self, entry_box: customtkinter.CTkEntry) -> str:
        self.entry_box = entry_box
        self.host_company_name = entry_box.get()

    def empty(self) -> None:
        self.entry_box.delete(0, END)

    @property
    def get(self):
        return self.host_company_name


class DocumentTypeOptionMenuHandler():
    """DocumentTypeOptionMenu handler codec."""

    def read(self, option_menu: customtkinter.CTkOptionMenu) -> str:
        self.option_menu = option_menu
        self.document_type = option_menu.get()

    def empty(self) -> None:
        pass

    @property
    def get(self):
        return self.document_type


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


HANDLERS = {"InventoryName": InventoryNameEntryBoxHandler(),
            "PurchaseSheetName": PurchaseSheetNameEntryBoxHandler(),
            "HostName": HostNameEntryBoxHandler(),
            "HostAddressStreet": HostAddressStreetEntryBoxHandler(),
            "HostAddressCity": HostAddressCityEntryBoxHandler(),
            "HostPhoneNumber": HostPhoneNumberEntryBoxHandler(),
            "HostCompanyName": HostCompanyNameEntryBoxHandler(),
            "TemplateName": TemplateNameEntryBoxHandler(),
            "DocumentTypeOptionMenu": DocumentTypeOptionMenuHandler(),
            }


class GUIController():
    """Controls all elements of the gui. Processes data retrieved from GUI interface"""

    def __init__(self, ENTRY_BOXES):
        self.ENTRY_BOXES = ENTRY_BOXES

    def retrieve_gui_info(self):
        """Retrieve info from gui input elements."""
        for name, handler in HANDLERS.items():
            gui_element = self.ENTRY_BOXES[name]
            handler.read(gui_element)
            handler.empty()

    def retrieve_host_name(self):
        """Retrieve host name from gui."""

    # def retrieve_host_info_from_gui(self):
    #     """Retrieve host information from gui input element."""

    @property
    def InventoryName(self):
        """Get inventory name."""
        return HANDLERS["InventoryName"].get

    @property
    def PurchaseSheetName(self):
        """Get purchase sheet name."""
        return HANDLERS["PurchaseSheetName"].get

    @property
    def HostName(self):
        """Get host name."""
        return HANDLERS["HostName"].get

    @property
    def HostAddressStreet(self):
        """Get street + nr of host address."""
        return HANDLERS["HostAddressStreet"].get

    @property
    def HostAddressCity(self):
        """Get city of host address."""
        return HANDLERS["HostAddressCity"].get

    @property
    def HostPhoneNumber(self):
        """Get host phone number."""
        return HANDLERS["HostPhoneNumber"].get

    @property
    def HostCompanyName(self):
        """Get host company name."""
        return HANDLERS["HostCompanyName"].get

    @property
    def HostCompanyName(self):
        """Get host company name."""
        return HANDLERS["HostCompanyName"].get

    @property
    def DocumentType(self):
        """Get document type."""
        return HANDLERS["DocumentTypeOptionMenu"].get

    @property
    def TemplateName(self):
        """Get template name."""
        return HANDLERS["TemplateName"].get
