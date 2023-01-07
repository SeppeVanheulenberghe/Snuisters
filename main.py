from tkinter import *
import customtkinter
from packages.inventory import Inventory
from packages.document_factory import read_creator
from GUI.GUI_Code import GUIController
from datetime import datetime


def create_document_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]):
    """Main document creation codec."""
    # prepare GUI
    gui = GUIController(ENTRY_BOXES)
    gui.retrieve_gui_info()

    # get info
    INVENTORY_NAME = gui.InventoryName
    PURCHASE_SHEET_NAME = gui.PurchaseSheetName
    HOST_NAME = gui.HostName
    TEMPLATE_NAME = gui.TemplateName
    DETAILS = (HOST_NAME, TEMPLATE_NAME, PURCHASE_SHEET_NAME)

    # testing
    HOST_ADDRESS_STREET = gui.HostAddressStreet
    print(HOST_ADDRESS_STREET)
    HOST_ADDRESS_CITY = gui.HostAddressCity
    print(HOST_ADDRESS_CITY)
    HOST_PHONE_NUMBER = gui.HostPhoneNumber
    print(HOST_PHONE_NUMBER)
    HOST_COMPANY_NAME = gui.HostCompanyName
    print(HOST_COMPANY_NAME)
    DOCUMENT_TYPE = gui.DocumentType
    print(DOCUMENT_TYPE)

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

    print(f"""========================================================
    DOCUMENT CREATED: {datetime.now()}
    NAME: {PURCHASE_SHEET_NAME}
    HOST: {HOST_NAME}
    INVENTORY: {INVENTORY_NAME}
    TEMPLATE: {TEMPLATE_NAME}
========================================================
                        """)
