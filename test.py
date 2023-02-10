import random
import string

def generate_password(length=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for i in range(length))

x = generate_password(12)

print(x)