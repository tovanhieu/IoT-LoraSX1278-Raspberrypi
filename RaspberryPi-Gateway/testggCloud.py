import mysql.connector
mydb = mysql.connector.connect(
  host="35.220.202.217",
  user="root",
  passwd="1234",
  database="project_loraweb"
)
temp = 27
cabin_id = 8 
humi = 89
def insertGgClouddb(tem, cabinID, hum):
    mycursor = mydb.cursor()
    sql = "INSERT INTO tbl_cabin (temp, cabin_id, humi) VALUES (%s,%s,%s)"
    val = [ (tem, cabin_id, hum) ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
insertGgClouddb(temp, cabin_id, humi)