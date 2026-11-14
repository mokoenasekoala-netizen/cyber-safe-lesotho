import string
import math 
import getpass 

def has_lowercase(password):
    for character in password:
        if character in string.ascii_lowercase:
            return True
    return False

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

def calculate_entropy(password):
    pool = get_pool_size(password)
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 1)

COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "letmein", "admin", "welcome","iloveyou", "monkey"] 

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

print(is_common_password("password"))  # True
print(is_common_password("mypassword"))  # False

print(is_common_password("password"))    # True
print(is_common_password("PASSWORD"))    # True
print(is_common_password("Qwerty"))      # True
print(is_common_password("Kh7#mPq2!x"))  # False

LOCAL_WORDS = ["maseru", "lesotho", "basotho", "sesotho", "maputsoe", "leribe", "mafeteng", "moshoeshoe", "thaba", "mokhotlong"]

def contains_local_word(password):
    password_lower = password.lower()
    for word in LOCAL_WORDS:
        if word in password_lower:
            return True
    return False

def has_repeats(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False

sequences = ["abcdefghijklmnopqrstuvwxyz","0123456789", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
def has_sequence(password):
    lowered = password.lower()
    for seq in sequences:
        for i in range(len(seq) - 2):
            chunk = seq[i:i + 3]
            if chunk in lowered or chunk[::-1] in lowered:
                return True
    return False

def rate_entropy(score):
    if score < 28:
        return "Very Weak"
    elif score < 36:
        return "Weak"
    elif score < 60:
        return "Fair"
    elif score < 128:
        return "Strong"
    else:
        return "Very Strong"

def check_password(password):
    problems = []
    score = calculate_entropy(password)

    if contains_local_word(password):
        problems.append("This passwords contains a local word.")
        score -= 25
    if contains_local_word(password):
        problems.append("This password contains a local word.")
        score = 0
        return "Weak"
    if has_repeats(password):
        problems.append("This password contains repeated characters.")
        score = 0
    if has_sequence(password):
        problems.append("This password contains a sequence.")
        score -= 25

    return round(score, 1), rate_entropy(score), problems

def main():
    print ("=== Cyber-Safe_Lesotho: Password Checker ===")
    print ("Tip: test a password similar to your real one, not the real one. \n")

    password = getpass.getpass("Enter a password to test (hidden): ")
    score, rating, problems = check_password(password)
    print(f"Password Score: {score}")
    print(f"Password Rating: {rating}")
    if problems:
        print("Issues found:")
        for problem in problems:
            print(f" - {problem}")

    print("\n--- Results ---")
    print("Length :", len(password))
    print(f"Score : {score} bits")
    print(f"Rating : {rating}")

    if problems:
        print("\nProblems found:")
        for problem in problems:
            print(" -", problem)
    else:
        print("\nNo common weakness found.")

        if len(password) < 12:
            print("Make it at least 12 characters.")

        else:
            print("\nNO common weakness found.")

if __name__ == "__main__":

    main()

    