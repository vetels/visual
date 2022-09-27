
from multiprocessing.resource_sharer import stop


s = 'aaaabbcaa'

letters = []
letter = []
count = 1

for i in s:
    if i == s[count]:
        print(i)
        count += 1
#
    elif i != s[count]:
        print(s[count - 1])
        #letter_2 = letter.append(i)
        break
    #print(letters)
       
 

    
