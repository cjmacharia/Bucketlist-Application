from app import app
from user import User
from bucketlist import Bucketlist
from items import Item
from flask import Flask, session, render_template, request, redirect, g, url_for
import os


newUser = User()
NewItem=Item()
NewBucketlist=Bucketlist()

app.secret_key = os.urandom(24)

@app.route('/register/', methods=['GET', 'POST'])
def reg():
	if request.method== 'POST':
			name=request.form['name']
			email=request.form['email']
			password=request.form['password']
			cpassword=request.form['cpassword']
			result=newUser.register(email,name,password,cpassword)
			if result ==1:
				session['user']=name

				print("hello",session['user'])
				return render_template('login.html')
				
			elif result ==2:
				msg= ("please fill all the fields")
				return render_template ('register.html', data=msg)
			elif result ==3:
				msg= ("password mismatch")	
				return render_template ('register.html',data=msg)


	else:
			return render_template ('register.html')	
			
@app.route('/login/', methods=['GET', 'POST'])
def logins():
	if request.method=="POST":
		emailLogin=request.form['email']
		passLogin=request.form['password']
		loginResult =newUser.login(emailLogin,passLogin)
		if loginResult==1:
			name = newUser.get_user_by_email(emailLogin)
			print('done')
			session['user']=name
			return render_template ('home.html', data=session)
		elif loginResult==3:
			error = "input a field"
			return render_template ('login.html', data=error)	
		elif loginResult==3:
			error = "mismatch"
			return render_template ('login.html', data=error)	
		elif loginResult==4:
			error="password mismatch"
			return render_template ('register.html', data=error) 	
		else:
			error = "cj"
			return render_template ('login.html',data=error) 
	else:
		return render_template('login.html')
		
@app.route('/create/', methods=['GET', 'POST'])
def createBucketlist():
	if request.method=="POST":
		post=request.form['post']
		describe =request.form['description']
		result=NewBucketlist.create(post,describe)
		if result==1:
			data=NewBucketlist.Bucketlists
			return render_template('mybucketlist.html', datas=data)
		if result==2:
			error ="please fill all fields"
			return render_template('create.html' , data=error)
		
		return render_template('mybucketlist.html')
	else:
		return render_template('create.html' )	
# @app.delete('/delete')
# def delete():
# 	result=NewBucketlist.delete(post,description)
# 	if result==true:
# 		msg ="successfully deleted"
# 		return render_template('mybucketlist.html')
# 	else:
# 		return render_template('create.html')	
@app.route('/createitem/', methods=['GET', 'POST'])
def items():
	if request.method=="POST":
		item =request.form['item']
		result=Item.create(item)
		if result==1:
			return render_template('login.html')
	else:
		return render_template('create.html' )
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('logins'))
@app.route('/home/')
def protected():
    if g.user:
        return render_template('home.html')

    return redirect(url_for('logins'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

