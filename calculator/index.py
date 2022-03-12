print("Tambah = +, Kurang = -, Kali = *, Bagi = /")
first = input("Enter first number: ")
second = input("Enter second number: ")

operator = input("Enter operator: ")
if operator == "+":
    # if first and second integer
    if first.isdigit() and second.isdigit():
        print(int(first) + int(second))
    # if first and second float
    elif first.isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) + float(second))
    elif first.replace(".", "", 1).isdigit() and second.isdigit():
        print(float(first) + float(second))
    elif first.replace(".", "", 1).isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) + float(second))
    else:
        print("Invalid input")
elif operator == "-":
    if first.isdigit() and second.isdigit():
        print(int(first) - int(second))
    elif first.isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) - float(second))
    elif first.replace(".", "", 1).isdigit() and second.isdigit():
        print(float(first) - float(second))
    elif first.replace(".", "", 1).isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) - float(second))
    else:
        print("Invalid input")
elif operator == "*":
    if first.isdigit() and second.isdigit():
        print(int(first) * int(second))
    elif first.isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) * float(second))
    elif first.replace(".", "", 1).isdigit() and second.isdigit():
        print(float(first) * float(second))
    elif first.replace(".", "", 1).isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) * float(second))
    else:
        print("Invalid input")
elif operator == "/":
    if first.isdigit() and second.isdigit():
        print(int(first) / int(second))
    elif first.isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) / float(second))
    elif first.replace(".", "", 1).isdigit() and second.isdigit():
        print(float(first) / float(second))
    elif first.replace(".", "", 1).isdigit() and second.replace(".", "", 1).isdigit():
        print(float(first) / float(second))
    else:
        print("Invalid input")
else:
    print("Invalid operator")
