create database news_headlines;

use news_headlines;

create table news (

news_date				date,
web_site				varchar(20),
headline				blob,
theme_prediction		varchar(50),
theme					varchar(50)

);

create table themes(

id_theme 	int(30),
theme_name	varchar(50)

)