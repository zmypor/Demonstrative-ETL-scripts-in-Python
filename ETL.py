import pandas as pd
from sqlalchemy import create_engine
# Extracting data
def extract_data(file_path):
    data = pd.read_csv(file_path)
    return data
# Transforming data
def transform_data(data):
    data = data.drop_duplicates()
    data = data.fillna(0)
    return data
# Loading data
def load_data(data, db_path, table_name):
    engine = create_engine(f'sqlite:///{db_path}')
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)
# ETL process main function
def etl_process(file_path, db_path, table_name):
    # Extraction
    data = extract_data(file_path)
    # Transformation
    transformed_data = transform_data(data)
    # Loading
    load_data(transformed_data, db_path, table_name)
# Calling ETL process
etl_process('data.csv', 'output.db', 'my_table')
