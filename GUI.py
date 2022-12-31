from tkinter import *
import customtkinter
from main import create_document_from_GUI


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('Purchase Sheet Application')
root.geometry("500x350")


ENTRY_BOXES = {}


# Tabview
tabview = customtkinter.CTkTabview(root)
tabview.pack(padx=20, pady=20)
SHEET_TAB = "Sheet"
ADVANCED_TAB = "Advanced"
tabview.add(SHEET_TAB)
tabview.add(ADVANCED_TAB)
tabview.set(SHEET_TAB)


# SHEET_TAB
# Entry boxes
NAME = "InventoryName"  # "INVENTORY_EXCEL_ENTRY"
name_inventory_excel_entry = customtkinter.CTkEntry(
    master=tabview.tab(SHEET_TAB),
    placeholder_text='inventory file name (.xslx)',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_inventory_excel_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_inventory_excel_entry

NAME = "PurchaseSheetName"  # "OUTFILE_DOCX_ENTRY"
name_outfile_docx_entry = customtkinter.CTkEntry(
    master=tabview.tab(SHEET_TAB),
    placeholder_text='output file name (.docx)',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_outfile_docx_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_outfile_docx_entry

NAME = "HostName"  # "HOST_ENTRY"
name_host_entry = customtkinter.CTkEntry(
    master=tabview.tab(SHEET_TAB),
    placeholder_text='host name',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_host_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_host_entry


# Create Button
create_button = customtkinter.CTkButton(
    master=tabview.tab(SHEET_TAB),
    text='CREATE',
    width=200, height=40,
    compound="top",
    # EntryBox(ENTRY_BOXES).EmptyAllEntryBoxes()
    command=lambda: create_document_from_GUI(ENTRY_BOXES)
)
create_button.pack(pady=20)

# ADVANCED_TAB
# Entry boxes
NAME = "TemplateName"  # "TEMPLATE_DOCX_ENTRY"
name_template_entry = customtkinter.CTkEntry(
    master=tabview.tab(ADVANCED_TAB),
    placeholder_text='template file name (.docx)',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_template_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_template_entry

root.mainloop()
