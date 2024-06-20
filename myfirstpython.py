#this program says hello and asks for my name

'''print('Hello, world!')
print("What is your name?") # asks for their name
myName = input()
print('It is good to meet you, '+ myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') # aks for their age
myAge = input()
print('You will be ' + str(int(myAge) +1)+ "in a year")'''


'''name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')'''

'''name = ''
while name != 'your name':
    print('Please type your name: ')
    name = input()
print('Thank you :)')'''

'''while True:
    print('Please type your name: ')
    name = input()
    if name == 'your name':
        break
print('Thank you')'''

'''print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')'''

total = 0
for num in range(101):
    total = total + num
print(total)
