
# string

s = "I am a string."
print("The type of  is ",type(s))   # str


# Boolean
yes = True
print("The type of yes is ",type(yes))

no = False
print("The type of no is ",type(no))


# List  -  ordered and changeable
alpha_list = ["a","b","c"]   # initialize list

print("The type of alpha_list is ",type(alpha_list))
print("The data type of alpha_list[0] is ",type(alpha_list[0]))
alpha_list.append("d")   # add d to the end of the list
print(alpha_list)


# tuple  -  ordered and unchangeable list
alpha_tuple = ("a","b","c")

print("The type of alpha_tuple is ",type(alpha_tuple))
print("The data type of alpha_tuple[0] is ",type(alpha_tuple[0]))

try:
	alpha_tuple[2] = "d"   # try to replace c with d
except TypeError:
	print("We can't change a tuple")

print(alpha_tuple)