ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list
ft_list[1] = "World!"

# tuple
y = list(ft_tuple)
y[1] = "Malaysia!"
ft_tuple = tuple(y)

# set
ft_set |= {"Kuala Lumpur!"}
ft_set -= {"tutu!"}

# # dict
ft_dict["Hello"] = "42 Kuala Lumpur!"

# other dict
# ft_dict.update({"Hello": "42 Kuala Lumpur!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
