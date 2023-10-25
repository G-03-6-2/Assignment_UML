import database

class Location:

    def __init__(self, name, _id=None):
        self.name = name
        self.locationId = _id

    def insert_location(self):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "INSERT INTO location (locationId, name) VALUES (%s, %s)"
        val = (None, self.name)
        mycursor.execute(sql,val)
        self.locationId = mycursor.getlastrowid()
        arr = {"locationId" : mycursor.getlastrowid()}
        mydb.commit()
        mycursor.close()
        mydb.close()
        return arr
        
    def update_location(self):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "UPDATE location SET  name=%s WHERE locationId=%s"
        val = (self.name, self.locationId)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Update location success"}

    @classmethod
    def get_all_location(cls):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM location"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        arr = []
        if len(myresult) > 0: 
            for result in myresult:
                location = {
                    "locationId" : result[0],
                    "name" : result[1]
                }
                arr.append(location)
        return arr

    def get_location(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM location WHERE locationId='{}'".format(_id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) > 0: 
            for result in myresult:
                arr = {
                    "locationId" : result[0],
                    "name" : result[1]
                    }
        return arr

    def delete_location(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "DELETE FROM location WHERE locationId={}".format(_id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Delete location success"}