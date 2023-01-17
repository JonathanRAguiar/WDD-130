import csv

from datetime import datetime


def main():
    try:
        product_code_index = 0
        product_code = 0
        product_name = 1
        product_Price = 2
        filename = "products.csv"
        products_dict = read_dict("products.csv", product_code_index)
        filename = "request.csv"
        count = count_items("request.csv")
        subtotal = calculate_subtotal(products_dict, "request.csv")
        sales_tax = calculate_tax(subtotal)
        order_total = calculate_total(subtotal, sales_tax)
        print("Inkom Emporium")
        print()
        print_items(products_dict, "request.csv")
        print()
        print(f"Number of Items: {count}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {order_total:.2f}")

        current_date_and_time = datetime.now()

        print()

        print("Thank you for shopping at the Inkom Emporium.")

        print(f"{current_date_and_time:%A %I:%M %p}")

    except KeyError as Error:
        print(f"{Error}: unknown product ID in the {filename} file")
        print(product_code)

    except FileNotFoundError as not_found:
        print("Error: missing file")
        print(f"[Error no 2] No such file or directory:", not_found.filename)

    except PermissionError as perm_err:
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print("You don't have permission to read filename.")
        print("Run the program again and enter the name" \
              " of a file that you are allowed to read.")


def calculate_total(subtotal, taxes):
    return subtotal + taxes


def calculate_tax(subtotal):
    return subtotal * 0.06


def calculate_subtotal(products_dict, filename):
    subtotal = 0
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                product_code = row_list[0]
                product_quantity = int(row_list[1])

                product_info = products_dict[product_code]

                product_price = float(product_info[2])

                subtotal_product = product_quantity * product_price

                subtotal += subtotal_product
    return subtotal


def count_items(filename):
    with open(filename, "rt") as csv_file:
        count = 0
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                quantity = int(row_list[1])
                count += quantity
        return count


def print_items(products_dict, filename):
    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                product_code = row_list[0]
                product_quantity = row_list[1]

                product_info = products_dict[product_code]

                product_name = product_info[1]
                product_price = product_info[2]

                print(f"{product_name}: {product_quantity} @ {product_price}")

    return product_code, filename  # type: ignore


def read_dict(filename, key_column_index):
    products_dict = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                key = row_list[key_column_index]

                products_dict[key] = row_list

    return products_dict


if __name__ == "__main__":
    main()