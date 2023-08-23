from RedditPy import RedditPy

re = RedditPy("<user>", "<pwd>", log=["debug", "log", "info"], proxy="http://localhost:8888")
re.login()
print("Logged in - Session:", re.get_session())
re.send_message("u/spez", "does this work", "yes it does")
