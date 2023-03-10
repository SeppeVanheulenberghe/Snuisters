from tkinter import *
import customtkinter
from packages.inventory import Inventory, Host, Address
from packages.document_factory import read_creator
from GUI.GUI_Code import GUIController
from datetime import datetime
from papertrail_log.papertrail_logging import LoggingToPapertrail

log = LoggingToPapertrail()


def create_document_from_GUI(ENTRY_BOXES: dict[str, customtkinter.CTkEntry]):
    """Main document creation codec."""
    # prepare GUI
    gui = GUIController(ENTRY_BOXES)
    gui.retrieve_gui_info()
    log.debug("GUI info retrieved")

    # get info
    INVENTORY_NAME = gui.InventoryName
    log.debug("inventory name stored")

    PURCHASE_SHEET_NAME = gui.PurchaseSheetName
    log.debug("purchase sheet name stored")

    HOST_NAME = gui.HostName
    log.debug("host name stored")

    HOST_ADDRESS_STREET = gui.HostAddressStreet
    log.debug("host address (street) stored")

    HOST_ADDRESS_CITY = gui.HostAddressCity
    log.debug("host address (city) stored")

    HOST_PHONE_NUMBER = gui.HostPhoneNumber
    log.debug("host phone number stored")

    HOST_COMPANY_NAME = gui.HostCompanyName
    log.debug("host company name stored")

    DOCUMENT_TYPE = gui.DocumentType
    log.debug("docment type stored")

    # create addres
    ADDRESS = Address(HOST_ADDRESS_STREET, HOST_ADDRESS_CITY)
    log.debug("address object created")

    # create host
    HOST = Host(HOST_NAME, HOST_COMPANY_NAME, ADDRESS, HOST_PHONE_NUMBER)
    log.debug("host object created")

    # create inventory
    inventory = Inventory(INVENTORY_NAME)
    log.debug("inventory object created")

    DETAILS = (HOST, PURCHASE_SHEET_NAME)
    inventory.set_details = DETAILS
    log.debug("inventory details set")

    # get document factory
    fac = read_creator(DOCUMENT_TYPE)
    log.debug("document factory retrieved")

    # retrieve document creator
    doc_creator = fac.get_document_creator()
    log.debug("document creator retrieved")

    # prepare document
    doc_creator.prepare_document(inventory)
    log.debug("document prepared")

    # create document
    doc_creator.create_document(PURCHASE_SHEET_NAME)
    log.info(f"DOCUMENT CREATED")
    log.info(f"NAME: {PURCHASE_SHEET_NAME}")
    log.info(f"HOST: {HOST_NAME}")
    log.info(f"INVENTORY: {INVENTORY_NAME}")

    print(
        f"""========================================================
    DOCUMENT CREATED: {datetime.now()}
    NAME: {PURCHASE_SHEET_NAME}
    HOST: {HOST_NAME}
    INVENTORY: {INVENTORY_NAME}
========================================================
                        """
    )
