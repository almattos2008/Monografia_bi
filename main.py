import openpyxl as openpyxl
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import date
# from google.colab import files
import mysql.connector
from mysql.connector import Error
import os.path

import database_connection

connection = mysql.connector.connect(host='localhost',
                                         database='news_headlines',
                                         user='root',
                                         password='')

print(pd.read_sql("SELECT * FROM news", connection))