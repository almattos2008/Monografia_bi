import news_operations
import database_operations
from datetime import date


previous_df = database_operations.get_stored_news()
totalArray = news_operations.callAllSites()
dataframe = news_operations.toDataSet(totalArray)
dataframe.pop('theme_prediction')
dataframe.pop('theme')
merged_df = news_operations.compare(dataframe, previous_df)
dated_merged_df = merged_df.assign(news_date=date.today().strftime("%Y/%m/%d"))

print(dated_merged_df)
database_operations.save_news(dated_merged_df)
