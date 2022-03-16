from flask import *
from multiprocessing import Process, Value
import praw
import config
import os
import time, datetime
import smtplib, ssl
import process

app = Flask(__name__)
app.config['SECRET_KEY'] = config.secret_key
email = ""
subreddit = ""
r = process.bot_login()

@app.route('/', methods=('GET', 'POST'))
def render_site():
	if request.method == 'POST':
		email = request.form['email']
		subreddit = request.form['subreddit']
		p = Process(target=process.process, args=(r, subreddit, email))
		p.start()
		return render_template('index.html')
	return render_template('index.html')

def main():
	app.run()
	p.join()

if __name__ == '__main__':
	main()