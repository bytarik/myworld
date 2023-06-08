
'''
Dictionaries are used to store data values in key:value pairs.
- we can be referred to by using the key name
- we can change, add or remove items after the dictionary has been created.
- we can not have two items with the same key ** Duplicate keys will overwrite existing values **
- 
'''
test_dict={'c':'c'}
mytup = ('example tuple')
mytup2=('example tuple 2')
mychar = chr(97)
mychar2 = chr(98)
#example of a dictionary
dict_one = {
    #keys can be a char but we got return a string, not a char
    #values can be a char but we got return a string, not a char
    mychar : mychar2,
    #keys can be a string
    #values can be a string
    'İsim':'Tarık',
    'Yaş':'21', 
    'Yaş':'22',
    # ***Duplicate keys will overwrite existing values***
    'Cinsiyet':'Erkek',
    #keys can be an integer
    #values can be an integer
    1:11,
    #keys can be a tuple but we got the data inside the tuple as a return
    #values can be a tuple but we got the data inside the tuple as a return
    mytup:mytup2,
    #values can be a dictionary
    2:test_dict
            }
#example of empty dictionary
dict_two = {}


'''  And now we want KEYS name 
        -How we get KEYS name    '''
### Method 1 - with 'dict.keys()' method
print('<<<<<<<<<<<< Method 1 Results >>>>>>>>>>>>')
print(dict_one.keys())
# we achieved keys name of type 'dict_keys' object
print('if Dictionary is empty look like  \u2193')
print(dict_two.keys())

### Method 2 - with using together 'list()' and 'dict.keys()' methods
print('<<<<<<<<<<<< Method 2 Results >>>>>>>>>>>>')
print(list(dict_one.keys()))
# we achieved keys name of type list 
print('if Dictionary is empty look like  \u2193')
print(list(dict_two.keys()))
### Method 3 - with using for loop
print('<<<<<<<<<<<< Method 3 Results >>>>>>>>>>>>')
for x in dict_one:
    print(x)
# we achieved keys name of type in which it was first added to the dictionary
print('if Dictionary is empty look like  \u2193')
for x in dict_two:
    print(x)

### Method 4 - with Unpacking operator(*)
print('<<<<<<<<<<<< Method 4 Results >>>>>>>>>>>>')
print([*dict_one])
# we achieved keys name of type list 
print('if Dictionary is empty look like  \u2193')
print([*dict_two])

'''
if we want VALUES
'''
# Method 1 - with directly call dictionary
print(dict_one)
print(dict_two)
# we got all together 'key:values' pair as a dictionary object 

# Method 2 - with values method
print(dict_one.values())
# we achieved values of type 'dict_values' object

# Method 3 - with directly together call dictionary
print(dict_one['İsim'])
# we achieved values as a type in which it was first added to the dictionary

# Method 4 - with get method 
print(dict_one.get(1))
#whichever key we call, we only get its value as a type in which it was first added to the dictionary
'''
print(dict_two.get())
!!! we can not call get() method as empty so we can not using for empty dictionary !!!
'''

# Method 5 - with using get() method and for loop
for x in dict_one:
    print(dict_one.get(x))
for y in dict_two:
    print(y)

# Method 6 - with using values method and for loop
for x in dict_one.values():
    print(x)
for y in dict_two.values():
    print(y)