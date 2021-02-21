#if control flow
i = 3
if i == 45:
    print(f'i is {i}')
elif i == 35:
    print(f'i is {i}')
elif i % 3 == 0:
    print('I is a multiple of 3')
else:
    print("I don't know the value of i")

#nested if control flow. inner if can only execute if the outer if is true
cat = 'Sheba'
if 's' in cat.lower():
    print("Found an 's' in cat")
    if cat.lower() == 'sheba':
        print("I found a Sheba")
    else:
        print("Some other cat")
else: print("A cat without a 's'")

'''
for loops allow you to repeat a block of statemnts
as you iterate through the sequence until the loop is broken
'''

for i in range(10):
    x = i * 2
    print(x)

'''
continue statement skips a step in a loop 
jumping to the next item in the sequence
'''

for i in range(10):
    if i == 3:
        continue
    print(i)

'''
while loops repeat a block as long as a condition is true
ex while count < 3 
or in gaming ex
while player.alive():
    player.play()
'''

count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1

#an alternate pattern is to supply a break statement
while True:
    print(f"The count is {count}")
    if count > 5:
        break
    count += 1