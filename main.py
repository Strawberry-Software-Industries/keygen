import random
import array

random.seed()

MAX_LEN = 5

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F']

COMBINED = DIGITS+LOWERCASE+UPPERCASE

while True:
    rand_digit1 = random.choice(DIGITS)
    rand_lower1 = random.choice(LOWERCASE)
    rand_upper1 = random.choice(UPPERCASE)

    rand_digit2 = random.choice(DIGITS)
    rand_lower2 = random.choice(LOWERCASE)
    rand_upper2 = random.choice(UPPERCASE)

    rand_digit3 = random.choice(DIGITS)
    rand_lower3 = random.choice(LOWERCASE)
    rand_upper3 = random.choice(UPPERCASE)

    temp_key1 = rand_digit1 + rand_lower1 + rand_upper1
    temp_key2 = rand_digit2 + rand_lower2 + rand_upper2
    temp_key3 = rand_digit3 + rand_lower3 + rand_upper3

    for x1 in range(MAX_LEN - 4):
        temp_key1 = temp_key1 + random.choice(COMBINED)
        temp_key_list1 = array.array('u', temp_key1)
        random.shuffle(temp_key_list1)

    for x2 in range(MAX_LEN - 4):
        temp_key2 = temp_key2 + random.choice(COMBINED)
        temp_key_list2 = array.array('u', temp_key2)
        random.shuffle(temp_key_list2)

    for x3 in range(MAX_LEN - 4):
        temp_key3 = temp_key3 + random.choice(COMBINED)
        temp_key_list3 = array.array('u', temp_key3)
        random.shuffle(temp_key_list3)

    key1 = ""
    key2 = ""
    key3 = ""

    for x1 in temp_key_list1:
        key1 = key1 + x1

    for x2 in temp_key_list2:
        key2 = key2 + x2

    for x3 in temp_key_list3:
        key3 = key3 + x3

    full_key = key1 + "-" + key2 + "-" + key3

    print(full_key, file=open("output.txt", "a"))
