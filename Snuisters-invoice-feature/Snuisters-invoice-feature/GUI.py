from tkinter import *
import customtkinter
from main import create_document_from_GUI


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('Purchase Sheet Application')
root.geometry("500x430")


ENTRY_BOXES = {}


# Tabview
tabview = customtkinter.CTkTabview(root)
tabview.pack(padx=1, pady=1)
DOCUMENT_TAB = "Document"
INFO_TAB = "Info"
tabview.add(DOCUMENT_TAB)
tabview.add(INFO_TAB)
tabview.set(DOCUMENT_TAB)

# ============================================
# SHEET_TAB
# ============================================

# Entry boxes
# --------------------------------------------

NAME = "InventoryName"
name_inventory_excel_entry = customtkinter.CTkEntry(
    master=tabview.tab(DOCUMENT_TAB),
    placeholder_text='inventory file name (.xslx)',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
name_inventory_excel_entry.pack(pady=10)
name_inventory_excel_entry.insert(END, "Bestelbon.xlsx")
ENTRY_BOXES[NAME] = name_inventory_excel_entry

NAME = "PurchaseSheetName"
name_outfile_docx_entry = customtkinter.CTkEntry(
    master=tabview.tab(DOCUMENT_TAB),
    placeholder_text='document name',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
name_outfile_docx_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_outfile_docx_entry

NAME = "DocumentTypeOptionMenu"
document_type_option_menu = customtkinter.CTkOptionMenu(
    master=tabview.tab(DOCUMENT_TAB),
    height=30,
    width=400,
    corner_radius=10,
    values=["Snuisters purchase sheet", "Snuisters invoice"]
)
document_type_option_menu.pack(pady=10)
document_type_option_menu.set("Snuisters purchase sheet")
ENTRY_BOXES[NAME] = document_type_option_menu

# Create Button
# --------------------------------------------

create_button = customtkinter.CTkButton(
    master=tabview.tab(DOCUMENT_TAB),
    text='CREATE',
    width=200, height=40,
    compound="top",
    command=lambda: create_document_from_GUI(ENTRY_BOXES)
)
create_button.pack(pady=20)

# ============================================
# ADVANCED_TAB
# ============================================

# Entry boxes
# --------------------------------------------

address_label = customtkinter.CTkLabel(
    master=tabview.tab(INFO_TAB),
    text="Host Name")
address_label.pack(padx=5, anchor=W)

NAME = "HostName"
name_host_entry = customtkinter.CTkEntry(
    master=tabview.tab(INFO_TAB),
    placeholder_text='host name',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
name_host_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_host_entry

address_label = customtkinter.CTkLabel(
    master=tabview.tab(INFO_TAB),
    text="Address")
address_label.pack(padx=5, anchor=W)

NAME = "HostAddressStreet"
host_address_street_entry = customtkinter.CTkEntry(
    master=tabview.tab(INFO_TAB),
    placeholder_text='street + nr',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
host_address_street_entry.pack(pady=10)
ENTRY_BOXES[NAME] = host_address_street_entry

NAME = "HostAddressCity"
host_address_city_entry = customtkinter.CTkEntry(
    master=tabview.tab(INFO_TAB),
    placeholder_text='City',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
host_address_city_entry.pack(pady=10)
ENTRY_BOXES[NAME] = host_address_city_entry

host_phone_number_label = customtkinter.CTkLabel(
    master=tabview.tab(INFO_TAB),
    text="Phone Number")
host_phone_number_label.pack(padx=5, anchor=W)

NAME = "HostPhoneNumber"
host_phone_number_entry = customtkinter.CTkEntry(
    master=tabview.tab(INFO_TAB),
    placeholder_text='+32',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
host_phone_number_entry.pack(pady=10)
host_phone_number_entry.insert(END, '+32')
ENTRY_BOXES[NAME] = host_phone_number_entry

host_company_name_label = customtkinter.CTkLabel(
    master=tabview.tab(INFO_TAB),
    text="Company Name")
host_company_name_label.pack(padx=5, anchor=W)

NAME = "HostCompanyName"
host_company_name_entry = customtkinter.CTkEntry(
    master=tabview.tab(INFO_TAB),
    placeholder_text='company name',
    width=400,
    height=30,
    border_width=1,
    corner_radius=10)
host_company_name_entry.pack(pady=10)
ENTRY_BOXES[NAME] = host_company_name_entry

root.mainloop()
