import random
import string

def random_user_id():
    # Combine all lowercase/uppercase letters and digits (0-9)
    characters = string.ascii_letters + string.digits
    
    # Pick 6 random characters and join them together
    user_id = ''.join(random.choices(characters, k=6))
    
    return user_id

print(random_user_id())

def user_id_gen_by_user():
    # Get the length and count from the user, converting strings to integers
    num_chars = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    characters = string.ascii_letters + string.digits
    generated_ids = []

    # Loop 'num_ids' times to build each ID
    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_chars))
        generated_ids.append(user_id)
        
    # Join all IDs with a newline character so they print on separate lines
    return '\n'.join(generated_ids)

print(user_id_gen_by_user())
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

