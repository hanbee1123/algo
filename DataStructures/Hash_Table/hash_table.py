#dictionaries are same as hash tables.
#Internally, a hash function is used which puts the keys, values into a specific index.

"""HASH TABLE에서는 IN 연산자를 사용하는게 핵심"""

# if 'music' in score
 # when checking keys in dictionaries, it is done in Random Access

#  .clear()	  remove all elements in dictionary
# .copy()	      Returns a copy of the dictionary
# .fromkeys()	  Returns a dictionary with the specified keys and values
# .get()	      Return the value of the specified key
# .items()	  Returns a list containing a tuple for each key value pair
# .keys()	      Returns a list containing the dictionary's key
# .pop()	      removes the element with the specified key
# .popitem()	   Removes the last inserted key-value pair
# .setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# .update()	   Update the dictionary with the specified key-value pairs
# .values()	   Returns a list of all the values in the dictionary
# |	
# a = {1: 'a', 2: 'b', 3: 'c'}
# b = {4: 'd', 5: 'e'}
# c = a|b
# print(c)
# OUT: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


# |=	a = {1: 'a', 2: 'b', 3: 'c'}
# b = {4: 'd', 5: 'e'}
# a|=b
# print(a)
# OUT: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}