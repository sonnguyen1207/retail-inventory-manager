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
        print(product)

    conn.close()


if __name__ == "__main__":
    show_products()
