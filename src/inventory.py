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


if __name__ == "__main__":
    # show_products()
    show_low_stock()
