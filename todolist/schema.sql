create table todos (
  id integer primary key not null,
  title varchar(128),
  is_complete tinyint(1)
)