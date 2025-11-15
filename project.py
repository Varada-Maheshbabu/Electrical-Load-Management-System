import sqlite3


# =======================
# 1. SIMPLE APPLIANCE CLASS (Very Light OOP)
# =======================
class Appliance:
    def __init__(self, name, wattage, quantity):
        self.name = name
        self.wattage = wattage
        self.quantity = quantity

    def total_power(self):
        return self.wattage * self.quantity



# =======================
# 2. DATABASE MANAGER (ANSI SQL – No vendor-specific syntax)
# =======================
class DBManager:
    def __init__(self, db_name="electrical_load.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS appliances (
            id INTEGER PRIMARY KEY,
            name TEXT,
            wattage REAL,
            quantity INTEGER
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_appliance(self, appliance: Appliance):
        query = """
        INSERT INTO appliances (name, wattage, quantity)
        VALUES (?, ?, ?);
        """
        self.conn.execute(query, (appliance.name, appliance.wattage, appliance.quantity))
        self.conn.commit()

    def get_appliances(self):
        query = "SELECT * FROM appliances;"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def clear_all(self):
        self.conn.execute("DELETE FROM appliances;")
        self.conn.commit()



# =======================
# 3. LOAD CALCULATION SYSTEM (Current + MCB selection)
# =======================
class LoadCalculator:
    def __init__(self):
        self.total_load = 0  # in watts

    def add(self, appliance: Appliance):
        self.total_load += appliance.total_power()

    def calculate_current(self, voltage=230):
        return self.total_load / voltage

    def recommended_mcb(self):
        current = self.calculate_current()

        if current <= 6:
            return "6A MCB"
        elif current <= 10:
            return "10A MCB"
        elif current <= 16:
            return "16A MCB"
        elif current <= 20:
            return "20A MCB"
        else:
            return "32A or higher (Heavy Load)"



# =======================
# 4. MAIN APPLICATION
# =======================
class App:
    def __init__(self):
        self.db = DBManager()
        self.calc = LoadCalculator()

    def run(self):
        print("\n===== ELECTRICAL LOAD MANAGEMENT SYSTEM =====")

        # Load all existing data
        existing = self.db.get_appliances()
        for row in existing:
            name, watt, qty = row[1], row[2], row[3]
            a = Appliance(name, watt, qty)
            self.calc.add(a)

        while True:
            print("\n1. Add Appliance")
            print("2. View Appliances")
            print("3. Calculate Load")
            print("4. Clear All Data")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter appliance name: ")
                wattage = float(input("Enter wattage (W): "))
                quantity = int(input("Enter quantity: "))

                a = Appliance(name, wattage, quantity)
                self.db.add_appliance(a)
                self.calc.add(a)

                print("Appliance added successfully.")

            elif choice == "2":
                rows = self.db.get_appliances()
                print("\n--- Stored Appliances ---")
                for row in rows:
                    print(f"{row[0]}. {row[1]} - {row[2]}W x {row[3]}")
                if not rows:
                    print("No appliances stored.")

            elif choice == "3":
                total = self.calc.total_load
                current = self.calc.calculate_current()
                mcb = self.calc.recommended_mcb()

                print(f"\nTotal Connected Load : {total} W")
                print(f"Required Current     : {current:.2f} A")
                print(f"Recommended MCB      : {mcb}")

            elif choice == "4":
                self.db.clear_all()
                self.calc.total_load = 0
                print("All data cleared.")

            elif choice == "5":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice. Try again.")



# =======================
# RUN THE APP
# =======================
if __name__ == "__main__":
    App().run()

