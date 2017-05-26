create table event (event_dt date, user_id int, meal_id int, event_type varchar(50));
 .mode csv
 .import /Users/daniel/Dropbox/projects/db_to_parquet/events.csv event
 .save event
