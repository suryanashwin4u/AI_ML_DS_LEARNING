# interpolation search using function
# uniformaly distributed and sorted array needed
# position formula-->position=lower_index+[{key-mylist(lower_index)}*{(higher_index-lower_index)}]/(mylist[higher_index]-mylist[lower_index])

def interpolation_search(mylist,list_length,key):
    lower_index=0
    higher_index=list_length-1
    while lower_index<=higher_index and key>=mylist[lower_index] and key<=mylist[higher_index]:
        if lower_index==higher_index:
            if mylist[lower_index]==key:
                return lower_index
            return -1
        
        position=lower_index+[((key-mylist[lower_index])*(higher_index-lower_index))//(mylist[higher_index]-mylist[lower_index])]
        
        if mylist[position]==key:
            return position
        elif mylist[position]<key:
            lower_index=position+1
        elif mylist[position]>key:
            higher_index=position-1
    return -1



mylist=input("enter the sorted and uniformaly distributed list of numbers:").split(",")
print(f"list input:{mylist}")

key=input("enter the searching element:")
print(f"key entered is:{key}")

list_length=len(mylist)
print(f"length of the list:{list_length}")

index=interpolation_search(mylist,list_length,key)

if index==-1:
    print("element not found")
else:
    print(f"element is found at {index+1}")
