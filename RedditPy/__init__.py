class RedditPy(object):
	def __init__(self, name,Pass,Proxies=False): # init. Log-In with a Username and password
		super(RedditPy, self).__init__()

		with open("RedditPy/media/UA.txt","r") as f: agents = f.read().split("\n")
		import random
		self.UA = random.choice(agents)

		from RedditPy.login import login
		Pass = Pass.replace("u/", "") # you never know if someone is doing it wrong
		self.session = login(self.UA, name,Pass) # storing the logged-in session.

		if Proxies == True: # get proxyes
			import requests
			proxies = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http", allow_redirects=True).text.split("\r\n")
            #print("[*] Downloaded proxies")
			self.session.proxies = {"http": random.choice(proxies)}

	def vote(self,url,Dir="1"):
		from RedditPy.vote import vote
		vote(self.UA, self.session,url,Dir)

	def send_message(self,recipient,title,body):
		from RedditPy.sendMessage import send_message
		send_message(self.UA, self.session,recipient,title,body)

	def post_text(self,subreddit,title,body,NSFW=False,Spoiler=False,OC=False):
		from RedditPy.postText import post_text
		post_text(self.UA, self.session,subreddit,title,body,NSFW,Spoiler,OC)

	def post_comment(self,url,body):
		from RedditPy.comment import comment
		comment(self.UA, self.session,url, body)

	def subscribe(self,user,Type="sub",unsub=False):
		from RedditPy.subscribe import subscribe
		subscribe(self.UA, self.session, user, Type, unsub)

		