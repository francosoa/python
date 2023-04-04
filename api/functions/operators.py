import pandas as pd
import logging

def df_to_json(file, sep=';', dtype=str, delete_id=None):
    """
    This method read a csv file, convert in dataframe and after that convert in JSON File
    :param file: Path of your csv file
    :param sep: Separator of your csv
    :param dtype: Type to convert all columns
    :return: A JSON object

    """

    df = pd.read_csv(file, sep=sep, dtype=dtype)
    df = df.fillna('')

    if delete_id == True:

        for column in df.columns:
            logging.info(column)

            if column == '#':
                df.drop('#', axis=1, inplace=True)
            else:
                break

    json = df.to_json(orient='records')

    return json

