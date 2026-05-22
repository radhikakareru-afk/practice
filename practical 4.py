'''list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

print(have_common_member(list1, list2))'''

'''
list = [1,2,3,4,5,6,7,8,9,0]
print(list)
list.pop(5)
list.pop(4)
list.pop(2)
list.pop(0)
print(list)'''

'''
original_list = [2,4,6,8]
copylist1 = original_list[:] #slicing 
Copylist2 = list(original_list) #list constructor
copylist3 = original_list.copy() #copy method
print("original list: ",original_list)
print("slicing: ",copylist1)
print("list constructor: ",Copylist2)
print("copy method: ",copylist3)'''

'''a = [1,1,2,3,5,8,13,21,34,55,89]
for num in a:
    if num < 5:
        print(num)'''

def check_duplicate(Lst):
    list = set()
    for item in Lst:
        if item in list:
            return True
        list.add(item)
    return False
print(check_duplicate([1,2,3,4]))

    
