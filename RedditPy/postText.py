def post_text(ua, session,subreddit,title,body,NSFW,Spoiler,OC):
	import requests

	if subreddit.find("r/") != -1:
		subreddit = subreddit.split("r/")[1]

	############################### REQUEST 1: TOKENS AND STUFF
	headers = {
		"User-Agent": ua
	}
	try:
	url = "https://www.reddit.com/r/"+subreddit+"/submit"
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

	except:
		print("[!] Request 1 failed. Does the link exist?")
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
			"user-agent": ua,
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
		
		final = session.post(postUrl,headers=headers,data=data,timeout=5)
		try:
			url = final.json()["json"]["data"]["url"]
			print(f"[*] post posted successfull, url={url}")
		except:
			print("[*] something failed. Debug info:")
			print(final.json())

	except:
		print("[!] Request 2 failed. Is the data correct?")


