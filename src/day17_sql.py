#Task 1: The Database Architect (Table Creation & SELECT)
import pandas as pd
import sqlite3
conn = sqlite3.connect("/Users/abiamaimun/Desktop/database/internship.db")
df = pd.read_sql_query("SELECT name,track FROM interns", conn)
print(df)
