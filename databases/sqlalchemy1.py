from sqlalchemy import MetaData
metadata_obj = MetaData()
from sqlalchemy import Table, Column, Integer, String
user_table = Table(
	"user_account",
	metadata_obj,
	Column("id", Integer, primary_key=True),
	Column("name", String(30)),
	Column("fullname", String))
	
print(user_table.c.name)
print(user_table.c.keys())
print(user_table.primary_key)

