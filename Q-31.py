# 31) Write a Python program to count the number of strings where the string  length is 2 or more and 
# the first and last character are same from a given list of strings. 

l1 = ["harsh","mom","harsh"]
l2 = [i for i in l1 if len(i)>= 2 and i[0] == i[-1]]
print(l2)



