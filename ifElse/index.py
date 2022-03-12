import datetime 


today = datetime.datetime.now()
print(f"{today.hour}:{today.minute}:{today.second}")
if today.hour < 12:  # if statement
    print("Good Morning")
elif today.hour < 18:  # elif statement
    print("Good Afternoon")
else:              # else statement
    print("Good Evening")

# ======== comparison operators ========
# ==, !=, >, <, >=, <=
# == is equal to
# != is not equal to
# > is greater than
# < is less than
# >= is greater than or equal to
# <= is less than or equal to

# ======== and, or, not ========
# and is logical and
# or is logical or
# not is logical not
