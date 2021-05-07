from flask import Flask, request
from user import User

# Create Flask app
app = Flask(__name__)

# API endpoint to home.
@app.route('/')
@app.route('/home')
def home():
	return "<h1>WELCOME TO AUTH PROJECT<h1>"

# API endpoint to list users.
@app.route('/users/list')
def users():
	users = User()
	return users.users

# API endpoint to create a user record.
@app.route('/users', methods = ['POST'])
def implement_create_users():
	users = User()
	if request.method == 'POST':
		data = request.json
		try:
			users.create_user(data)
		except Exception as e:
			print("User create failed. %s" %e)
		print(data)
	return "User created successfully"

# API endpoint to modify a user record.
@app.route('/users', methods = ['PUT'])
def implement_modify_users():
	users = User()
	return "User record is modified"

# API endpoint to delete a user record.
@app.route('/users', methods = ['DELETE'])
def implement_delete_users():
	users = User()
	return "User record is deleted"

if __name__ == "__main__":
	app.run(debug=True)
