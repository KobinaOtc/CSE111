import csv
# Exceeding the Requirements
import random
import string
from datetime import datetime, timedelta

def main():
    try:
        current_date_and_time = datetime.now()
        # Exceeding the Requirements: Write code to print a reminder of how many 
        # days until the New Years Sale begins (Jan 1) at the bottom of the 
        # receipt.
        future_date =  datetime(2026, 1, 1)
        return_date = current_date_and_time + timedelta(days=30)
        today = datetime.today()
        coupon_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        products = read_dictionary('products.csv', 0)
        items_array = []
        PRODUCT_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY_INDEX = 1
        total_items = 0
        sub_total = 0.00
        product_count = 0
        discount_price = 0.00
        discount_total = 0.00
        print('Inkom Emporium')
        with open('request.csv', 'rt') as file:
            file_read = csv.reader(file)
            next(file_read)
            for line in file_read:
                items_array.append(line)

        print('Requested Items')
        for item in items_array:
            product_index = products[item[PRODUCT_INDEX]]
            product_name = product_index[NAME_INDEX]
            price = product_index[PRICE_INDEX]
            quantity = item[QUANTITY_INDEX]
            total_items += int(quantity)
            sub_total += float(price) * int(quantity)
            if product_index[PRODUCT_INDEX] == 'D083':
                discount_price = float(price)
                product_count += 1
            print(f'{product_name}: {quantity} @ {price}')

        sales_tax = get_sales_tax(sub_total, 0.06) 
        total = sub_total + sales_tax    
        if product_count > 1:
            discount_total = total - discount_price

        random_prod = random.choice(items_array)
        days_remining = (future_date - today).days
        print(f'Number of Items: {total_items}\nSubtotal: {sub_total:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}\nTotal: {total:.2f}')
        print('Thank you for shopping at the Inkom Emporium.')
        # Exceeding the Requirements
        print(f'{days_remining} days remaining until the New Years Sale begins (Jan 1)')
        print(f'Return by: {return_date} at 9:00 PM\nDiscount price is: {discount_total:.2f}')
        print(f'Reward: Coupon for 50% off {products[random_prod[0]][1]}. Code: {coupon_code}')
        print(f'{current_date_and_time:%a %b %_d %H:%M:%S %Y}')


    except KeyError as e:
        print(f'Error: unknown product ID in the request.csv file {e}')
    except PermissionError as e:
        print(f'You do not have the permissions to access this file {e}')
    except FileNotFoundError as e:
        print(f'Error: missing file\n{e}')

def read_dictionary(filename, key_column_index=0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    items = {}
    with open(filename, 'rt') as file:
        file_read = csv.reader(file)

        next(file_read)

        for line in file_read:
            items[line[key_column_index]] = line
    return items

def get_sales_tax(total, rate):
    sales_tax = total * rate
    return sales_tax

    

if '__main__' == __name__:
    main()