def ft_statistics(*args: any, **kwargs: any) -> None:
    """"Print out statistics"""
    if len(args) == 0:
        for item in kwargs:
            print("ERROR")
        return
    for item in args:
        if isinstance(item, str):
            return
    mean = sum(args) / len(args)

    m_numbers = sorted(args)
    number_len = len(args)
    if number_len % 2 == 1:
        median = m_numbers[number_len // 2]
    else:
        middle1 = m_numbers[(number_len - 1) // 2]
        middle2 = m_numbers[(number_len + 1) // 2]
        median = (middle1 + middle2) / 2

    q_numbers = sorted(args)
    q_25 = 0.25 * (number_len)
    q_75 = 0.75 * (number_len)
    quartile = [q_numbers[int(q_25)],
                q_numbers[int(q_75)]]
    quartile = [float(num) for num in quartile]

    square_diff = [(item - mean) ** 2 for item in sorted(args)]
    var = sum(square_diff) / number_len
    std = var ** 0.5

    for item in kwargs:
        if kwargs[item] == "mean":
            print(f"mean: {mean}")
        if kwargs[item] == "median":
            print(f"median: {median}")
        if kwargs[item] == "quartile":
            print(f"quartile: {quartile}")
        if kwargs[item] == "var":
            print(f"var: {var}")
        if kwargs[item] == "std":
            print(f"std: {std}")
