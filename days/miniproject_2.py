import pyodbc
from datetime import datetime

try:
    server = r"LAPTOP-2HCHVK65\SQLEXPRESS"
    database = "hotel_sahil"

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    print("Connected to hotel_sahil 🔥")

    # 🔹 Step 1: Show Menu
    print("\n------ MENU ------")
    cursor.execute("SELECT menu_id, item_name, price FROM Menu")
    menu_items = cursor.fetchall()

    for item in menu_items:
        print(f"{item.menu_id}. {item.item_name} - ₹{item.price}")

    # 🔹 Step 2: Take Order Input
    selected_id = int(input("\nEnter Menu ID to order: "))
    quantity = int(input("Enter Quantity: "))

    # 🔹 Step 3: Insert Order
    cursor.execute(
        "INSERT INTO Orders (menu_id, quantity) VALUES (?, ?)",
        (selected_id, quantity)
    )
    conn.commit()

    print("Order Placed Successfully ✅")

        # 🔹 Step 4: Generate Bill
    print("\n------ BILL ------")

    cursor.execute("""
    SELECT O.order_id, M.item_name, M.price, O.quantity,
    (M.price * O.quantity) AS total_price,
    O.order_date
    FROM Orders O
    JOIN Menu M ON O.menu_id = M.menu_id
    WHERE O.order_id = SCOPE_IDENTITY()
    """)

    bill = cursor.fetchone()

    print(f"Order ID   : {bill.order_id}")
    print(f"Item       : {bill.item_name}")
    print(f"Price      : ₹{bill.price}")
    print(f"Quantity   : {bill.quantity}")
    print(f"Total      : ₹{bill.total_price}")
    print(f"Order Date : {bill.order_date}")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
