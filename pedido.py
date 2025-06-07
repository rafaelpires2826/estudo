import csv
import os
from datetime import datetime

ORDERS_FILE = "orders.csv"


def send_order(item, quantity):
    order_id = datetime.now().strftime("%Y%m%d%H%M%S")
    order = [order_id, item, quantity]
    header = ["id", "item", "quantity"]
    file_exists = os.path.isfile(ORDERS_FILE)
    with open(ORDERS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(order)
    print(f"Pedido enviado: {order_id}")


def main():
    while True:
        item = input("Item (vazio encerra): ").strip()
        if not item:
            break
        quantity = input("Quantidade: ").strip()
        send_order(item, quantity)


if __name__ == "__main__":
    main()
