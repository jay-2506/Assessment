import datetime

inventory = {
    "dolo": {"price": 2.0, "stock": 50},
    "vitamin c": {"price": 5.0, "stock": 40},
    "dyzin": {"price": 1.5, "stock": 100}
}

sales = []


def show_inventory():
    global inventory
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n---- Current Inventory ----")
    print(f"{'Medicine':<15}{'Price':<15}{'Stock':<15}")
    print("-" * 35)
    for med, info in inventory.items():
        print(f"{med:<15}{info['price']:<15}{info['stock']:<15}")


        
def add_or_update_medicine():
    med = input("Enter medicine name: ").strip()
    try:
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input! Price and quantity must be numeric.")
        return

    if med in inventory:
        inventory[med]['price'] = price
        inventory[med]['stock'] += qty
        print(f"Updated {med}: New Price = {price}, Stock = {inventory[med]['stock']}")
    else:
        inventory[med] = {"price": price, "stock": qty}
        print(f"Added new medicine: {med}")





        
def process_sale():
    customer = input("Enter customer name: ").strip()
    medicine = input("Enter medicine name: ").strip()

    if medicine not in inventory:
        print("Medicine not found in inventory!")
        return

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a number!")
        return

    if qty > inventory[medicine]['stock']:
        print("Not enough stock available!")
        return

    total = qty * inventory[medicine]['price']
    inventory[medicine]['stock'] -= qty  # Deduct stock
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Record sale
    sales.append({"customer": customer, "medicine": medicine, "qty": qty, "total": total, "date": date})

    generate_bill(customer, medicine, qty, total, date)




    
def generate_bill(customer, medicine, qty, total, date):
    print("\n----- Bill -----")
    print(f"Customer: {customer}")
    print(f"Medicine: {medicine}")
    print(f"Quantity: {qty}")
    print(f"Total Amount: ₹{total}")
    print(f"Date: {date}")
    print("----------------\n")





def main_menu():
    while True:
        print("\n=== MediTrack Pharmacy System ===")
        print("1. View Inventory")
        print("2. Add / Update Medicine")
        print("3. Process Sale")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_or_update_medicine()
        elif choice == "3":
            process_sale()
        elif choice == "4":
            print("Exiting MediTrack. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    print("DEBUG INVENTORY AT START:", inventory)  # just to confirm
    main_menu()
