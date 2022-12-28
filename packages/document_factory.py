from typing import Protocol
from packages.inventory import Inventory
from packages.purchase_sheet import Snuisters_Purchase_Sheet


class DocumentCreator(Protocol):
    """Basis representation of a document creation codec."""

    def prepare_document(self) -> None:
        """Prepare document for creation."""

    def create_document(self) -> None:
        """Create document."""


class SnuistersPurchaseSheetCreator():
    """Purchase sheet creation codec."""
    IMAGES_FILEPATH = "./images"

    def prepare_document(self, inventory: Inventory) -> None:
        self.purchase_sheet = Snuisters_Purchase_Sheet(inventory)

    def create_document(self, PURCHASE_SHEET_NAME: str, TEMPLATE_NAME: str) -> None:
        self.purchase_sheet.create(PURCHASE_SHEET_NAME, TEMPLATE_NAME)


class DocumentCreatorFactory(Protocol):
    """Factory that contains a document codec."""

    def get_document_creator(self) -> DocumentCreator:
        """Return a new document creator belonging to this factory"""


class SnuistersPurchaseSheetFactory():
    """Factory aimed at creating a Snuister purchase sheet."""

    def get_document_creator(self) -> DocumentCreator:
        return SnuistersPurchaseSheetCreator


def read_creator(doc_creator: str) -> DocumentCreatorFactory:
    """Return the selected document creator factory."""
    factories = {"Snuisters Purchase Sheet": SnuistersPurchaseSheetCreator}
    return factories[doc_creator]
