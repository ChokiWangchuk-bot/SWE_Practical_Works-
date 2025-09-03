#Array Manipulation
#Question 1
first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []
index = len(first_list) - 1  
while index >= 0:
    value = first_list.pop()
    inverse_list.append(value)
    index -= 1
print(inverse_list)

#Question 2
#Implementing functions
def reverse_array(first_list):
    inverse_list = []
    index = len(first_list) - 1

    while index >= 0:
        value = first_list.pop()
        inverse_list.append(value)
        index -= 1

    return inverse_list


first_list = [0,1,2,3,4,5,6,7,8,9]
print(reverse_array(first_list))   


