import re
import pandas as pd
import sqlite3
def clean_slang_abusive(text):
    conn = sqlite3.connect('data/slang_abusive.db')
    df_slang = pd.read_sql('''SELECT * FROM slangwords''', conn)
    df_abusive = pd.read_sql('''SELECT * FROM abusivewords''', conn)
    conn.close()
    
    #create dictionary format {slangword(key):realword(value)}, e.g {3x:tiga kali, aamiin:amin}
    Slang_dict = dict(zip(df_slang['alay'], df_slang['normal'])) 
    Abusive_list = list(df_abusive['ABUSIVE'])
    #create empty array
    holder = [] 
    
    for word in text.split(' '):
        #check if input word exist in dictionary key
        if word in Slang_dict.keys():
            #if exist, convert with realworld
            word = Slang_dict[word]
            if word in Abusive_list:
                #if exist delete
                word=''
            holder.append(word)
        else :
            if word in Abusive_list:
                #if exist delete
                word=''
            #if not, fill the empty array
            holder.append(word)

    return ' '.join(holder) #string converted slang words with real words

def clean_to_alphanumeric(text):
    return re.sub(r'\\[x][a-zA-z0-9]{2}|\\[x][a-zA-z0-9]{1}|\\n|[^a-zA-Z0-9]', ' ',text).lower()

def clean_everything(text):
    return " ".join(clean_slang_abusive(clean_to_alphanumeric(text)).split())



