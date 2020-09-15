def comment(ua, session,url,body):
	import requests

	if url.find("?") != -1:
		url = url.split("?")[0]

	################################################ TOKENS AND STUFF
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
	################################################### 3
	weirdUrl = "https://oauth.reddit.com/api/comment"

#try:

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
		"api_type": "json",
		"return_rtjson": "true",
		"thing_id": name,
		"text": "",
		"richtext_json": '{"document":[{"e":"par","c":[{"e":"text","t":"'+body+'"}]}]}' # this is crap
	}

	final = requests.post(url,headers=headers,data=data).text
	print(final)
	quit()
	link = "reddit.com"+final["permalink"]
	print(f"[*] commented successfully! The url is {link}")
	#except:
		#print("[!] could not comment. Is all the input data correct?")

