import matplotlib.pyplot as plt
from load_csv import load


def main():
    '''
    displays the projection of life expectancy in relation to
    the gross national product of the year 1900 for each country.
    '''
    try:
        data_life = load('life_expectancy_years.csv')
        data_gdp =\
            load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        life = data_life['1900']
        gdp = data_gdp['1900']
        plt.scatter(gdp, life)
        plt.xscale('log')
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.title("1900")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.savefig("project.jpg")
    except FileNotFoundError:
        print("File not found")
        exit(0)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
