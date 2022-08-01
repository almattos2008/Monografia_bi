import self as self
from sqlalchemy import create_engine
import pandas as pd
import sqlalchemy


class database_operations:

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

    def get_stored_specific_themed_news(self,yesterday, theme):
        dbConnection = self.connect()
        frame = pd.read_sql("select web_site, headline  from news where news_date >= '" + yesterday +"' and theme = '"+ theme +"'" , dbConnection)
        # frame = pd.read_sql("SELECT DATE_FORMAT(news_date, '%%Y-%%m-%%d') as news_date  from news", dbConnection)
        # pd.set_option('display.expand_frame_repr', False)
        # print(frame)
        self.close(dbConnection)
        return frame

    def get_stored_not_themed_news(self, yesterday, theme):
        dbConnection = self.connect()
        frame = pd.read_sql("select web_site, headline  from news where news_date >= '" + yesterday +"' and theme_prediction is not null" , dbConnection)
        # frame = pd.read_sql("SELECT DATE_FORMAT(news_date, '%%Y-%%m-%%d') as news_date  from news", dbConnection)
        # pd.set_option('display.expand_frame_repr', False)
        # print(frame)
        self.close(dbConnection)
        return frame


    def save_news(self, dataFrame):
        dbConnection = self.connect()
        dataFrame.to_sql("news", dbConnection, if_exists='append', index=False, dtype={'news_date': sqlalchemy.DateTime()})
        self.close(dbConnection)

    def save_themes(self, dataFrame):
        dbConnection = self.connect()
        dataFrame.to_sql("news", dbConnection, if_exists='append', index=False, dtype={'news_date': sqlalchemy.DateTime()})
        self.close(dbConnection)


    def connect(self):
        dbConnection = self.sqlEngine.connect()
        return dbConnection

    def close(self, dbConnection):
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


    if __name__ == "__main__":
        main()
