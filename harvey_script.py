import praw
import config

def bot_login():
    print("Logging in")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "copy paste bot")
    print("Logged in using this bot: " + config.username)
    return r

def run_bot(r):
    num_commented = 0
    for comment in r.subreddit('BinghamtonUniversity').comments(limit = 100):
        if "Harvey" in comment.body:
            comment.reply("Harvey G. Stenger is an American educator and academic administrator, who is serving as the seventh president of Binghamton University since 2012.")
            num_commented += 1
            print(str(num_commented) + " comments replied to")

def main():
    r = bot_login()
    run_bot(r)

main()
