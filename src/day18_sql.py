#Task 1: The Insight Filter (WHERE & GROUP BY)
import pandas as pd
import sqlite3
conn = sqlite3.connect("/Users/abiamaimun/Desktop/database/internship.db")
af = pd.read_sql_query("SELECT * FROM interns WHERE stipend>5000 AND track='Data Science'",conn)
print(af)
bf = pd.read_sql_query("SELECT track,avg(stipend) FROM interns GROUP BY track",conn)
print(bf)
cf = pd.read_sql_query("SELECT track,count(id) FROM interns GROUP BY track", conn)
print(cf)


#Task 2: The Data Connector (JOINs & Python Integration)
df = pd.read_sql_query("SELECT interns.name,mentor.mentor_name FROM interns INNER JOIN mentor ON interns.track=mentor.mentor_track", conn)
print(df)


