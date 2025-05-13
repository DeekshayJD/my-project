#find duplicates

def find_duplicates(l):
    duplicates=[]
    for i in l:
        if l.count(i)>1 and i not in duplicates:
         duplicates.append(i)
    return duplicates

l=[1,6,5,4,3,2,3]
print(find_duplicates(l))


# find first non repating character in string

s="NETSETOSNET"
s1=[]
for i in s:
   if i not in s1 and s.count(i)<2:
      s1.append(i)
result=" ".join(s1)
print(result)
