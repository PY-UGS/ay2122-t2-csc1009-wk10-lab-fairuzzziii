# ========== Q2B ==========
# Function to convert number into string
# Switcher is dictionary data type here
def code_to_name(argument):
    switcher = {
        "CSC1009": "Object-Oriented Programming",
        "CSC1010": "Computer Networking",
        "CSC1008": "Data Structures & Algorithm",
    }
    return switcher.get(argument, "Invalid Course Code!")
# If argument does not match any of the dictionary values, return "invalid course code"


# Driver program
if __name__ == "__main__":
    argument = 0
    print(code_to_name("CSC1008"))

# ========== Q2C ==========
myList = []

for x in range (66, 103):  # loop through 66-102
    if x % 2 > 0:  # if x is an odd number, append to myList
        myList.append(x)

myList.sort(reverse=True)  # reverse the order of myList to be in descending order
print(myList)
