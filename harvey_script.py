import praw
import config
import os
import time

def bot_login():
    print("Logging in")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "copy paste bot")
    print("Logged in using this bot: " + config.username)
    return r

def run_bot(r, comments_replied):
    for comment in r.subreddit('tifu').comments(limit = 25):
        if "you" in comment.body and comment.id not in comments_replied and comment.author != r.user.me():
            comment.reply("good bot")
            #comment.reply("Harvey G. Stenger is an American educator and academic administrator, who is serving as the seventh president of Binghamton University since 2012.")
            comments_replied.append(comment.id)
            print("a comment has been replied to in this session")
            with open("comments_replied.txt", "a") as f:
                f.write(comment.id + "\n")
            time.sleep(.5)

def get_saved_comments():
    if not os.path.isfile("comments_replied.txt"):
        comments_replied = []
    else:
        with open("comments_replied.txt", "r") as f:
            comments_replied = f.read()
            comments_replied = comments_replied.split("\n")
            comments_replied = list(filter(None, comments_replied))
    return comments_replied

r = bot_login()
comments_replied = get_saved_comments()

while True:
    run_bot(r, comments_replied)
