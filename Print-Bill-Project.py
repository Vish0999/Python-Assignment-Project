
import pyodbc

class Database:
    def __init__(self):
        server = r"Poonam\SQLEXPRESS01"
        database = "hotel_data"

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()
        print("Connected successfully")



class Hotel(Database):
    def __init__(self):
        super().__init__()
        self.menu = {}
        self.load_menu()

    def load_menu(self):
        self.menu.clear()
        self.cursor.execute("SELECT menu_name, price FROM menu")
        for name, price in self.cursor.fetchall():
            self.menu[name] = price

    def show_menu(self):
        print("\n------ MENU ------")
        for item, price in self.menu.items():
            print(f"{item:<15}{price:>5}")
        print("------------------")

    def add_menu_item(self):
        name = input("Enter new menu name: ").lower()
        price = int(input("Enter price: "))

        try:
            self.cursor.execute(
                "INSERT INTO menu(menu_name, price) VALUES (?, ?)",
                (name, price)
            )
            self.conn.commit()
            self.menu[name] = price
            print("Menu item added successfully")
        except:
            print("Menu already exists")


    def customer_Bill(self):
        cust_name = input("Enter customer name: ").lower()

        self.cursor.execute(
            "SELECT menu_name, quantity, price FROM orders WHERE cust_name=?",
            (cust_name,)
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("No order found for this customer")
            return

        print("\nmenu            quantity           price")
        print("-" * 45)

        for item, qty, price in rows:
            print(f"{item:<15}{qty:^15}{price:>10}")

        self.cursor.execute(
            "SELECT total_amount FROM bill WHERE cust_name=?",
            (cust_name,)
        )
        total = self.cursor.fetchone()[0]

        print("-" * 45)
        print(f"{'Total':<30}{total:>10}")



    def download_bill(self):
        cust_name = input("Enter customer name to download bill: ").lower()
        self.cursor.execute(
                "SELECT menu_name, quantity, price FROM orders WHERE cust_name=?",
                (cust_name,)
            )
        rows = self.cursor.fetchall()

        if not rows:
                print("No order found for this customer")
                return

        self.cursor.execute(
                "SELECT total_amount FROM bill WHERE cust_name=?",
                (cust_name,)
            )
        total = self.cursor.fetchone()[0]

        filename = f"{cust_name}.txt"

        with open(filename, "w") as file:
                file.write("------ HOTEL BILL ------\n")
                file.write(f"Customer Name: {cust_name}\n\n")
                file.write("Menu           Quantity        Price\n")
                file.write("-" * 45 + "\n")

                for item, qty, price in rows:
                    file.write(f"{item:<15}{qty:^15}{price:>10}\n")

                file.write("-" * 45 + "\n")
                file.write(f"{'Total':<30}{total:>10}\n")

        print(f"Bill downloaded successfully as {filename}")

            


            



class Order:
    def __init__(self, hotel):
        self.hotel = hotel
        self.items = {}
        self.total = 0

    def take_order(self):
        self.cust_name = input("Enter customer name: ").lower()

        while True:
            choice = input("Add item (Yes/No): ").lower()
            if choice in {"y", "yes"}:
                item = input("Enter item name: ").lower()
                if item in self.hotel.menu:
                    qty = int(input("Enter quantity: "))
                    self.items[item] = self.items.get(item, 0) + qty
                else:
                    print("Item not available")
            else:
                break

    def save_order(self):
        self.total = 0

        for item, qty in self.items.items():
            price = self.hotel.menu[item] * qty
            self.total += price

            self.hotel.cursor.execute(
                """INSERT INTO orders(cust_name, menu_name, quantity, price)
                   VALUES (?, ?, ?, ?)""",
                (self.cust_name, item, qty, price)
            )

        # bill table
        self.hotel.cursor.execute(
            "IF EXISTS (SELECT 1 FROM bill WHERE cust_name=?) "
            "UPDATE bill SET total_amount = total_amount + ? WHERE cust_name=? "
            "ELSE INSERT INTO bill(cust_name, total_amount) VALUES (?, ?)",
            (self.cust_name, self.total, self.cust_name,
             self.cust_name, self.total)
        )

        self.hotel.conn.commit()



    def print_bill(self):
        print("\nCustomer:", self.cust_name)
        print("\nmenu            quantity           price")
        print("-" * 45)

        self.hotel.cursor.execute(
            "SELECT menu_name, quantity, price FROM orders WHERE cust_name=?",
            (self.cust_name,)
        )

        for item, qty, price in self.hotel.cursor.fetchall():
            print(f"{item:<15}{qty:^15}{price:>10}")

        self.hotel.cursor.execute(
            "SELECT total_amount FROM bill WHERE cust_name=?",
            (self.cust_name,)
        )
        total = self.hotel.cursor.fetchone()[0]

        print("-" * 45)
        print(f"{'Total':<30}{total:>10}")



hotel = Hotel()

while True:
    print("""
1. Show Menu
2. Add New Menu
3. Take Order
4. print Bill
5. Download Bills
6. Exit
""")
    ch = input("Enter choice: ")

    if ch == "1":
        hotel.show_menu()

    elif ch == "2":
        hotel.add_menu_item()

    elif ch == "3":
        order = Order(hotel)
        order.take_order()
        order.save_order()

    elif ch == "4":
        hotel.customer_Bill()

    elif ch == "5":
        hotel.download_bill()

    elif ch == "6":
        break
    else:
        print("Invalid Selection !!!!! ")
        break
