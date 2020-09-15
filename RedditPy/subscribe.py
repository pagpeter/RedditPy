def subscribe(ua, session,user,Type,unsub):
	try:
		import requests
		####### for users
		if Type == "user":
			infoUrl = "https://www.reddit.com/user/" + user
			if user.find("u/") != -1:
				user.replace("/","_")
			elif user.find("u/") == -1:
				user = "u_" + user
		####### for subreddits
		elif Type == "sub":
			infoUrl = "https://www.reddit.com/r/" + user
			if user.find("r/") != -1:
				user.replace("/","_")
		else:
			print("[!] please only input 'sub' or 'user', and not anything else.")
			return

		if unsub == True:
			action = "unsub"
		else:
			action = "sub"
	########################

		headers = {
			"User-Agent": ua
		}
		try:
			PostData = session.get(infoUrl,headers=headers,timeout=5).text

			auth = PostData.split('"accessToken":"')[1].split('"')[0]

			xRedditSession = PostData.split('"sessionTracker":"')[1].split('"')[0]

			loid = PostData.split('"loid":"')[1].split('"')[0]
			loidCreated = PostData.split('"loidCreated":"')[1].split('"')[0]
			blob = PostData.split('"blob":"')[1].split('"')[0]
			version = "2"

			#getting the 3 tokens we need from the sourcecode of the site. Will use bs4 later, but this works so far
			xRedditSession = PostData.split('"sessionTracker":"')[1].split('"')[0]
			authorization = "Bearer "+auth
			xRedditLoid = loid + "." + version + "." + loidCreated + "." + blob
		except:
			print("[!] Request 1 failed. Does the link exist?")
		########################
		postUrl = "https://oauth.reddit.com/api/subscribe"

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
			"user-agent": ua,
			"x-reddit-loid": xRedditLoid,
			"x-reddit-session": xRedditSession
		}

		data = {
			"action": action,
			"sr_name": user,
			"api_action": "json"
		}

		final = requests.post(postUrl,headers=headers,data=data)
		if final.text == "{}":
			print("[*] subscribed successfully!")
		else:
			print("[*] something failed. Debug info:")
			print(final.text)
	except:
		print("[!] Request 2 failed. Does the link exist?")
