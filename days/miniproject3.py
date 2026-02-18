# save the enrollment dict into
# the name , mobile , pan , 10th , 12th , gradmarks - input user will add
# 1. this input first validate all input information
# 2. after validation add into the dict and will return the roll no
# 3. save this info in a file
# 4. on the next record check if already record exist then add with new id
#
#
import os
BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)

def get_next_id(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("ID,Name,Mobile,PAN,10th,12th,Graduation\n")
            return 1

        with open(file_name, "r") as f:
            lines = f.readlines()
            if len(lines) <= 1:  
                return 1

            last_line = lines[-1]
            last_id = int(last_line.split(",")[0])
            return last_id + 1


def get_input(prompt, validate_fn):
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return None
        try:
            if validate_fn(value):
                return value
            else:
                print("Invalid input. Try again or type 'exit'.")
        except:
            print("Invalid input. Try again or type 'exit'.")


def sahil_name(x):
    return x.replace(" ", "").isalpha()


def sahil_mobile(x):
    return x.isdigit() and len(x) == 10


import re
def sahil_pan(x):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, x.upper()))

def sahil_marks(x):
    m = float(x)
    return 0 <= m <= 100


file_name = os.path.join(BASE_DIR, "student_data.txt")

while True:
    name = get_input("Enter name: ", sahil_name)
    if name is None:
        break

    mobile = get_input("Enter mobile (10 digits): ", sahil_mobile)
    if mobile is None:
        break

    pan = get_input("Enter PAN: ", sahil_pan)
    if pan is None:
        break

    marks_10 = get_input("Enter 10th marks (0-100): ", sahil_marks)
    if marks_10 is None:
        break

    marks_12 = get_input("Enter 12th marks (0-100): ", sahil_marks)
    if marks_12 is None:
        break

    graduation = get_input("Enter graduation marks (0-100): ", sahil_marks)
    if graduation is None:
        break

    record_id = get_next_id(file_name)

    with open(file_name, "a") as f:
        f.write(
            f"{record_id},{name},{mobile},{pan},{marks_10},{marks_12},{graduation}\n"
        )

        print("saved successfully!")
        