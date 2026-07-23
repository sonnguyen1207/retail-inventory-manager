def revenue_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        p.ProductName,
                        SUM(s.Quantity) AS UnitsSold,
                        SUM(s.TotalAmount) AS Revenue
                    FROM Sales s
                    JOIN Products p
                    ON s.ProductID = p.ProductID
                    GROUP BY p.ProductName
                    ORDER BY Revenue DESC
                    """)

    rows = cursor.fetchall()

    print("\n=== PRODUCT REVENUE REPORT ===\n")

    for product_name, units_sold, revenue in rows:
        print(f"Product : {product_name}")
        print(f"Units   : {units_sold}")
        print(f"Revenue : €{float(revenue):.2f}")
        print("-" * 30)

    conn.close()