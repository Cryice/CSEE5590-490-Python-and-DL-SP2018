# Taking input from the user
list1 = input("Enter Sentence: ").split(" ")

# Function for evaluating the sentence
def give_sentence(list1):
    # Declaring empty list
    list2 = []
    #Print middle words in a sentence
    print("Middle Words of the Sentence are: "+list1[len(list1)//2], list1[(len(list1)//2)+1])

    # Printing Longest Word in the sentence
    for item in list1:
        list2.append(len(item))
    print("Longest Word in the Sentence: "+list1[list2.index(max(list2))] +" "+"("+str(max(list2)) + " letters"+ ")")
    # Printing Sentence in Reverse
    # item[::-1] to reverse the string
    # end = " " is to print side by side
    print("Reversed Sentence: ", end= " ")
    for item in list1:
        print(item[::-1],end = " ")

give_sentence(list1)