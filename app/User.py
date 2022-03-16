import json

class User:
	def __init__(self, email, subreddit):
	    self.email = email
	    self.subreddit = subreddit
	    self.titles = []

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,
        	sort_keys=True, indent=4)