import sqlite3
import pandas as pd

conn = sqlite3.connect('data/slang_abusive.db')

try:
    #create table
    conn.execute("""create table slangwords (alay varchar(255), normal varchar(255));""")
    print("Table created")
except:
    #if exist, do nothing
    print("Table already exist")

#import data to dataframe
df_slang = pd.read_csv("data/new_kamusalay.csv", names = ['alay', 'normal'], encoding = 'latin-1', header = None)

#import df to db
df_slang.to_sql(name='slangwords', con=conn, if_exists = 'replace', index = False)

try:
    #create table
    conn.execute("""create table abusivewords (abusive varchar(255);""")
    print("Table created")
except:
    #if exist, do nothing
    print("Table already exist")

#import data to dataframe
df_abusive = pd.read_csv("data/abusive.csv", header = 0, encoding = 'latin-1')

#import df to db
df_abusive.to_sql(name='abusivewords', con=conn, if_exists = 'replace', index = False)
