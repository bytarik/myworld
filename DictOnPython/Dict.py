

'''
Dictionaries are used to store data values in key:value pairs.
- we can be referred to by using the key name
- we can change, add or remove items after the dictionary has been created.
- we can not have two items with the same key ** Duplicate values will overwrite existing values **
- 
'''

myTup = ('example tuple')
char = chr(97)
#example of a dictionary
DictOne = {
    #keys can be a char but we got return a string
    char : 'b',
    #keys can be a string
    'İsim':'Tarık',
    'Yaş':'22',
    'Cinsiyet':'Erkek',
    #keys can be an integer
    1:11,
    #keys can be a tuple but we got the data inside the tuple as a return
    myTup:'aa'
            }
#example of empty dictionary
DictTwo = {}


'''  And now we want keys name 
        -How we get keys name    '''
### Method 1 - with 'dict.keys()' method
print('<<<<<<<<<<<< Method 1 Results >>>>>>>>>>>>')
print(DictOne.keys())
# we achieved keys name of type 'dict_keys' object
print('if Dictionary is empty look like  \u2193')
print(DictTwo.keys())

### Method 2 - with using together 'list()' and 'dict.keys()' methods
print('<<<<<<<<<<<< Method 2 Results >>>>>>>>>>>>')
print(list(DictOne.keys()))
# we achieved keys name of type list 
print('if Dictionary is empty look like  \u2193')
print(list(DictTwo.keys()))
### Method 3 - with using for loop
print('<<<<<<<<<<<< Method 3 Results >>>>>>>>>>>>')
for x in DictOne:
    print(x)
# we achieved keys name of type in which it was first added to the dictionary
print('if Dictionary is empty look like  \u2193')
for x in DictTwo:
    print(x)

### Method 4 - with Unpacking operator(*)
print('<<<<<<<<<<<< Method 4 Results >>>>>>>>>>>>')
print([*DictOne])
# we achieved keys name of type list 
print('if Dictionary is empty look like  \u2193')
print([*DictTwo])