class product:
    def __init__(self, p_id, p_name, price, qty, p_cat, m_date, x_date, disc = 0):
        self.p_id = p_id
        self.p_name = p_name
        self.price = price
        self.qty = qty
        self.p_cat = p_cat
        self.m_date = m_date
        self.x_date = x_date
        self.disc = disc

    def __str__(self):
        return f'Product: {self.p_name} | ID: {self.p_id} | Qty: {self.qty} | \
    Price: {self.price} | Mfg Date: {self.m_date} | Expiry Date: {self.x_date}'
    def __repr__(self):
        return str(self)

def product_details():
    #Date Function--------------------------
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
    #------------------------------------------------------------
    print('-------------------------------------------')
    print('Enter product details below...')
    p_id = input('Product ID  : ')
    p_name = input('Product Name: ')
    price = float(input('Price (Rs)  : '))
    qty = int(input('Qty         : '))
    p_cat = input('Category    : ')
    print('Mfg Date')
    m_date = datefun()
    print('Exp Date')
    x_date = datefun()
    disc = float(input('Discount %  : '))
    print('-------------------------------------------')
    return product(p_id, p_name, price, qty, p_cat, m_date, x_date, disc)

# '''
# Product ID  :
# Product Name:
# Price (Rs)  :
# Qty         :
# Category    :
# Mfg Date    :
# Exp Date    :
# Discount %  :
# \tyear        :
# \tmonth       :
# \tday         :
# from datetime import date
# d = date(year = ,month = ,day = )
# print(d)
# date
