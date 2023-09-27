def ft_filter(func, iterable):
    for x in iterable:
        if func(x):
            yield x


# def ft_is_even(x) :
# 	return x % 2 == 0


# def main() :

#   iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#   result = ft_filter(ft_is_even, iterable)
#   for x in result:
# 	  print(x)


# if __name__ == "__main__":
#     main()
