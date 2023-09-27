def ft_tqdm(lst: range) -> None:
    '''
    This function is a clone of tqdm.
    '''
    percentage = 0
    for n in range(len(lst) + 1):
        spaces = int(n / len(lst) * 127)
        loading = ("█" * spaces + (" " * (127 - spaces)))
        if n / len(lst) * 100 >= percentage:
            print(f"{percentage}%|{loading}", end="")
            print(f"| {n + 1 - 1}/{len(lst)}", end="\r")
            percentage += 1
        yield n
