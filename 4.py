str_var="abcde"

rev_str_var=""
#Bring the string in a new variable without using any inbuilt functions

#Idea is to use a for loop in a reverse manner

for i in range(len(str_var)-1,-1,-1):
    rev_str_var+=str_var[i]
print(rev_str_var)