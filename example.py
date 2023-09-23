"""""
import jenny
jenny.greet("jenny")
"""""

import jenny
import string

x=input("enter name:")
jenny.greet('jenny')
generate_password=input("do u wish we generate a password for you? (yes/no):")

if generate_password=="yes":
    print(jenny.password_gen)
else:
    my_password=input("enter your password:")
    if my_password <= "5":
        print("password is weak")
    else:
        print("password strong")
    print(f"your password:{my_password}")

