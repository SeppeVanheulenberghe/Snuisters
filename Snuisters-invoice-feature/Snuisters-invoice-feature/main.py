from tkinter import *
import customtkinter
from packages.inventory import Inventory, Host, Address
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
    HOST_ADDRESS_STREET = gui.HostAddressStreet
    HOST_ADDRESS_CITY = gui.HostAddressCity
    HOST_PHONE_NUMBER = gui.HostPhoneNumber
    HOST_COMPANY_NAME = gui.HostCompanyName
    DOCUMENT_TYPE = gui.DocumentType

    # create addres
    ADDRESS = Address(HOST_ADDRESS_STREET, HOST_ADDRESS_CITY)

    # create host
    HOST = Host(HOST_NAME, HOST_COMPANY_NAME, ADDRESS, HOST_PHONE_NUMBER)

    # create inventory
    inventory = Inventory(INVENTORY_NAME)
    DETAILS = (HOST, PURCHASE_SHEET_NAME)
    inventory.set_details = DETAILS

    # get document factory
    fac = read_creator(DOCUMENT_TYPE)

    # retrieve document creator
    doc_creator = fac.get_document_creator()

    # prepare document
    doc_creator.prepare_document(inventory)

    # create document
    doc_creator.create_document(PURCHASE_SHEET_NAME)

    print(f"""========================================================
    DOCUMENT CREATED: {datetime.now()}
    NAME: {PURCHASE_SHEET_NAME}
    HOST: {HOST_NAME}
    INVENTORY: {INVENTORY_NAME}
========================================================
                        """)
