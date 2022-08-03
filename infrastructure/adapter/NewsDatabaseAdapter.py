import self as self
from sqlalchemy import create_engine
import pandas as pd
import sqlalchemy


class NewsDatabaseAdapter:

    def __init__(self):
        self.sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/news_headlines', pool_recycle=3600)

    def get_stored_news(self, yesterday):
        dbConnection = self.connect()
        frame = pd.read_sql("select web_site, headline  from news where news_date >= '" + yesterday +"'" , dbConnection)
        # frame = pd.read_sql("SELECT DATE_FORMAT(news_date, '%%Y-%%m-%%d') as news_date  from news", dbConnection)
        # pd.set_option('display.expand_frame_repr', False)
        # print(frame)
        self.close(dbConnection)
        return frame

    def save_news(self, dataFrame):
        dbConnection = self.connect()
        dataFrame.to_sql("news", dbConnection, if_exists='append', index=False, dtype={'news_date': sqlalchemy.DateTime()})
        self.close(dbConnection)

    def connect(self):
        dbConnection = self.sqlEngine.connect()
        return dbConnection

    def close(self, dbConnection):
        dbConnection.close()