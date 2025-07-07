from inventory_utils import restock_product
import random

# Base Product Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} - Rs.{self.price} x {self.quantity} = Rs.{self.total_value():.2f}"


# PerishableProduct Subclass
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        total = super().total_value()
        if self.expiry_days < 5:
            return total * 0.8  # 20% discount
        return total


# Inventory Manager Class
class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def list_inventory(self):
        print("\n📦 Inventory List:")
        for i, product in enumerate(self.inventory, 1):
            print(f"{i}. {product}")

    def search_by_name(self, term):
        print(f"\n🔍 Searching for: '{term}'")
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.inventory))
        for product in results:
            print(product)
        if not results:
            print("No products found.")

    def restock_all(self):
        for product in self.inventory:
            product.quantity = restock_product()


# Export Summary Using Comprehension
def export_inventory_summary(manager):
    summary = {
        product.name: product.total_value()
        for product in manager.inventory
    }
    with open("inventory_report.txt", "w") as file:
        file.write("📝 Inventory Report\n")
        for name, value in summary.items():
            file.write(f"{name}: Rs.{value:.2f}\n")


# 🚀 Sample Usage
if __name__ == "__main__":
    inv = InventoryManager()
    inv.add_product(Product("Laptop", 75000, 2))
    inv.add_product(PerishableProduct("Milk", 180, 10, expiry_days=3))
    inv.add_product(PerishableProduct("Eggs", 12, 30, expiry_days=7))
    inv.add_product(Product("Pen", 20, 50))

    inv.list_inventory()
    inv.search_by_name("milk")
    inv.restock_all()
    export_inventory_summary(inv)
    print("\n✅ Inventory updated and report exported.")
