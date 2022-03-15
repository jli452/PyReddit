import praw
import config
import os
import time, datetime
import smtplib, ssl

def bot_login():
    print("Logging in")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "copy paste bot")
    print("Logged in using this bot: " + config.username)
    return r

def get_date(post):
    time = post.created
    return datetime.datetime.fromtimestamp(time)

def write_title(title):
    exists = os.path.exists("titles.txt")
    if exists:
        with open("titles.txt", "a") as f:
            f.write(title + "\n")
    else:
        f = open("titles.txt",'w')
        f.write(title + "\n")

def text_to_dict(textfile):
    titles = {}
    f = open(textfile, 'r')
    for line in f:
        titles[line.strip()] = None
    f.close()
    return titles

def email(sender_email, receiver_email, message, password):
    port = 465
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def run_bot(r, sr, pw, se, re):
    for post in r.subreddit(sr).new(limit = 25):
        if post.title not in text_to_dict("titles.txt"):
            write_title(post.title)
            message = "New post to " + sr + ":" + post.title
            email(se, re, pw, message)

def main():
    r = bot_login()
    sr = input("Type in the subreddit you want to track:\n")
    se = input("Type sender email:\n")
    re = input("Type receiver email:\n")
    pw = input("Type your password for email that you want to receive new notifications for:\n")
    while(1):
        run_bot(r, sr, pw, se, re)

if __name__ == "__main__":
    main()
