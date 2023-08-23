def post_text(self, subreddit, title, body, NSFW, Spoiler, OC):

	if subreddit.find("r/") != -1:
		subreddit = subreddit.split("r/")[1]

	############################### REQUEST 1: TOKENS AND STUFF
	headers = {
		"User-Agent": self.device["ua"]
	}
	try:
		path = f"r/{subreddit}/submit"
		res = self.sess.req("GET", path, headers=headers).text

		auth = res.split('"accessToken":"')[1].split('"')[0]

		xRedditSession = res.split('"sessionTracker":"')[1].split('"')[0]

		loid = res.split('"loid":"')[1].split('"')[0]
		loidCreated = res.split('"loidCreated":"')[1].split('"')[0]
		blob = res.split('"blob":"')[1].split('"')[0]
		version = "2"

		#getting the 3 tokens we need from the sourcecode of the site. Will use bs4 later, but this works so far
		xRedditSession = res.split('"sessionTracker":"')[1].split('"')[0]
		authorization = "Bearer "+auth
		xRedditLoid = loid + "." + version + "." + loidCreated + "." + blob

	except:
		self.error("[!] Request 1 failed. Does the link exist?")
		return

	############################### REQUEST 2: SUBMITTING THE POST

	postUrl = "https://oauth.reddit.com/api/submit"
	
	try:

		headers = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
			"authorization": authorization,
			"content-length": "32",
			"content-type": "application/x-www-form-urlencoded",
			"dnt": "1",
			"origin": "https://www.reddit.com",
			"referer": "https://www.reddit.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.device["ua"],
			"x-reddit-loid": xRedditLoid,
			"x-reddit-session": xRedditSession
		}
		richtext = '{"document":[{"e":"par","c":[{"e":"text","t":"'+body+'"}]}]}' # this is crap
		#quit()
		data = {
		"sr": subreddit,
		"api_type": "json",
		"show_error_list": "true",
		"title": title,
		"spoiler": str(Spoiler).lower(),
		"nsfw": str(NSFW).lower(),
		"kind": "self",
		"original_content": str(OC).lower(),
		"submit_type": "subreddit",
		"post_to_twitter": "false",
		"sendreplies": "true",
		"richtext_json": richtext,
		"validate_on_submit": "true"
			}
		
		final = self.sess.req("POST", postUrl, headers=headers, data=data)
		try:
			path = final.json()["json"]["data"]["url"]
			self.info(f"[*] post posted successfull, url={path}")
		except:
			self.error("[*] something failed (post_text())")
			self.debug(final.json())

	except:
		self.error("[!] Request 2 failed. Is the data correct?")


