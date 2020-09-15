def login(ua, user,Pass):
    #
    # We need to make 2 requests for the log-in. 
    #   1) Getting the CSRF_TOKEN. 
    #   2) Sending the POST request
    import requests

    session = requests.Session()
    url = "https://www.reddit.com/login"

    headers = {
            "User-Agent": ua, 
            "Accept": "*/*",
            "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.reddit.com",
            "Connection": "close",
            "Referer": "https://www.reddit.com/login/?d2x_sso=username_change",
            "Upgrade-Insecure-Requests": "1"
        }
    try:
        ############## CSRF ##############
        csrf = session.get("https://reddit.com/login",headers=headers).text
        csrf_token = csrf.split('name="csrf_token" value="')[1].split('">')[0]

        ############# POST request #######
        data = {
            "csrf_token": csrf_token,
            "dest": "https://www.reddit.com",
            "username": user,
            "password": Pass
            }
            
        r = session.post(url,headers=headers,data=data)

        if r.status_code == 200:
           # print(r.headers)
            print(f"[*] Logged in as {user}!")
            return session
        else:
            print(r.status_code)
            print(r.headers)
            print(f"[!] could not log in with {user}:{Pass}. Are you sure that the credentials are correct?")
    except:
        print(f"[!] could not log in with {user}:{Pass}. Are you sure that the credentials are correct?")
