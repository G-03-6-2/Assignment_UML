from flask import Flask , request , jsonify
from User import User
from Location import Location
from Post import Post
import time
from datetime import datetime  

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello This is Index!"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)


@app.route('/calculate/<num1>/<num2>', methods=['GET'])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = {
                'plus' : num1 + num2,
                'minus' : num1 - num2,
                'multiply': num1 * num2,
                'divide' : num1/num2
            }
    except:
        results = { 'error_msg' : 'inputs must be numbers' }

    return jsonify(results)

#####################################################################################

# a GET request to /user/ returns a list of registered users on a system
@app.route('/user/' , methods=['GET'])
def get_all_user():
    return jsonify(User.get_all_user())

# a POST request to /user/new creates a user with the using the body data. The response returns the ID.
@app.route('/user/new' , methods=['POST'])
def insert_user():
    request_data = request.get_json()
    new_user = User(request_data['name'], request_data['age'])
    return jsonify(new_user.insert_user())

# a PUT request to /user/123 updates user 123 with the body data
@app.route('/user/<_id>' , methods=['PUT'])
def update_user(_id):
    request_data = request.get_json()
    new_user = User(request_data['name'], request_data['age'], _id)
    return jsonify(new_user.update_user())

# a GET request to /user/123 returns the details of user 123
@app.route('/user/<_id>' , methods=['GET'])
def find_user(_id):
    return jsonify(User.get_user(_id))

# a DELETE request to /user/123 deletes user 123
@app.route('/user/<_id>' , methods=['DELETE'])
def delete_user(_id):
    return jsonify(User.delete_user(_id))

@app.route('/add_friend' , methods=['POST'])
def add_friend():
    request_data = request.get_json()
    return jsonify(User.add_friend(request_data["userId"], request_data["friendId"]))


#####################################################################################

# a GET request to /location/ returns a list of registered location on a system
@app.route('/location/' , methods=['GET'])
def get_all_location():
    return jsonify(Location.get_all_location())

# a POST request to /location/new creates a location with the using the body data. The response returns the ID.
@app.route('/location/new' , methods=['POST'])
def insert_location():
    request_data = request.get_json()
    new_location = Location(request_data['name'])
    return jsonify(new_location.insert_location())

# a PUT request to /location/123 updates location 123 with the body data
@app.route('/location/<_id>' , methods=['PUT'])
def update_location(_id):
    request_data = request.get_json()
    new_location = Location(request_data['name'], _id)
    return jsonify(new_location.update_location())

# a GET request to /location/123 returns the details of location 123
@app.route('/location/<_id>' , methods=['GET'])
def find_location(_id):
    return jsonify(Location.get_location(_id))

# a DELETE request to /location/123 deletes location 123
@app.route('/location/<_id>' , methods=['DELETE'])
def delete_location(_id):
    return jsonify(Location.delete_location(_id))

#####################################################################################

# /post (with json input and save into DB)
@app.route('/post', methods=['POST'])
def post():
    request_data = request.get_json()
    date_time = datetime.fromtimestamp(time.time())
    new_post = Post(date_time, request_data['content'], request_data['create_by'], request_data['location'], request_data['friend'])
    return jsonify(new_post.insert_post())

# /view (return all posts)
@app.route('/view', methods=['GET'])
def view():
    return jsonify(Post.view_all_post())

# /view/user/{user_id} (return all posts from a user_id)
@app.route('/view/user/<user_id>', methods=['GET'])
def view_post_user(user_id):
    return jsonify(Post.view_post_by_user(user_id))

# /view/location/{location_id} (return all posts from a location_id)
@app.route('/view/location/<location_id>', methods=['GET'])
def view_location(location_id):
    return jsonify(Post.view_post_by_locationTag(location_id))

# a PUT request to /post/123 updates post 123 with the body data
@app.route('/post/<_id>' , methods=['PUT'])
def update_post(_id):
    request_data = request.get_json()
    new_post = Post(request_data['title'], request_data['content'], request_data['create_by'], request_data['location'], request_data['friend'], _id)
    return jsonify(new_post.update_post())

# a GET request to /post/123 returns the details of post 123
@app.route('/post/<_id>' , methods=['GET'])
def find_post(_id):
    return jsonify(Post.get_post(_id))

# a DELETE request to /post/123 deletes post 123
@app.route('/post/<_id>' , methods=['DELETE'])
def delete_post(_id):
    return jsonify(Post.delete_post(_id))

#####################################################################################

if __name__ == '__main__':
    app.run()