from tkinter import *
import customtkinter
from main import create_document_from_GUI


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('Purchase Sheet Application')
root.geometry("350x300")


ENTRY_BOXES = {}


# Tabview
tabview = customtkinter.CTkTabview(root)
tabview.pack(padx=1, pady=1)
SHEET_TAB = "Sheet"
ADVANCED_TAB = "Advanced"
tabview.add(SHEET_TAB)
tabview.add(ADVANCED_TAB)
tabview.set(SHEET_TAB)

# ============================================
# SHEET_TAB
# ============================================

# Entry boxes
# --------------------------------------------

NAME = "InventoryName"
name_inventory_excel_entry = customtkinter.CTkEntry(
    master=tabview.tab(SHEET_TAB),
    placeholder_text='inventory file name (.xslx)',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_inventory_excel_entry.pack(pady=10)
name_inventory_excel_entry.insert(END, "Bestelbon.xlsx")
ENTRY_BOXES[NAME] = name_inventory_excel_entry

NAME = "PurchaseSheetName"
name_outfile_docx_entry = customtkinter.CTkEntry(
    master=tabview.tab(SHEET_TAB),
    placeholder_text='document name',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_outfile_docx_entry.pack(pady=10)
ENTRY_BOXES[NAME] = name_outfile_docx_entry

NAME = "HostName"
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
# --------------------------------------------

create_button = customtkinter.CTkButton(
    master=tabview.tab(SHEET_TAB),
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

NAME = "TemplateName"
name_template_entry = customtkinter.CTkEntry(
    master=tabview.tab(ADVANCED_TAB),
    placeholder_text='template file name (.docx)',
    width=300,
    height=30,
    border_width=1,
    corner_radius=10)
name_template_entry.pack(pady=10)
name_template_entry.insert(END, 'template')
ENTRY_BOXES[NAME] = name_template_entry

NAME = "OptionMenu"
option_menu = customtkinter.CTkOptionMenu(
    master=tabview.tab(ADVANCED_TAB),
    values=["overzicht", "factuur"]
)
option_menu.pack(pady=10)
option_menu.set("overzicht")

root.mainloop()
