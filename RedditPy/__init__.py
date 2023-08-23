from RedditPy.login import login
from RedditPy.vote import vote
from RedditPy.sendMessage import send_message
from RedditPy.postText import post_text
# from RedditPy.comment import comment
from RedditPy.subscribe import subscribe
from RedditPy.request import Session

class RedditPy():
	def __init__(self, user, pwd, proxy={}, timeout=8, log=[]): 
		self.device = {
			"clientHint": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
			"clientPlatform": '"macOS"',
        	"language": "en-US",
			"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
		} 

		self.proxy = proxy
		self.sess = Session(proxy, timeout)
		self.user = user 
		self.pwd = pwd 
		self.log = log

	def get_session(self):
		return self.sess._sess.cookies["session"]

	def info(self, *kwargs):
		if "info" not in self.log: return
		print("[INFO]", *kwargs)

	def error(self, *kwargs):
		if "error" not in self.log: return
		print("[ERROR]", *kwargs)

	def debug(self, *kwargs):
		if "debug" not in self.log: return
		print("[DEBUG]", *kwargs)

	def login(self):
		login(self, self.user, self.pwd) 

	def vote(self, url, direction="1"):
		vote(self, url, direction)

	def send_message(self, recipient, title, body):
		send_message(self, recipient, title, body)

	def post_text(self, subreddit, title, body, NSFW=False, Spoiler=False, OC=False):
		post_text(self, subreddit, title, body, NSFW, Spoiler, OC)

	# def post_comment(self,url,body):
	# 	comment(self.UA, self.session,url, body)

	def subscribe(self, user, actionType="sub", unsub=False):
		subscribe(self, user, actionType, unsub)

		