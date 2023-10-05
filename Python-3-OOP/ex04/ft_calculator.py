class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dot = 0
        for i in range(len(V1)):
            dot = dot + V1[i] * V2[i]
        print("Sum of dot is:", dot)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Sum of Vector is:",
              [float(V1[i] + V2[i]) for i in range(len(V1))])

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Substraction of Vector is:",
              [float(V1[i] - V2[i]) for i in range(len(V1))])
