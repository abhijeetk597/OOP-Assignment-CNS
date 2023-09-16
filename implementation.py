from inventory import InventoryServices
from product import product
from prettytable import PrettyTable
from datetime import date
prod1 = product(p_id='1', p_name='Parle-G', price=9, qty=25, p_cat='B', m_date=date(year=2022, month=1, day=1),
      x_date=date(year=2025, month=2,day=2), disc=5)
prod2 = product(p_id='2', p_name='Dark Fantasy', price=60, qty=10, p_cat='B', m_date=date(year=2023, month=1, day=31),
      x_date=date(year=2026, month=5, day=5), disc=8)
prod3 = product(p_id='3', p_name='Buorbon', price=45, qty=25, p_cat='B', m_date=date(year=2023, month=2, day =2),
      x_date=date(year=2026, month=2,day=3), disc=12)
product_list = []
product_list.append(prod1)
product_list.append(prod2)
product_list.append(prod3)


def table(list):
    x = PrettyTable()
    x.field_names = ["Product ID", "Product Name", "Quantity", "Price (Rs.)", "Discount %", "Mfg Date", "Expiry Date"]
    for item in list:
        x.add_row([item.p_id, item.p_name, item.qty, item.price, item.disc, item.m_date, item.x_date])
    return x

class Dmart(InventoryServices):
    def add_product(self, prod):
        if type(prod) == product:
            if prod.p_id in [x.p_id for x in product_list]:
                print('This product already exist...\nPlease update product')
                return
            product_list.append(prod)
            print('Product successfully Added...')
            print('--------------------------------------------------')
        else:
            print('Invalid Product')
        return

    def delete_product(self, pid):
        if len(product_list) == 0:
            return print("Invalid choice/ Product List empty")
        if pid in [x.p_id for x in product_list]:
            for prod in product_list:
                if prod.p_id == pid:
                    product_list.remove(prod)
                    print("Product Successfully Deleted..")
                    break
        else:
            print('This product is not present in inventory')
        return

    def search_product(self, pid):
        if len(product_list) == 0:
            return print("Invalid choice/ Product List empty")
        for prod in product_list:
            if prod.p_id == pid:
                return table([prod])
        return None

    def update_product(self, pid):
        if len(product_list) == 0:
            return print("Invalid choice/ Product List empty")
        prod = self.search_product(pid)
        if prod:
            print(prod)
        else:
            print('This product is not in inventory. Please add product.')
            return
        print('Please enter new details below: ')
        # Date Function--------------------------
        from datetime import date
        def datefun():
            while True:
                try:
                    a, b, c = map(int, (list(input('in format dd-mm-yyyy: ').strip().split('-'))))
                    e = date(day=a, month=b, year=c)
                except:
                    print('Enter correct date as dd-mm-yyyy...')
                    continue
                if e:
                    return e
        # ------------------------------------------------------------
        for prod in product_list:
            if prod.p_id == pid:
                prod.qty = int(input("Enter new quantity   : "))
                prod.price = float(input("Enter new price      : "))
                print('Enter new Mfg Date')
                prod.m_date = datefun()
                print('Enter new Exp Date')
                prod.x_date = datefun()
                prod.disc = float(input('Enter new discount % : '))
        print("Product details updated successfully")
        print('--------------------------------------------------')
        return

    def product_in_price_range(self, start_price, end_price):
        if len(product_list) == 0:
            return "Invalid choice/ Product List empty"
        temp_list = []
        if start_price <= end_price:
            for prod in product_list:
                if start_price <= prod.price <= end_price:
                    temp_list.append(prod)
        else:
            print('Start Price Cannot be Greater Than End Price')
        return table(temp_list)

    def list_product(self):
        if len(product_list) == 0:
            return "Invalid choice/ Product List empty"
        return table(product_list)

    def maxPriceProd(self):
        if len(product_list) == 0:
            return "Invalid choice/ Product List empty"
        price = 0
        maxPProduct = None
        for prod in product_list:
            if prod.price > price:
                price = prod.price
                maxPProduct = prod
        return table([maxPProduct])

    def minPriceProd(self):
        if len(product_list) == 0:
            return "Invalid choice/ Product List empty"
        price = 999999999
        minPProduct = None
        for prod in product_list:
            if prod.price < price:
                price = prod.price
                minPProduct = prod
        return table([minPProduct])

    def discounted_price(self, pid):
        if len(product_list) == 0:
            return print("Invalid choice/ Product List empty")
        for prod in product_list:
            if prod.p_id == pid:
                x = PrettyTable()
                x.field_names = ['Product ID', 'Product Name', 'Regular Price (Rs)', 'Discounted Price (Rs)']
                x.add_row([prod.p_id, prod.p_name, prod.price, prod.price*(100-prod.disc)/100])
                return x


