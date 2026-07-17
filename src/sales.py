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

# sell_product(2, 1)
