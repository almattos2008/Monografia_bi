import news_operations
import database_operations
from datetime import date
import identification

previous_df = database_operations.get_stored_news()
totalArray = news_operations.callAllSites()
dataframe = news_operations.toDataSet(totalArray)
merged_df = news_operations.compare(dataframe, previous_df)
print(str(len('Diferenças: ' + merged_df)))
merged_df = merged_df.assign(theme_prediction='')
for row in merged_df.index:
    theme = identification.identifify(merged_df['headline'][row])
    if theme == 0:
        merged_df.drop(row)
    else:
        merged_df['theme_prediction'][row] = theme
    # print(merged_df['headline'][row]+' - '+theme)
dated_merged_df = merged_df.assign(news_date=date.today().strftime("%Y/%m/%d"))

print(dated_merged_df)
database_operations.save_news(dated_merged_df)
