from packages.inventory import InventoryItem, Inventory


def test_make_InventoryItem() -> None:
    name = "Name"
    price = 10.
    profit = 10.
    number = 1
    inventory_item = InventoryItem(name, price, profit, number)
    assert inventory_item.name == name and inventory_item.price == price and inventory_item.profit == profit and inventory_item.number == number


def test_Inventory_AllItems():
    inventory_name = 'Bestelbon.xlsx'
    inventory = Inventory(inventory_name)
    inventory_dataframe = inventory.read_inventory_items_from_excel()
    assert isinstance(inventory.AllItems, dict) and len(
        inventory) == len(inventory_dataframe)


# def test_make_Details() -> None:
#     host = "host"
#     template_name = "template_name"
#     purchase_sheet_name = "purchase_sheet_name"
#     details = Details(host, template_name, purchase_sheet_name)
#     host_bool = host == details.host
#     template_name_bool = template_name == details.template_name
#     purchase_sheet_name_bool = purchase_sheet_name == details.purchase_sheet_name
#     assert host_bool * template_name_bool * purchase_sheet_name_bool == True
