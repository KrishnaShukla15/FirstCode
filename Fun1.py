#Program to convert tuple to list and again to tuple
#Creating Tuple 
tup1=(1,2,3,4,5)
List1=list(tup1)
List1.append(6)
tup1=tuple(List1)
print('Your tuple is :',tup1)

