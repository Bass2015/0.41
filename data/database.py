import pandas as pd
from sqlalchemy import create_engine
from configparser import ConfigParser

def get_connection(db_info: dict=None):
    """Returns a connection to the default database if the 
    parameter db_info is None. If a dict is provided, will return
    connection to the specified database.
    """
    if db_info is None:
        db_info = get_db_info()
    connect_string = f"mysql+pymysql://{db_info['USER']}:" + \
                     f"{db_info['PASSWORD']}@{db_info['HOST']}:"+ \
                     f"{db_info['PORT']}/{db_info['DATABASE']}"  
    engine = create_engine(connect_string, echo=False)
    conn = engine.connect()
    conn.execute('commit')
    return conn

def load_tables():
    conn = get_connection()
    names = ['orders', 'products', 'centers']
    tables = []
    tables.append(pd.read_csv('../data/csvs/order.csv', dtype={'emailer_for_promotion':bool, 'homepage_featured':bool}))
    tables.append(pd.read_csv('../data/csvs/product.csv').drop('Unnamed: 0', axis=1))
    tables.append(pd.read_csv('../data/csvs/center.csv').drop('Unnamed: 0', axis=1))
    for i in range(len(names)):
        tables[i].to_sql(names[i], conn, if_exists='replace')
        conn.execute('commit')
    conn.close()
    

def get_db_info(config_file='../config.ini'):
    config = ConfigParser()
    config.read(config_file)
    return config['DATABASE']
