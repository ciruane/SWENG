from github import Github
from flask import Flask, render_template, request, redirect, url_for, flash, session
app = Flask(__name__)
app.secret_key = 'SHHHH, it\'s a secret!'
app.config['SESSION_TYPE'] = 'filesystem'

name = ""
	
@app.route('/data.tsv',methods = ['POST', 'GET'])
def data():
	theData = "language\tfrequency\n"
	g = Github(session["username"], session["password"])
	try:
		user = g.get_user(name)
	except:
		user = g.get_user()
	langDict = {}
	for repo in user.get_repos():
			num = 0
			for language, num in repo.get_languages().items():
				try:
					langDict[language] += num
				except:
					langDict[language] = num
			#for commit in repo.get_commits():
				#num = num + 1
			#theData = theData + repo.name + "\t" + str(num) + "\n"
	for language, num in langDict.items():
		theData = theData + language + "\t" + str(num/1000) + "\n"
	return theData

@app.route('/search',methods = ['POST', 'GET'])
def search():
	global name
	name = request.form['repo']
	return render_template("js.html", name = name)

@app.route('/',methods = ['POST', 'GET'])		
@app.route('/index',methods = ['POST', 'GET'])
@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		session["username"] = request.form['nm']
		session["password"] = request.form['nm2']
		g = Github(session["username"], session["password"])
		data = ""
		for repo in g.get_user().get_repos():
			data = data + "," + repo.name
    
		return render_template("js.html", name = session["username"])
	else:
		return render_template("login.html")


if __name__ == '__main__':
	app.run(debug = True)
