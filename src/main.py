from inventory import show_products, show_low_stock, add_product
from sales import sell_product, return_product, sales_report, revenue_report

while True:

    print("\nRetail Inventory Manager")
    print("0. Exit")
    print("1. Show Products")
    print("2. Sell Product")
    print("3. Low Stock Alerts")
    print("4. Add Product")
    print("5. Return Product")
    print("6. Sales Report")
    print("7. Revenue Report")

    choice = input("Choice: ")
    if choice == "0":
        break
    elif choice == "1":
        show_products()

    elif choice == "2":
        product_id = int(input("Product ID: "))
        quantity = int(input("Quantity: "))

        sell_product(product_id, quantity)

    elif choice == "3":
        show_low_stock()

    elif choice == "4":
        add_product()
    elif choice == "5":
        product_id = int(input("Product ID: "))
        quantity = int(input("Return quantity: "))

        return_product(product_id, quantity)
    elif choice == "6":
        sales_report()
    elif choice == "7":
        revenue_report()
