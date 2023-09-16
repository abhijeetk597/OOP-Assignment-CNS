from user import user, input_user_details
from product import product_details
from implementation import Dmart


abhi = user(u_name='abhi', p_word='abhi123', user_id=1, f_name='abhijeet', l_name='python',
            gender='Male', age=30, address='kop', mob='915815')

user_list = []
user_list.append(abhi)
dservice = Dmart()


# Function related to user-----------------
def register_user():
    while True:
        print('---------------------------------------------------')
        new_user = input_user_details()
        if new_user.user_id not in [users.user_id for users in user_list]:
            user_list.append(new_user)
            print('New user successfully registered...\nProceeding to login...')
            print('---------------------------------------------------')
            return
        else:
            print('This User ID already exist. Try with different user id...')
            continue


def login():
    print("Please input your credentials...")
    u_name = input('\tEnter username: ')
    p_word = input('\tEnter password: ')
    # print(u_name, p_word, sep = '\n')
    is_login_success = False
    for user in user_list:
        if user.u_name == u_name and user.p_word == p_word:
            print('Login successful...')
            print('-------------------------------------------------')
            is_login_success = True
            break
    return is_login_success


def main_block():
    get_service = 0
    while True:
        if login():
            get_service = 1
            break
        else:
            print('...Invalid credentials...')
            z = int(input('\t\t1. Re-login\n\t\t2. Register\n\t\t3. Exit\n\tEnter your choice: '))
            if z == 1:
                continue
            elif z == 2:
                register_user()
                continue
            else:
                break
    return get_service
#---------------------------------------------------


# Service Block------------------------------------
def services():
    while True:
        print('You can enjoy below services')
        print('''        1. Add Product
        2. Delete Product
        3. Update Product
        4. Search Product(ID)
        5. Max Price Product
        6. Min Price Product
        7. Search Product In Price Range(X,Y)
        8. List Products
        9. Check discounted price of a Product
        ''')
        try:
            prch = int(input('Enter Your Choice : '))
        except:
            print('Invalid input')
            continue
        if prch == 1:
            prod = product_details()
            dservice.add_product(prod)
        elif prch == 2:
            pid = input('Enter Product Id For Delete : ')
            dservice.delete_product(pid)
        elif prch == 3:
            pid = input('Enter Product Id for Update : ')
            dservice.update_product(pid)
        elif prch == 4:
            pid = input('Enter Product Id For Search : ')
            prod = dservice.search_product(pid)
            print(prod)
        elif prch == 5:
            print("Max Price product details as below:\n", dservice.maxPriceProd())
        elif prch == 6:
            print("Min Price product details as below:\n", dservice.minPriceProd())
        elif prch == 7:
            x, y = float(input('Enter min price: ')), float(input('Enter max price: '))
            z = dservice.product_in_price_range(x, y)
            print(z)
        elif prch == 8:
            prods = dservice.list_product()
            print(prods)
        elif prch == 9:
            proid = input('Enter Product ID: ')
            print(dservice.discounted_price(proid))
        else:
            print('Enter Valid Choice : ')
            continue
        if prch in range(1, 10):
            print('-------------------------------------------------')
            a = input('Do you want to continue with the services?\n(y/n)\t:')
            print('-------------------------------------------------')
            if a in ('yes', 'y', 'Y', 'Yes', 'YES'):
                continue
            else:
                return
#--------------------------------------------------


# =========================================================================
while True:
    print('Welcome to the App...')
    while True:
        print('''---------------------------------------------
    1. Login
    2. Sign up
---------------------------------------------
        ''')
        # choice block --------------------
        while True:
            try:
                choice = int(input("Enter your choice to proceed: "))
            except:
                print('Invalid input')
                continue
            if choice == 1 or choice == 2:
                break
            else:
                print("Plase enter valid choice 1. Login / 2. Sign up")
                continue
        #-----------------------------------
        if choice == 1:
            res = main_block()
        else:
            register_user()
            res = main_block()
        if res == 1:
            services()
        break
    break
print('Exited from App. Thank you...')
# ========================================================