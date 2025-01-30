import random


def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while len(result) < 4:
        result += random.choice(characters)

    if result.lower() == result:
        print(result)
        c = random.choice(result)
        result = result.replace(c, c.upper())

    result += str(random.randint(0, 9999)).zfill(4)
    return result
