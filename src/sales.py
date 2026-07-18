from db import get_connection


def sell_product(product_id, quantity):

    conn = get_connection()

    if not conn:
        return

    cursor = conn.cursor()

    cursor.execute("""
        SELECT ProductName,
               Price,
               StockQuantity
        FROM Products
        WHERE ProductID = ?
    """, (product_id,))

    # typically returns a tuple
    product = cursor.fetchone()

    if not product:
        print("Product not found.")
        conn.close()
        return

    # is called tuple unpacking in Python.
    name, price, stock = product

    if stock < quantity:
        print("Not enough stock.")
        conn.close()
        return

    total = price * quantity

    cursor.execute("""
        INSERT INTO Sales
        (ProductID, Quantity, TotalAmount)
        VALUES (?, ?, ?)
    """, (product_id, quantity, total))

    cursor.execute("""
        UPDATE Products
        SET StockQuantity = StockQuantity - ?
        WHERE ProductID = ?
    """, (quantity, product_id))

    conn.commit()

    print("\nSALE COMPLETED")
    print(f"Product: {name}")
    print(f"Quantity: {quantity}")
    print(f"Total: €{total:.2f}")

    conn.close()


def return_product(product_id, quantity):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ProductName
        FROM Products
        WHERE ProductID = ?
    """, (product_id,))

    product = cursor.fetchone()

    if not product:
        print("Product not found.")
        conn.close()
        return

    cursor.execute("""
        UPDATE Products
        SET StockQuantity = StockQuantity + ?
        WHERE ProductID = ?
    """, (quantity, product_id))

    conn.commit()

    print(f"{quantity} units returned.")

    conn.close()


def sales_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SaleID,
               ProductID,
               Quantity,
               TotalAmount,
               SaleDate
        FROM Sales
        ORDER BY SaleDate DESC
    """)

    rows = cursor.fetchall()

    print("\n=== SALES REPORT ===\n")

    for row in rows:
        print(
            f"Sale #{row[0]} | "
            f"Product {row[1]} | "
            f"Qty {row[2]} | "
            f"€{row[3]} | "
            f"{row[4]}"
        )

    conn.close()


def revenue_report():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(TotalAmount)
        FROM Sales
    """)

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\n=== REVENUE REPORT ===")
    print(f"Total Revenue: €{total:.2f}")

    conn.close()


# sell_product(2, 1)
# sales_report()
revenue_report()
