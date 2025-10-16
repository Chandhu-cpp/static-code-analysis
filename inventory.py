import json
from datetime import datetime


stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def removeItem(item, qty):
    """Remove a quantity of an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        print(f"Item '{item}' not found in stock: {e}")


def getQty(item):
    """Return the quantity of an item."""
    return stock_data[item]


def loadData(file="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)


def saveData(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def printData():
    """Print all items and their quantities."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def checkLowItems(threshold=5):
    """Return list of items below threshold quantity."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Run inventory demo."""
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    print("eval removed — safe print executed")


main()
