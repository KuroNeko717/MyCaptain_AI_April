# Program to print positive numbers from a list
# creating an empty list 
list1 = [] 
j=0
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
    list1.append(ele) # adding the element 
    
print('Positive Numbers:')
while(j < len(list1)): 
    # checking condition 
    if list1[j] >= 0: 
        print(list1[j], end = " ") 
    # increment num  
    j+=1
