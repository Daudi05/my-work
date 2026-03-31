import requests

My_URL = "http://127.0.0.1:5000"

def view_inventory():
    res = requests.get(f"{My_URL}/inventory")
    print(res.json())

def add_item():
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    res = requests.post(f"{My_URL}/inventory", json={
        "product_name": name,
        "price": price,
        "stock": stock
    })

    print(res.json())

def update_item():
    item_id = input("Item ID: ")
    price = input("New price: ")
    stock = input("New stock: ")

    res = requests.patch(f"{My_URL}/inventory/{item_id}", json={
        "price": float(price),
        "stock": int(stock)
    })

    print(res.json())

def delete_item():
    item_id = input("Item ID: ")
    res = requests.delete(f"{My_URL}/inventory/{item_id}")
    print("Deleted!" if res.status_code == 204 else "Error")

def fetch_external():
    barcode = input("Enter barcode: ")
    res = requests.get(f"{My_URL}/external/{barcode}")
    print(res.json())

def menu():
    while True:
        print("\n--- Inventory CLI ---")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Fetch Product (API)")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            fetch_external()
        elif choice == "6":
            break

if __name__ == "__main__":
    menu()