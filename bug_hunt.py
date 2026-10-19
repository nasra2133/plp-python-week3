count = 1
total = 0
#Bug: Added the missing colon to the while loop.

# BUG: Changed < 5 to <= 5 so the loop also adds 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Used a comma to print text and the number together.
print("Sum of 1 to 5 is: ", total)    