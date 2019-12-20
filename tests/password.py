import random
import string

a = random.randint(0,10)
b = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits, k=30))
print(b)