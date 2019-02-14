import pymysql
import json
from main import logthis
class DatabaseManager : 
    
    hostname = "localhost"
    username = "root"
    password = "root"
    dbname = "python"
    port = "3306"
    connexion = False

    def __init__(self):
        pass

    def con(self):
        if not DatabaseManager.connexion :              
            # Open database connection
            try :
                DatabaseManager.connexion = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='och3',charset='utf8')
                print("Database. Database connected successfully ..")
            except :
                print("Database. Database not connected ..")
        return DatabaseManager.connexion

    def insertLine(self,title,image,content,datePub): 
        try:
            titleEncoded = str(str(title))
            imageEncoded = str(str(image))
            contentEncoded = str(str(content))
            datePubEncoded = str(str(datePub))
            cursor = self.con().cursor()
            cursor.execute('INSERT INTO tbl_news VALUES(null,%s,%s,%s,%s,%s,%s)',(titleEncoded,str(7),str(1),datePubEncoded,imageEncoded,contentEncoded))
            self.con().commit()
        except Exception as e:
            self.con().rollback()
            print("Database. Exception : "+str(e))
            