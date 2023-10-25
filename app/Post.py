import database

class Post:

    def __init__(self, time, content, createBy, locationTag, friendTag, _id=None):
        self.time = time
        self.content = content
        self.createBy = createBy
        self.locationTag = locationTag
        self.friendTag = friendTag
        self.postId = _id

    def insert_post(self):
        txt = ""
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        if len(self.friendTag) > 0:
            for friend in self.friendTag:
                sql_ = "SELECT senderId, recipient FROM friend_ship WHERE (senderId=%s AND recipient=%s) OR (senderId=%s AND recipient=%s)"
                val = (self.createBy, friend, self.createBy, friend)
                mycursor.execute(sql_, val)
                myresult_ = mycursor.fetchall()
                if len(myresult_) == 0:
                    txt += "User ID {} are not your friend. ".format(friend)
        if txt != "":
            return {"error" : txt}
        sql = "INSERT INTO post (time, content, createBy, locationTag) VALUES (%s, %s, %s, %s)"
        val = (self.time, self.content, self.createBy, self.locationTag)
        mycursor.execute(sql, val)
        self.postId = mycursor.getlastrowid()
        arr = {"postId" : mycursor.getlastrowid()}
        for friend in self.friendTag:
            sql = "INSERT INTO post_tags (postId, tagged_userId) VALUES (%s, %s)"
            val = (self.postId, friend)
            mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return arr
    
    def update_post(self):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "UPDATE user SET  time=%s , content=%s , createBy=%s , locationTag=%s , friendTag=%s WHERE user_id=%s"
        val = (self.time, self.content, self.createBy, self.locationTag, self.friendTag, self.postId)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Update post success"}

    @classmethod
    def view_all_post(cls):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM post;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        arr = []
        if len(myresult) > 0: 
            for result in myresult:
                friendTag = []
                sql_ = "SELECT tagged_userId FROM post_tags WHERE postId={}".format(result[0])
                mycursor.execute(sql_)
                myresult_ = mycursor.fetchall()
                if len(myresult_) > 0:
                    for x_ in myresult_:
                        friendTag.append(x_[0])
                post = {
                    "postId" : result[0],
                    "content" : result[1],
                    "createBy" : result[2],
                    "locationTag" : result[3],
                    "time" : result[5],
                    "friendTag" : friendTag
                }
                arr.append(post)
        else:
            arr = {"error" : "Post not found."}
        mydb.commit()
        mycursor.close()
        mydb.close()
        return arr
    
    def view_post_by_user(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM post WHERE createBy={}".format(_id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        arr = []
        if len(myresult) > 0: 
            for result in myresult:
                friendTag = []
                sql_ = "SELECT tagged_userId FROM post_tags WHERE postId={}".format(result[0])
                mycursor.execute(sql_)
                myresult_ = mycursor.fetchall()
                if len(myresult_) > 0:
                    for x_ in myresult_:
                        friendTag.append(x_[0])
                post = {
                    "postId" : result[0],
                    "content" : result[1],
                    "createBy" : result[2],
                    "locationTag" : result[3],
                    "time" : result[5],
                    "friendTag" : friendTag
                }
                arr.append(post)
        else:
            arr = {"error" : "Post not found."}
        mydb.commit()
        mycursor.close()
        mydb.close()
        return arr
    
    def view_post_by_locationTag(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM post WHERE locationTag={}".format(_id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        arr = []
        if len(myresult) > 0: 
            for result in myresult:
                friendTag = []
                sql_ = "SELECT tagged_userId FROM post_tags WHERE postId={}".format(result[0])
                mycursor.execute(sql_)
                myresult_ = mycursor.fetchall()
                if len(myresult_) > 0:
                    for x_ in myresult_:
                        friendTag.append(x_[0])
                post = {
                    "postId" : result[0],
                    "content" : result[1],
                    "createBy" : result[2],
                    "locationTag" : result[3],
                    "time" : result[5],
                    "friendTag" : friendTag
                }
                arr.append(post)
        else:
            arr = {"error" : "Post not found."}
        mydb.commit()
        mycursor.close()
        mydb.close()
        return arr
    
    def get_post(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM post WHERE postId='{}'".format(_id)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) > 0: 
            for result in myresult:
                arr = {
                    "postId" : result[0],
                    "time" : result[1],
                    "content" : result[2],
                    "createBy" : result[3],
                    "locationTag" : result[4],
                    "friendTag" : result[5]
                }
        return arr

    def delete_post(_id):
        mydb = database.connectorMysql()
        mycursor = mydb.cursor()
        sql = "DELETE FROM post WHERE postId={}".format(_id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return {'message' : "Delete post success"}
