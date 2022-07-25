from sqlalchemy import create_engine
import pandas as pd
import sqlalchemy

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/news_headlines', pool_recycle=3600)

def get_stored_news():
    dbConnection = connect()
    frame = pd.read_sql("select web_site, headline  from news", dbConnection)
    # frame = pd.read_sql("SELECT DATE_FORMAT(news_date, '%%Y-%%m-%%d') as news_date  from news", dbConnection)
    # pd.set_option('display.expand_frame_repr', False)
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

# previous_df = get_stored_news()
# totalArray = news_operations.callAllSites()
# dataframe = news_operations.toDataSet(totalArray)
# dataframe.pop('theme_prediction')
# dataframe.pop('theme')
# merged_df = news_operations.compare(dataframe, previous_df)
# dated_merged_df = merged_df.assign(news_date=date.today().strftime("%Y/%m/%d"))
# print(dated_merged_df)
# save_news(dated_merged_df)
