#find duplicates

def find_duplicates(l):
    duplicates=[]
    for i in l:
        if l.count(i)>1 and i not in duplicates:
         duplicates.append(i)
    return duplicates

l=[1,6,5,4,3,2,3]
print(find_duplicates(l))
