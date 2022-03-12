# list of strings <- like an array
friends = ["Kevin", "Karen", "Jim", "Oscar",
           "Tobyers", "Morty", "Jim", "lyxnnn"]
luckynumbers = [4, 8, 15, 16, 23, 42]
boolgemink = [True, False, True, True, False]

friends[3] = "Mamat"  # replace the value at index 3 with "Mamat"
print(f"mamank {friends[0]}")
print(f"{friends[1:]}")
# ===== list functions =====
# len()
print(len(friends))  # length of the list
# max()
print(max(friends))  # returns the largest value in the list
# min()
print(min(friends))  # returns the smallest value in the list
# sum()
print(sum(luckynumbers[1:3]))  # returns the sum of all the values in the list
# sorted()
print(sorted(friends))  # returns a sorted list
# reverse()
friends.reverse()  # reverses the order of the list
print(friends)
# sort()
boolgemink.sort()  # sorts the list
print(boolgemink)
# count()
print(friends.count("Jim")) # returns the number of times the value appears in the list
# index()
print(friends.index("Jim"))  # returns the index of the value in the list
# append()
friends.append("Asep")  # adds a value to the end of the list
print(friends)
# pop()
friends.pop()  # removes the last value in the list
print(friends)
# remove()
friends.remove("Jim")  # removes Jim from the list
print(friends)
# extend()
friends.extend(["Ucok", "Budi"])  # adds a list to the end of the list
print(friends)
# insert()
friends.insert(0, "Makoto")  # inserts a value at the specified index
print(friends)
# del()
del friends[0]  # deletes the value at the specified index
print(friends)
# clear()
friends.clear() # removes all the values in the list
print(friends)
