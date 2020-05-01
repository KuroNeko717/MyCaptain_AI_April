# Program to Assign Elements to Different Lists
list1 = [1,2,3,4,5,6,7] 
list2 = [2,4,6,8,10,12]
# Program to Assign Elements From a Tuple
T1=(10,20,30,40,50,60,70)
element=T1[2]
print(element)
# Program to Delete different Dictionary Element
dictionary1 = {
  "Username": "KuroNeko717",
  "Email": "kuroneko717@gmail.com",
  "Password": "abc", 
  "Age": 20,
}
print(dictionary1)
''' 
Deleting an entry from dictionary using del 
It’s necessary to check if key is present in dictionary before deletion otherwise del with throw keyError.
'''
# If key exist in dictionary then delete it using del.
if "Age" in dictionary1:
    del dictionary1["Age"]
'''
OR
try:
    del wordFreqDic["testing"]
except KeyError:
    print("Key 'testing' not found")

OR
result = Dictionary1.pop("Age", None)    
 
print("Deleted item's value = ", result)
print("Updated Dictionary :" , dictionary1)  
'''
print(dictionary1)