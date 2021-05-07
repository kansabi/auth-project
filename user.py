from user_database import UserDB

class User():
    def __init__(self):
        # Create admin user
        self.db = UserDB.get_instance()

    def create_user(self, data):
        user_record = (data.get('username'),
                       data.get('password'),
                       data.get('email'),
                       data.get('telephone')
                       )
        print(type(user_record))
        try:
            self.db.add_user_record(user_record)
        except Exception as e:
            print("Adding User to Database failed")



    def list_user(self):
        pass

    def modify_user(self):
        pass

    def delete_user(self):
        pass


