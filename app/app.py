from flask import *
from multiprocessing import Process, Value
import process
import config
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = config.secret_key
email = ""
subreddit = ""
r = process.bot_login()
users = []

@app.route('/', methods=('GET', 'POST'))
def render_site():
	if request.method == 'POST':
		email = request.form['email']
		subreddit = request.form['subreddit']
		new = process.add_user(email, subreddit, users)
		p = Process(target=process.process, args=(r, subreddit, email))
		p.start()
		# original_stdout = sys.stdout
		# with open('titles.json', 'w') as f:
		# 	sys.stdout = f
		# 	for user in users:
		# 		print(user)
		# 	sys.stdout = original_stdout
	return render_template('index.html')

def main():
	app.run()
	p.join()

if __name__ == '__main__':
	main()