
import pandas as pd
import os
import env

url= f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'

query = '''SELECT * FROM logs LEFT JOIN cohorts ON cohorts.id = logs.user_id;'''



def get_cohort_and_log_data():
    filename='df0.csv'
    if os.path.isfile(filename):
         return pd.read_csv(filename)
    else: df0=pd.read_sql(query,url)
    df0.to_csv('df0.csv',index=False)