import matplotlib.pyplot as plt
from load_csv import load


def main():
    '''
    main function: creates the plot showing the life expectancy
    projections of the selected country
    '''
    try:
        dataframe = load('life_expectancy_years.csv')
        data_life_year = dataframe.columns[1:]
        data_life_country =\
            dataframe.loc[dataframe["country"] == "Malaysia"].iloc[0][1:]
        print(data_life_country)
        plt.plot(data_life_year, data_life_country)
        plt.xticks(["1800", "1840", "1880", "1920",
                    "1960", "2000", "2040", "2080"])
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.title('Malaysia Life expectancy Projections')
        plt.savefig("project.jpg")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
