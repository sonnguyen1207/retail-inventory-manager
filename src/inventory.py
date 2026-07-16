from db import get_connection


def show_products():
    conn = get_connection()

    if not conn:
        return

    cursor = conn.cursor()

    cursor.execute("""
        SELECT ProductID,
               ProductName,
               Price,
               StockQuantity
        FROM Products
    """)

    products = cursor.fetchall()

    for product in products:
        print(
            f"ID: {product[0]} | "
            f"Name: {product[1]} | "
            f"Price: €{product[2]} | "
            f"Stock: {product[3]}"
        )

    conn.close()


def show_low_stock():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM LowStockAlerts
    """)

    rows = cursor.fetchall()

    print("\n=== LOW STOCK ALERTS ===")

    for row in rows:
        print(f"⚠️  {row[1]}")
        print(f"   Current Stock : {row[2]}")
        print(f"   Reorder Level : {row[3]}")
        print(f"   Supplier      : {row[4]}")
        print(f"   Contact       : {row[5]}")
        print(f"   Phone         : {row[6]}")
        print(f"   Email         : {row[7]}")
        print()

    conn.close()


def show_suppliers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SupplierID, SupplierName
        FROM Suppliers
    """)

    print("\n=== SUPPLIERS ===")

    for supplier_id, supplier_name in cursor.fetchall():
        print(f"{supplier_id}: {supplier_name}")

    conn.close()


def add_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))
    reorder_level = int(input("Reorder level: "))
    show_suppliers()
    supplier_id = int(input("Supplier ID: "))

    conn = get_connection()
    cursor = conn.cursor()
    # Check if supplier exists
    cursor.execute("""
        SELECT SupplierName
        FROM Suppliers
        WHERE SupplierID = ?
    """, (supplier_id,))

    supplier = cursor.fetchone()

    if not supplier:
        print(f"❌ Supplier ID {supplier_id} does not exist.")
        print("Please choose a valid supplier.")
        conn.close()
        return
    cursor.execute("""
        INSERT INTO Products
        (ProductName, Price, StockQuantity, ReorderLevel, SupplierID)
        VALUES (?, ?, ?, ?, ?)
    """, (name, price, stock, reorder_level, supplier_id))

    conn.commit()

    print(f"✅ Product '{name}' added successfully.")

    conn.close()


if __name__ == "__main__":
    # show_products()
    # show_low_stock()
    add_product()
