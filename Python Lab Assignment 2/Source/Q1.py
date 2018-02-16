# Initialised a dictionary with below data
dict = {"c":20,"web":30,"python":50,"java":40,"scala":50, "c++":60}

# Taking inputs from the user to get the range
r1 = int(input("Enter range 1: "))
r2 = int(input("Enter range 2: "))

# for loop to print the items that are in the range given by the user
for i in dict.keys():
# Checking for range of values whether they are between ranges given by the user
    if dict[i]>=r1 and dict[i]<=r2:
#Printing the data
        print(i)
