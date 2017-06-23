import unittest
from user import User

class Usertest(unittest.TestCase):
     #tests for the class
    def setUp(self):
        self.newUser=User()


    def test_register_null_name(self):
        output=self.newUser.register('test@email.com','','pass','pass')
        self.assertEqual(2,output, "please fill all fields")
    def test_register_null_email(self):
        output=self.newUser.register('','name','pass','pass')
        self.assertEqual(2,output, "please fill all fields")    
    def test_cpassword_is_password(self):
        output=self.newUser.register('test@email.com', 'cj', 'pass', 'pss')    
        self.assertEqual(3,output, "please match your passwprds")
    def test_if_login_password_exist(self):
        output = self.newUser.login('email@gmail.com', 'pass')
        self.assertEqual(2,output, "password mismatch" )    
if __name__ == "__main__":
    unittest.main()        