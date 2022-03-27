import random
import array
import sqlite3 as sql
from Cryptodome.Hash import SHAKE256
import itertools as it
counter = it.count()


random.seed()

MAX_LEN = 5

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]

COMBINED = DIGITS+LOWERCASE+UPPERCASE

# hashed_pro = sql.connect("keys_pro.db")
# raw_pro = sql.connect("keys_pro_raw.db")

# hashed_enterprise = sql.connect("keys_enterprise.db")
# raw_enterprise = sql.connect("keys_enterprise_raw.db")

hashed_developer = sql.connect("keys_developer.db")
raw_developer = sql.connect("keys_developer_raw.db")

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

    rand_digit4 = random.choice(DIGITS)
    rand_lower4 = random.choice(LOWERCASE)
    rand_upper4 = random.choice(UPPERCASE)

    temp_key1 = rand_digit1 + rand_lower1 + rand_upper1
    temp_key2 = rand_digit2 + rand_lower2 + rand_upper2
    temp_key3 = rand_digit3 + rand_lower3 + rand_upper3
    temp_key4 = rand_digit4 + rand_lower4 + rand_upper4

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
    
    for x4 in range(MAX_LEN - 4):
        temp_key4 = temp_key4 + random.choice(COMBINED)
        temp_key_list4 = array.array('u', temp_key4)
        random.shuffle(temp_key_list3)

    key1 = ""
    key2 = ""
    key3 = ""
    key4 = ""

    for x1 in temp_key_list1:
        key1 = key1 + x1

    for x2 in temp_key_list2:
        key2 = key2 + x2

    for x3 in temp_key_list3:
        key3 = key3 + x3

    for x4 in temp_key_list4:
        key4 = key4 + x4

    full_key = key1 + "-" + key2 + "-" + key3 + "-" + key4

    ByteKeys = str.encode(full_key)
    KeyHashing = SHAKE256.new()
    KeyHashing.update(ByteKeys)
    HashedKey = KeyHashing.read(26).hex()

    # Uncomment to Create new Keys

    # hashed_pro.execute(f"INSERT INTO keys (KEY) VALUES ('{HashedKey}')")
    # raw_pro.execute(f"INSERT INTO keys (KEY) VALUES ('{full_key}')")
    # hashed_pro.commit()
    # raw_pro.commit()
    
    # hashed_enterprise.execute(f"INSERT INTO keys (KEY) VALUES ('{HashedKey}')")
    # raw_enterprise.execute(f"INSERT INTO keys (KEY) VALUES ('{full_key}')")
    # hashed_enterprise.commit()
    # raw_enterprise.commit()
    
    hashed_developer.execute(f"INSERT INTO keys (KEY) VALUES ('{HashedKey}')")
    raw_developer.execute(f"INSERT INTO keys (KEY) VALUES ('{full_key}')")
    hashed_developer.commit()
    raw_developer.commit()

    print(next(counter))
