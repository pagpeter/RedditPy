def vote(self, url, actionDirection):
	actionDirection = str(actionDirection)

	if actionDirection == "1" or "+1": actionDirection = "+1"
	elif actionDirection == "-1": actionDirection = "-1"
	elif actionDirection == "0": actionDirection = "0"
	else: return self.error("[!] Please supply a valid vote direction!")
		
	if url.find("?") != -1: url = url.split("?")[0]
	
	headers = {
		"User-Agent": self.device["ua"]
	}
	try:
		postData = self.sess.req("GET", url, headers=headers).text

		auth = postData.split('"accessToken":"')[1].split('"')[0]

		xRedditSession = postData.split('"sessionTracker":"')[1].split('"')[0]

		loid = postData.split('"loid":"')[1].split('"')[0]
		loidCreated = postData.split('"loidCreated":"')[1].split('"')[0]
		blob = postData.split('"blob":"')[1].split('"')[0]
		version = "2"

		#getting the 3 tokens we need from the sourcecode of the site. Will use bs4 later, but this works so far
		xRedditSession = postData.split('"sessionTracker":"')[1].split('"')[0]
		authorization = "Bearer "+auth
		xRedditLoid = loid + "." + version + "." + loidCreated + "." + blob

		########################## REQUEST 2
		# same headers as before

		r = self.sess.req("GET", f"{url}.json", headers=headers).json()[0]["data"]["children"][0]["data"] # no need to do it in with the same session thingy

		name = r["name"]
	except:
		self.error("[!] Request 1 failed. Does the link exist?")
	########################## REQUEST 4
	postUrl = "https://oauth.reddit.com/api/vote"

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

		data = {
			"id": name, #(name we got from request 2)
			"dir": actionDirection, # dir is the direction. -1: downvote, +1: upvote, 0: no vote
			"api_type": "json"
		}
		
		Post1 = self.sess.req("POST", postUrl, headers=headers, data=data)
		if Post1.text == "{}":
			self.info("[*] voted successfull!")
		else:
			self.error("[*] something failed. Debug info:")
			self.error(Post1.text)
	except:
		self.error("[!] Request 2 failed. Does the link exist?")