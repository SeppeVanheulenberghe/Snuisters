# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:47:20 2022.

@author: Seppe
"""

from docx import Document
from docx.shared import Cm
from typing import List
from packages.inventory import Inventory


class Purchase_Sheet(object):
    """Responsible for writing the purchase sheets docx."""

    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.inventory_dict = inventory.get_inventory_dict
        self.inventory_details = inventory.details

    def open_doc(self, template_name: str) -> None:
        """Initialize Document object."""
        self.doc = Document(template_name)

    def add_heading(self, header: str, level: int):
        """Add new heading to Document object"""
        return self.doc.add_heading(header, level)

    def add_paragraph(self):
        """Add new paragraph to Document object."""
        return self.doc.add_paragraph()

    def add_text_to_paragraph(self, paragraph_name: str, text: str):
        """Add text to already existing paragraph by name"""
        paragraph_name.add_run(text)

    def add_host_to_details(self, details):
        """Add the host of the inventory to the Document object"""
        host = f"ONTVANGER: {self.inventory_details.host}"
        self.add_text_to_paragraph(details, host)

    def make_details_paragraph(self):
        self.add_heading('Details', 1)
        details = self.add_paragraph()
        self.add_host_to_details(details)

    def make_doc_table(self, rows: int, cols: int) -> None:
        """Add table to document."""
        self.table = self.doc.add_table(rows, cols)

    def fill_table_header(self, labels: List[str]) -> None:
        """Fill in header labels in tabel."""
        header = self.table.rows[0].cells
        for i, label in enumerate(labels):
            header[i].text = label

    def fill_table(self) -> None:
        """Fill in table with inventory items."""
        for i in range(1, len(self.inventory_dict) + 1):
            name = list(self.inventory_dict.keys())[i - 1]
            item = self.inventory_dict[name]

            row = self.table.rows[i].cells
            row[0].text = item.name
            paragraph = row[0].paragraphs[0]
            run = paragraph.add_run()
            try:
                run.add_picture(
                    "./images/" + self.inventory_dict[name].image, width=Cm(2))

            except TypeError:
                row[0].text += "\n\nimage not found\n"

            row[1].text = "€ " + f"{item.price:.2f}"
            row[2].text = "€ " + f"{item.profit:.2f}"
            row[3].text = str(item.number)

    @property
    def get_inventory_details_host(self) -> str:
        """Get host of inventory from Details object."""
        return self.inventory_details.host

    def set_table_style(self, style: str) -> None:
        """Set the table style of the purchase sheet."""
        self.table.style = style

    def create(
        self, doc_name: str, template_name: str, table_style: str = "Plain Table 1"
    ) -> None:
        """Create purchase sheet document."""
        # opening new document
        templates_dir = 'templates/'
        self.open_doc(templates_dir + template_name + '.docx')
        # adding details about inventory
        self.make_details_paragraph()
        # making table for inventory items
        rows, cols = len(self.inventory_dict) + 1, 5
        self.make_doc_table(rows, cols)
        labels = ["Artikel", "Prijs", "Winstmarge", "Geleverd", "Verkocht"]
        self.fill_table_header(labels)
        self.fill_table()
        self.set_table_style(table_style)
        self.doc.save(doc_name)
