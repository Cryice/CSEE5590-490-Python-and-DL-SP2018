# Created a list of dictionaries
contact_list = [{"name":'sarat', "number":99897, "email":"srt@gmail.com"},{"name":"tim", "number":767657657, "email":"tim@gmail.com"},{"name":"mike","number":8745126,"email":"mike@gmail.com"}]
# Asking input from user to enter name to get contact
nm = input("Enter name to get contact: ")
# Iterating over contact_list
for i in contact_list:
# if condition for checking the name entered by the user is in the dictionary or not
    if nm in i.values():
# if true printing the contact
        print(i)
# Asking input from the user to enter number to get contact
num = int(input("Enter number to get contact: "))
# Iterating over contact_list
for j in contact_list:
# If condition for checking whether the entered number is in dictinary or not
    if num in j.values():
# Prnting the contact if condition is true
        print(j)
# Asking user to enter the name
nme = input("Enter name to get contact and edit number: ")
# Iterating over the contact_list
for k in contact_list:
# If the entered name in dictionary
    if nme in k.values():
# Prnting the contact
        print(k)
# Asking user if he want to edit the number
        newnum = int(input("Enter number to edit: "))
# Editing the nimber for the particular user
        k["number"] = newnum
# Printing the contact
        print(k)
# Exit condition
s = input()
if(s=='exit'):
    exit()
