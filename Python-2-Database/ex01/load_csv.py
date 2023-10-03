import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    Load csv file and return Dataset object.
    '''
    try:
        assert isinstance(path, str), "This path is not a string"
        data = pd.read_csv(path)
        return data
    except AssertionError as msg:
        print("Assertion Error:", msg)
        exit(0)
    except FileNotFoundError:
        print("File not found")
        exit(0)
