from tkinter import *
import customtkinter
from packages.inventory import Inventory
from packages.document_factory import read_creator
from GUI.GUI_Code import EntryBoxHandler, GUI


def create_document_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]):
    """Main document creation codec."""
    # prepare GUI
    gui = GUI(ENTRY_BOXES)
    gui.get_gui_info()

    # get info
    INVENTORY_NAME = gui.InventoryName
    PURCHASE_SHEET_NAME = gui.PurchaseSheetName
    HOST_NAME = gui.HostName
    TEMPLATE_NAME = gui.TemplateName
    DETAILS = (HOST_NAME, TEMPLATE_NAME, PURCHASE_SHEET_NAME)

    # create inventory
    inventory = Inventory(INVENTORY_NAME)
    inventory.set_details = DETAILS

    # get document factory
    fac = read_creator("Snuisters Purchase Sheet")

    # retrieve document creator
    doc_creator = fac.get_document_creator()

    # prepare document
    doc_creator.prepare_document(inventory)

    # create document
    doc_creator.create_document(PURCHASE_SHEET_NAME, TEMPLATE_NAME)
