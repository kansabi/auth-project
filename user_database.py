import sqlite3

CREATE_TABLE = '''
				CREATE TABLE USERS ( 
							USERNAME TEXT,
							PASSWORD TEXT,
							EMAIL TEXT,
							TELEPHONE TEXT
							);
				'''

INSERT_ADMIN_USER = '''
					INSERT INTO USERS VALUES (
							"admin", 
							"admin_password",
							"admin@auth.project",
							"0000000000"
							)
					'''

INSERT_USER_RECORD = "INSERT INTO USER VALUES ({}, {}, {}, {})"

class UserDB():
	__instance = None

	def __init__(self):
		if UserDB.__instance != None:
			raise Exception("This is a Singleton Class")
		else:
			UserDB.__instance = self
			self.__conn = sqlite3.connect("UserDB.db")
			self.create_table()
			self.add_admin_user()

	@staticmethod
	def get_instance():
		if UserDB.__instance == None:
			UserDB()
		return UserDB.__instance

	def create_table(self):
		c = self.__conn.cursor()
		try:
			c.execute(CREATE_TABLE)
		except Exception as e:
			print("User table creation failed. %s" % e)
		finally:
			self.__conn.commit()

	def add_admin_user(self):
		c = self.__conn.cursor()
		try:
			c.execute(INSERT_ADMIN_USER)
		except Exception as e:
			print("Admin user creation failed. %s." % e)
		finally:
			self.__conn.commit()

	def add_user_record(self, user_record):
		c = self.__conn.cursor()
		expr = INSERT_USER_RECORD.format(user_record)
		print(expr)
		try:
			c.execute(expr)
		except Exception as e:
			print("Adding User Record to DB failed. %s." % e)
		finally:
			self.__conn.commit()


if __name__ == "__main__":
	db = UserDB()
	print("Check table and admin user in DB")