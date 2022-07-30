create database news_headlines;

use news_headlines;

create table news (

news_date				    date,
web_site				    varchar(20),
headline				    text,
theme_prediction_face       varchar(50),
theme_prediction_roberta    varchar(50),
theme					    varchar(50)

);

create table themes(

id_theme 	int(30),
theme_name	varchar(50)

)