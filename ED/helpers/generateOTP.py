import random
import string

def generateOTPCode(length):
    random_string = ''
    try:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
    except Exception as e:
        print(e)
    finally:
        return random_string

