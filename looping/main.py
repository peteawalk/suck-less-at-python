count = 0
while count < 3:
    print(f"The count is {count}")
    count +=1
'''
The count is 0
The count is 1
The count is 2
'''

for i in range(6):
    if i ==3:
        continue
    print(i)
'''
0
1
2
4
5
'''

# Use break and/or conditionals to prevent a forever loop:
count = 0
while True:
    print(f"the count is {count}")
    if count > 5:
        break
    count += 1

'''
the count is 0
the count is 1
the count is 2
the count is 3
the count is 4
the count is 5
the count is 6
'''