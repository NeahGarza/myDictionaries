phonebook = {'Chris':'555-111',
            'Katie':'555-2222',
            'Joanne':'555-3333'}
"""

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)

print(len(phonebook))

mydictionary = dict(m=8,n=9)

print(mydictionary)



print()
print('*****  end section 1 ********')
print()






print()
print('*****  start section 2 - search dictionary ********')
print()


#phone = phonebook['Chris']
#print(phone)
#print(phonebook['Chris'])

name = 'Chris'
if name in phonebook:
    print(phonebook[name])
else:
    print("Not found")


print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()


phonebook['Chris'] = '555-4444'
phonebook['Joe'] = '555-0123'
print(phonebook)


print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook["Chris"]
print(phonebook)


print()
print('*****  end section 4 ********')
print()





print()
print('*****  start section 5 - iterate through keys ********')
print()

for key in phonebook:
    print(key)
    print(phonebook[key])

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - iterate through values  ********')
print()

for value in phonebook.values():
    print(value)


print()
print('*****  end section 6 ********')
print()


"""




print()
print('*****  start section 7 - iterate through both key and value pair********')
print()


for key,value in phonebook.items():
    print(key, value)


print()
print('*****  end section 7 ********')
print()


"""





print()
print('*****  start section 8 - using random and converting to list ********')
print()




print()
print('*****  end section 8 ********')
print()



"""




