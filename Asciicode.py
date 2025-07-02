print("="*60)
print("STORY: ASCII and SALES ANALYSIS")
print("="*60)

orders = [
    {"OrderID": 1, "CustomerName": "Alice", "ProductCategory": "Electronics", "OrderAmount": 150.00, "City": "Bangalore"},
    {"OrderID": 2, "CustomerName": "Bob", "ProductCategory": "Clothing", "OrderAmount": 250.00, "City": "Bangalore"},
    {"OrderID": 3, "CustomerName": "Charlie", "ProductCategory": "Electronics", "OrderAmount": 90.00, "City": "Mumbai"},
    {"OrderID": 4, "CustomerName": "David", "ProductCategory": "Clothing", "OrderAmount": 200.00, "City": "Mumbai"},
    {"OrderID": 5, "CustomerName": "Eve", "ProductCategory": "Home Decor", "OrderAmount": 300.00, "City": "Bangalore"},
    {"OrderID": 6, "CustomerName": "Frank", "ProductCategory": "Electronics", "OrderAmount": 120.00, "City": "Delhi"},
    {"OrderID": 7, "CustomerName": "Grace", "ProductCategory": "Clothing", "OrderAmount": 220.00, "City": "Delhi"},
    {"OrderID": 8, "CustomerName": "Heidi", "ProductCategory": "Home Decor", "OrderAmount": 80.00, "City": "Mumbai"},
    {"OrderID": 9, "CustomerName": "Ivan", "ProductCategory": "Electronics", "OrderAmount": 180.00, "City": "Delhi"},
    {"OrderID": 10, "CustomerName": "Judy", "ProductCategory": "Clothing", "OrderAmount": 160.00, "City": "Bangalore"},
]

from collections import defaultdict

city_data = defaultdict(list)

for order in orders:
    if order["OrderAmount"] > 100:
        city_data[order["City"]].append(order["OrderAmount"])

print("="*60)
print("SALES SUMMARY BY CITY (FILTER: OrderAmount > 100, COUNT > 2)")
print("="*60)
for city, amounts in city_data.items():
    if len(amounts) > 2:
        total_orders = len(amounts)
        total_revenue = sum(amounts)
        average_order_value = total_revenue / total_orders

        print(f"{'CITY: ' + city.upper():<25}")
        print(f"  TOTAL ORDERS      : {total_orders}")
        print(f"  TOTAL REVENUE     : {total_revenue:.2f}")
        print(f"  AVERAGE ORDER VAL : {average_order_value:.2f}")
        print("-"*60)

print()
print("="*60)
print("ASCII DEMO")
print("="*60)
char = input("Enter any character to see its ASCII code: ")
ascii_code = ord(char)
print(f"The ASCII code for '{char}' is {ascii_code}")