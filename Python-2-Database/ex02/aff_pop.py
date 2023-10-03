import matplotlib.pyplot as plt
from load_csv import load


def integer_converter(dataframe):
    result = []
    for i in dataframe:
        if i.endswith("M"):
            i = float(i[0:-1]) * 1000000
        elif i.endswith("k"):
            i = float(i[0:-1]) * 1000
        else:
            i = float(i)
        result.append(i)
    return result


def main():
    '''
    displays the country information of your campus versus other
    country of your choice
    '''
    try:
        dataframe = load('population_total.csv')
        data_life_year = dataframe.columns[1:252]
        data_life_country1 = dataframe.loc
        [dataframe["country"] == "Malaysia"].iloc[0][1:252]
        data_life_country2 = dataframe.loc
        [dataframe["country"] == "France"].iloc[0][1:252]
        data_life_country1 = integer_converter(data_life_country1)
        data_life_country2 = integer_converter(data_life_country2)
        plt.plot(data_life_year, data_life_country1, color="Blue")
        plt.plot(data_life_year, data_life_country2, color="Green")
        plt.legend(["Malaysia", "France"], loc='lower right')
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.xticks(["1800", "1840", "1880", "1920", "1960", "2000", "2040"])
        plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
        plt.savefig("Malaysia.jpg")
    except KeyboardInterrupt:
        pass
    except IndexError:
        print("Index error")
        exit(0)


if __name__ == "__main__":
    main()
