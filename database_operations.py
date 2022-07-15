from sqlalchemy import create_engine
import pymysql
import pandas as pd
import main_t
import sqlalchemy

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/news_headlines', pool_recycle=3600)

def get_all_news():
    dbConnection = connect()
    frame = pd.read_sql("select * from news", dbConnection)
    pd.set_option('display.expand_frame_repr', False)
    # print(frame)
    close(dbConnection)
    return frame

def save_news(dataFrame):
    dbConnection = connect()
    dataFrame.to_sql("news", dbConnection, if_exists='append', index=False, dtype={'news_date': sqlalchemy.DateTime()})
    close(dbConnection)


def connect():
    dbConnection = sqlEngine.connect()
    return dbConnection

def close(dbConnection):
    dbConnection.close()

previous_df = get_all_news()
# print(previous_df)
totalArray = main_t.callAllSites()
dataframe = main_t.toDataSet(totalArray)
# print(dataframe)
# merged_df = main_t.compare2(dataframe, previous_df)
save_news(dataframe)
