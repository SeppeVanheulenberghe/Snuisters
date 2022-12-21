# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:47:20 2022.

@author: Seppe
"""

from docx import Document
from docx.shared import Cm
from typing import List


class Purchase_Sheet(object):
    """Responsible for writing the purchase sheets docx."""

    def __init__(self, inventory_dict: dict):
        self.inventory = inventory_dict

    def open_doc(self, template_name: str) -> None:
        """Initialize Document object."""
        self.doc = Document(template_name)

    def make_doc_table(self, rows: int, cols: int) -> None:
        """Add table to document."""
        self.table = self.doc.add_table(rows, cols)

    def fill_header(self, labels: List[str]) -> None:
        """Fill in header labels in tabel."""
        header = self.table.rows[0].cells
        for i, label in enumerate(labels):
            header[i].text = label

    def fill_tabel(self) -> None:
        """Fill in table with inventory items."""
        for i in range(1, len(self.inventory) + 1):
            name = list(self.inventory.keys())[i - 1]
            item = self.inventory[name]

            row = self.table.rows[i].cells
            row[0].text = item.name
            paragraph = row[0].paragraphs[0]
            run = paragraph.add_run()
            try:
                run.add_picture(
                    "./images/" + self.inventory[name].image, width=Cm(2))

            except TypeError:
                row[0].text += "\n\nimage not found\n"

            row[1].text = "€ " + f"{item.price:.2f}"
            row[2].text = "€ " + f"{item.profit:.2f}"
            row[3].text = str(item.number)

    def set_table_style(self, style: str) -> None:
        """Set the table style of the purchase sheet."""
        self.table.style = style

    def create(
        self, doc_name: str, template_name: str, table_style: str = "Plain Table 1"
    ) -> None:
        """Create purchase sheet document."""
        templates_dir = 'templates/'
        self.open_doc(templates_dir + template_name + '.docx')
        rows, cols = len(self.inventory) + 1, 5
        self.make_doc_table(rows, cols)
        labels = ["Artikel", "Prijs", "Winstmarge", "Geleverd", "Verkocht"]
        self.fill_header(labels)
        self.fill_tabel()
        self.set_table_style(table_style)
        self.doc.save(doc_name)
