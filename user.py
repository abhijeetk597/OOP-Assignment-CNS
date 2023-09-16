

class user:
    def __init__(self,u_name, p_word, user_id, f_name,l_name, gender, age, address, mob):
        self.u_name = u_name
        self.p_word = p_word
        self.user_id = user_id
        self.f_name = f_name
        self.l_name = l_name
        self.name = self.f_name + self.l_name
        self.gender = gender
        self.age = age
        self.address = address
        self.mob = mob

    def __str__(self):
         return f"Name : {self.name} \nUser ID : {self.user_id} \nUsername : {self.u_name} \nGender : {self.gender} \nAddress : {self.address}"

    def __repr__(self):
         return str(self)

def input_user_details():
    print('Enter new user details as below...')
    u_name = input('Username                    : ')
    p_word = input('Password                    : ')
    user_id = int(input('User ID No.                 : '))
    f_name = input('First Name                  : ')
    l_name = input('Last Name                   : ')
    while True:
        gender = int(input('Gender -> 1. Male / 2.Female: '))
        if gender == 1 or gender == 2:
            break
        print('\t\tEnter correct choice...')
    if gender == 1:
        gender = 'Male'
    else:
        gender = 'Female'
    age = int(input('Age                         : '))
    address = input('City                        : ')
    mob = input('Mobile No.                  : ')
    return user(u_name, p_word, user_id, f_name,l_name, gender, age, address, mob)


# Username                    : abhi
# Password                    : abhi123
# User ID No.                 : 1
# First Name                  : abhijeet
# Last Name                   : python
# Gender                      : 'Male'
# Age                         : 30
# City                        : kop
# Mobile No.                  : 915815