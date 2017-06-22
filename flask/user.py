from flask import Flask, session, render_template, request, redirect, g, url_for
import re
user_id=0
users = []
class User():

    
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def register(self,email, name,password, cpassword):       
            if password==cpassword:
                if  name!='' and email!='' and password!='':

                    for user in users:
                        if user['email']==email:
                            return 4
                    user = {}
                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                    result = email
                    if re.search(regex, result):
                        match = re.search(regex, result)
                         
                        user['email']=email
                        user['name']=name 
                        user['password']=password
                        users.append(user)
                        print(users) 
                        return  1
                    else:
                        return 5 
                else:
                    return 2
            else:
                return 3
                        
    def login(self, email, password):
        # import pdb; pdb.set_trace()
        for user in users:
            if user['email']==email:
                if user['password']==password:
                    return 1
                    # print ('done')
                else:
            #     else:
                    return 3
            # elif email!='' and password!='':
            #     return 2
            # else:
            #     return 4        
    def get_user_by_email(self, email):
        for user in users:
            if user['email'] == email:
                return user['name']
                break
        else:
            return False