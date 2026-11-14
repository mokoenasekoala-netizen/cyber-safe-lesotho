import string
import math 

def has_lowercase(password):
    for character in password:
        if character in string.ascii_lowercase:
            return True
    return False

print(has_lowercase("ABC123"))
print(has_lowercase("ABc123"))
print(has_lowercase(""))

def has_uppercase(password):
    for character in password:
        if character in string.ascii_uppercase:
            return True
    return False

def has_digit(password):
    for character in password:
        if character in string.digits:
            return True
    return False

def has_symbol(password):
    for character in password:
        if character in "!@#$%^&*()-+":
            return True
    return False

print(has_uppercase("ABC123"))
print(has_uppercase("abc123"))
print(has_uppercase(""))

print(has_digit("abcDEF"))
print(has_digit("abc7"))
print(has_symbol("Abc123"))
print(has_symbol("Abc123!"))

def get_pool_size(password):
    pool = 0
    if has_lowercase(password):
        pool += 26
    if has_uppercase(password):
        pool += 26
    if has_digit(password):
        pool += 10
    if has_symbol(password):
        pool += 32
    return pool

print(get_pool_size("abc"))
print(get_pool_size("Abc"))
print(get_pool_size("Abc1"))
print(get_pool_size("Abc1!"))
print(get_pool_size(""))

def calculate_entropy(password):
    pool = get_pool_size(password)
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 1)

print(calculate_entropy("abc"))
print(calculate_entropy("Maseru2026"))
print(calculate_entropy(""))