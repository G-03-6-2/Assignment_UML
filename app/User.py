import database

class User:

    def __init__(self, name, age, _id=None):
        self.name = name
        self.age = age
        self.user_id = _id
        self.friend = []

    def insert_user(self):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "INSERT INTO user (name, age) VALUES (%s ,%s)"
        val = (self.name, self.age)
        mycursor.execute(sql, val)
        self.user_id = mycursor.getlastrowid()
        arr = {"user_id" : mycursor.getlastrowid()}
        mydb.commit()
        mycursor.close()
        mydb.close()
        return arr
    
    def update_user(self):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "UPDATE user SET  name=%s , age=%s WHERE user_id=%s"
        val = (self.name, self.age, self.user_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Update user success"}

    @classmethod
    def get_all_user(cls):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM user"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        arr = []
        friend = []
        if len(myresult) > 0: 
            for x in myresult:
                friend = []
                sql_ = "SELECT senderId, recipient FROM friend_ship WHERE (senderId=%s OR recipient=%s)"
                val = (x[0], x[0])
                mycursor.execute(sql_, val)
                myresult_ = mycursor.fetchall()
                if len(myresult_) > 0:
                    for x_ in myresult_:
                        if x_[0] == int(x[0]):
                            friend.append(x_[1])
                        elif x_[1] == int(x[0]):
                            friend.append(x_[0])
                user = {
                    "userId" : x[0],
                    "name" : x[1],
                    "age" : int(x[2]),
                    "friend" : friend
                }
                arr.append(user)
        return arr

    def get_user(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM user WHERE userId='{}'".format(_id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        friend = []
        sql_ = "SELECT senderId, recipient FROM friend_ship WHERE (senderId=%s OR recipient=%s)"
        val = (_id, _id)
        mycursor.execute(sql_, val)
        myresult_ = mycursor.fetchall()
        if len(myresult_) > 0:
            for x in myresult_:
                if x[0] == int(_id):
                    friend.append(x[1])
                elif x[1] == int(_id):
                    friend.append(x[0])

        if len(myresult) > 0: 
            for x in myresult:
                arr = {
                    "userId" : x[0],
                    "name" : x[1],
                    "age" : int(x[2]),
                    "friend" : friend
                    }
        return arr
        
    def delete_user(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "DELETE FROM user WHERE user_id={}".format(_id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Delete user success"}
    
    def add_friend(_id, friend_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "INSERT INTO friend_ship (senderId, recipient) VALUES (%s ,%s)"
        val = (_id, friend_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Add friend success"}