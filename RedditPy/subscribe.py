def subscribe(self, user, actionType, unsub):
	####### for users
	if actionType == "user":
		if user.find("u/") != -1: user.replace("/","_")
		else: user = "u_" + user
		path = f"user/{user}"

	####### for subreddits
	elif actionType == "sub":
		path = f"r/{user}"
		if user.find("r/") != -1: user.replace("/","_")
	else:
		self.error("[!] please only input 'sub' or 'user', and not anything else.")
		return

	if unsub: action = "unsub"
	else: action = "sub"

	headers = {
		"user-agent": self.device["ua"]
	}

	postBody = self.sess.req("GET", path, headers=headers)

	if postBody.status_code > 200: return self.error("Couldnt get sub/user")

	auth = postBody.text.split('"accessToken":"')[1].split('"')[0]
	xRedditSession = postBody.split('"sessionTracker":"')[1].split('"')[0]
	loid = postBody.text.split('"loid":"')[1].split('"')[0]
	loidCreated = postBody.split('"loidCreated":"')[1].split('"')[0]
	blob = postBody.text.split('"blob":"')[1].split('"')[0]

	xRedditSession = postBody.split('"sessionTracker":"')[1].split('"')[0]
	authorization = f"Bearer {auth}"
	xRedditLoid = f"{loid}.2.{loidCreated}.{blob}"

	########################

	headers = {
		"accept": "*/*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
		"authorization": authorization,
		"content-length": "32",
		"content-action": "application/x-www-form-urlencoded",
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

	data = {
		"action": action,
		"sr_name": user,
		"api_action": "json"
	}

	final = self.sess.req("POST", "https://oauth.reddit.com/api/subscribe", headers=headers, data=data)
	if final.text == "{}": self.info("[*] subscribed successfully!")
	else:
		self.error("[*] something failed. Debug info:")
		self.error(final.text)
