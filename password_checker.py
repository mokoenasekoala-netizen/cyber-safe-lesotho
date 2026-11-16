import math
import string
from getpass import getpass

COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123",
                    "letmein", "admin", "welcome", "iloveyou", "monkey"]

LOCAL_WORDS = ["maseru", "lesotho", "basotho", "sesotho", "maputsoe",
               "leribe", "mafeteng", "moshoeshoe", "thaba", "mokhotlong"]

SEQUENCES = ["abcdefghijklmnopqrstuvwxyz", "0123456789",
             "qwertyuiop", "asdfghjkl", "zxcvbnm"]

GUESSES_PER_SECOND = 10_000_000_000


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
        if character in string.punctuation:
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


def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def contains_local_word(password):
    lowered = password.lower()
    for word in LOCAL_WORDS:
        if word in lowered:
            return True
    return False


def has_repeats(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False


def has_sequence(password):
    lowered = password.lower()
    for seq in SEQUENCES:
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
    elif score < 80:
        return "Strong"
    else:
        return "Very Strong"


def check_password(password):
    problems = []
    score = calculate_entropy(password)

    if is_common_password(password):
        problems.append("This is one of the most common passwords.")
        score = 0
    if contains_local_word(password):
        problems.append("This password contains a local word.")
        score -= 25
    if has_repeats(password):
        problems.append("This password contains repeated characters.")
        score -= 25
    if has_sequence(password):
        problems.append("This password contains a sequence.")
        score -= 25

    if score < 0:
        score = 0
    return round(score, 1), rate_entropy(score), problems


def format_time(seconds):
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day

    if seconds < 1:
        return "less than a second"
    elif seconds < minute:
        return f"{int(seconds)} seconds"
    elif seconds < hour:
        return f"{int(seconds / minute)} minutes"
    elif seconds < day:
        return f"{int(seconds / hour)} hours"
    elif seconds < year:
        return f"{int(seconds / day)} days"
    elif seconds < 1000 * year:
        return f"{int(seconds / year)} years"
    else:
        return "more than 1,000 years"


def estimate_crack_time(score):
    if score >= 100:
        return "more than 1,000 years"
    seconds = 2 ** score / GUESSES_PER_SECOND
    return format_time(seconds)


def main():
    print("=== Cyber-Safe Lesotho: Password Checker ===")
    print("Tip: test a password similar to your real one, not the real one.\n")

    password = getpass("Enter a password to test (hidden): ")
    score, rating, problems = check_password(password)

    print("\n--- Results ---")
    print("Length     :", len(password))
    print("Score      :", score, "bits")
    print("Rating     :", rating)
    print("Crack time :", estimate_crack_time(score))

    if problems:
        print("\nProblems found:")
        for problem in problems:
            print(" -", problem)
    else:
        print("\nNo common weaknesses found.")

    if len(password) < 12:
        print(" - Make it at least 12 characters.")


if __name__ == "__main__":
    main()