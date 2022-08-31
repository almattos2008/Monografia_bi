import self as self
from sqlalchemy import create_engine, values
import pandas as pd
import sqlalchemy
from sqlalchemy import update
from sqlalchemy import create_engine


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

    def get_stored_news_for_prediction(self):
        dbConnection = self.connect()
        frame = pd.read_sql("select headline from news where theme_prediction_roberta is null and theme_prediction_face is null limit 5000" , dbConnection)
        self.close(dbConnection)
        return frame


    def update_news(self, news, roberta, face,roberta_pt,face_pt):
        # engine = create_engine('sqlite://', echo=False)
        dbConnection = self.connect()
        sql =  "UPDATE news SET theme_prediction_roberta = \""+roberta+"\", theme_prediction_face = \""+face+"\", theme_prediction_roberta_pf = \""+roberta_pt+"\", theme_prediction_face_pt = \""+face_pt+"\" WHERE headline like \""+ news + "\""
        print(sql)
        # update("news").where("news".headline == news)
        # values(theme_prediction_roberta=roberta, theme_prediction_face=face)
        # dbConnection.
        dbConnection.execute(sql)
        self.close(dbConnection)

    def update_news_in_portuguese(self, news, roberta_pt, face_pt):
        # engine = create_engine('sqlite://', echo=False)
        dbConnection = self.connect()
        sql =  "UPDATE news SET theme_prediction_roberta_portuguese = \""+roberta_pt+"\", theme_prediction_face_portuguese = \""+face_pt+"\" WHERE headline like \""+ news + "\""
        print(sql)
        # update("news").where("news".headline == news)
        # values(theme_prediction_roberta=roberta, theme_prediction_face=face)
        # dbConnection.
        dbConnection.execute(sql)
        self.close(dbConnection)

    def get_stored_news_for_portuguese_prediction(self):
        dbConnection = self.connect()
        frame = pd.read_sql(
            "select headline from news where theme_prediction_roberta_portuguese is null and theme_prediction_face_portuguese is null limit 500",
            dbConnection)
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