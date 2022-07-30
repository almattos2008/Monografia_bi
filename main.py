import news_operations
import database_operations
from datetime import date, timedelta
import identification
import themed_news_operations

# Get generic news and store
def populate_generic_themed_database():
    yesterday = date.today() - timedelta(days=1)
    previous_df = database_operations.get_stored_news(yesterday.strftime("%Y/%m/%d"))
    totalArray = news_operations.callAllSites()
    dataframe = news_operations.toDataSet(totalArray)
    merged_df = news_operations.compare(dataframe, previous_df)
    # merged_df = merged_df.assign(theme_prediction='')
    # for row in merged_df.index:
    #     theme = identification.identifify(merged_df['headline'][row])
    #     if theme == 0:
    #         merged_df.drop(row)
    #         print("Dropped")
    #     else:
    #         merged_df['theme_prediction'][row] = theme
    #         print("Save")
    #     # print(merged_df['headline'][row]+' - '+theme)
    merged_df = merged_df.assign(news_date=date.today().strftime("%Y/%m/%d"))
    print('Diferenças: ' + str(len(merged_df)))
    print(merged_df)
    database_operations.save_news(merged_df)

# Get specific news and store
def populate_specific_themed_database(theme):
    yesterday = date.today() - timedelta(days=1)
    previous_df = database_operations.get_stored_news(yesterday.strftime("%Y/%m/%d"))
    totalArray = themed_news_operations.call_themed_sites()
    dataframe = themed_news_operations.toDataSet(totalArray)
    merged_df = themed_news_operations.compare(dataframe, previous_df)
    merged_df = merged_df.assign(news_date=date.today().strftime("%Y/%m/%d"))
    merged_df = merged_df.assign(theme=theme)
    print('Diferenças: ' + str(len(merged_df)))
    print(merged_df)
    database_operations.save_news(merged_df)

# Guess not predicted news
def guess_theme():
    yesterday = date.today() - timedelta(days=1)
    previous_df = database_operations.get_stored_news(yesterday.strftime("%Y/%m/%d"))
    merged_df = previous_df.assign(theme_prediction_face='')
    merged_df = previous_df.assign(theme_prediction_roberta='')
    for row in merged_df.index:
        theme = identification.identifify_facebook_model(merged_df['headline'][row])
        if theme == 0:
            merged_df.drop(row)
            print("Dropped")
        else:
            merged_df['theme_prediction_face'][row] = theme
            print("Save")

        theme = identification.identifify_xlm_roberta_large_model(merged_df['headline'][row])
        if theme == 0:
            merged_df.drop(row)
            print("Dropped")
        else:
            merged_df['theme_prediction_roberta'][row] = theme
            print("Save")


populate_specific_themed_database("economia")
populate_generic_themed_database()
