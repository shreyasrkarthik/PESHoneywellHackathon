import MySQLdb
conn = MySQLdb.connect(host= "localhost", user="root", passwd="crap", db="Honeywell")
x = conn.cursor()
try:
   x.execute("""INSERT INTO user_rmac_table VALUES (%s,%s)""",("chandler","B1:C2:D1:E1:A2:M2"))
   conn.commit()
except:
   conn.rollback()
conn.close()