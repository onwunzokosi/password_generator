
import string
import random

password=string.ascii_letters + string.digits + string.punctuation
password_gen= ''.join(random.choice(password)for i in range(10))    #''is function in random modules

def greet(name):
    print(f"hello,I am {name}")