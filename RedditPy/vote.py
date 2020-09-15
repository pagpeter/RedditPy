def vote(ua, session,url,Dir):
	import requests
	Dir = str(Dir)
	if Dir == "1" or "+1":
		Dir = "+1"
	elif Dir == "-1":
		Dir = "-1"
	elif Dir == "0":
		Dir = "0"
	else:
		print("[!] Please supply a valid vote direction!")
		return
	if url.find("?") != -1:
		url = url.split("?")[0]
	#	to upvote a post, tons of requests have to be done.
	#	1) a GET request to the post url.
	#		we need to retrive several tokens and stuff.
	#		a) x-reddit-loid
	#			loid + "." + version + "." + loidCreated + "." + blob version is 2 most of the time, so we just use 2 for now
	#			example: 00000000004qopi8gg.2.1570381230000.Z0FBQUFBQmZLc0hCd3liS1BPR1gwMGpoZjY5dnI1cV9aMktYVXpJWERaQkxIXzlZTzdSdDJEYWl4NDh6eTVDQjlpSU42QmtJcE9wb0FtZlFldkpYd2NPYTdXTlpfSXd0M3NSTzR5UXYxenljTEhpc195OTFtcHYtM29jMHhOZHVwOUZFMFUzZDlxVlo
	#		b) authorization 
	#			"Bearer " + accessToken
	#		c) x-reddit-session
	#			sessionTracker
	#
	#	2) get the intern name of the poster, and more data we need (eg. t3_i3kzvz)
	#		we do a request to the url + ".json"
	#		then we GET the data: r[0]["data"]["children"][0]["data"]["name"]
	#		we also get some more data for the last request
	#
	#	3) the first POST request, again to https://oauth.reddit.com/api/vote?redditWebClient=desktop2x&app=desktop2x-client-production&raw_json=1&gilding_detail=1
	#		important:
	#		here we have the x-reddit-loid
	#						 x-reddit-session and 
	#						 authorization
	#		crap in the headers.
	#		we also have a bit data to send:
	#			{
	#			"id": name (name we got from request 2)
	#			"dir": "-1" idk what that is
	#			"api_type": "json"
	#			}
	########################## REQUEST 1

	headers = {
		"User-Agent": ua
	}
	try:
		PostData = session.get(url,headers=headers,timeout=5).text

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

		########################## REQUEST 2
		# same headers as before

		r = requests.get(url+".json",headers=headers,timeout=5).json()[0]["data"]["children"][0]["data"] # no need to do it in with the same session thingy

		name = r["name"]
	except:
		print("[!] Request 1 failed. Does the link exist?")
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
			"user-agent": ua,
			"x-reddit-loid": xRedditLoid,
			"x-reddit-session": xRedditSession
		}

		data = {
			"id": name, #(name we got from request 2)
			"dir": Dir, # dir is the direction. -1: downvote, +1: upvote, 0: no vote
			"api_type": "json"
		}
		
		Post1 = session.post(postUrl,headers=headers,data=data,timeout=5)
		if Post1.text == "{}":
			print("[*] voted successfull!")
		else:
			print("[*] something failed. Debug info:")
			print(Post1.text)
	except:
		print("[!] Request 2 failed. Does the link exist?")