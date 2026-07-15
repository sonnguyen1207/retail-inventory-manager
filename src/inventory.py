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


if __name__ == "__main__":
    show_products()
