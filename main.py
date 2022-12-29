from tkinter import *
import customtkinter
from packages.inventory import Inventory
from packages.document_factory import read_creator
from GUI.GUI_Code import EntryBox


def get_details_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]) -> tuple[str, tuple[str, str, str]]:
    """Get the inventory details from the GUI."""
    entry_box = EntryBox(ENTRY_BOXES)
    INVENTORY_NAME = entry_box.GetInventoryName
    PURCHASE_SHEET_NAME = entry_box.GetPurchaseSheetName
    HOST = entry_box.GetHostName
    TEMPLATE_NAME = entry_box.GetTemplateName
    DETAILS = (HOST, TEMPLATE_NAME, PURCHASE_SHEET_NAME)
    return INVENTORY_NAME, DETAILS


def get_inventory_name_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]):
    """Get inventory name from GUI."""
    entry_box = EntryBox(ENTRY_BOXES)
    return entry_box.GetInventoryName


def create_inventory_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]):
    """Inventory creation from GUI codec."""
    INVENTORY_NAME, DETAILS = get_details_from_GUI(ENTRY_BOXES)
    inventory = Inventory(INVENTORY_NAME)
    inventory.set_details = DETAILS
    return inventory


def create_document_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]):
    """Main document creation codec."""
    # create inventory
    inventory = create_inventory_from_GUI(ENTRY_BOXES)
    PURCHASE_SHEET_NAME = inventory.details.purchase_sheet_name
    TEMPLATE_NAME = inventory.details.template_name

    # get document factory
    fac = read_creator("Snuisters Purchase Sheet")

    # retrieve document creator
    doc_creator = fac.get_document_creator()

    # prepare document
    doc_creator.prepare_document(inventory)

    # create document
    doc_creator.create_document(PURCHASE_SHEET_NAME, TEMPLATE_NAME)
