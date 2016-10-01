import MySQLdb
conn = MySQLdb.connect(host= "localhost", user="root", passwd="crap", db="Honeywell")
cursor = conn.cursor()
u_mac = "A1:B2:C1:D2:E4:A2"#user mac
try:
	#get username
	cursor.execute("""SELECT user_name FROM umac_user_table WHERE u_mac=%s""",(u_mac))
	print cursor[0]
	for (user_name) in cursor:
		username = user_name[0]
	cursor.execute("""INSERT INTO user_rmac_table VALUES (%s,%s)""",(username,"B1:C2:D1:E1:A2:M5"))
	conn.commit()
except:
	conn.rollback()
conn.close()