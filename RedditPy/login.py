def login(self, user, pwd):

    url = "https://www.reddit.com/login"

    headers = {
            "User-Agent": self.device["ua"], 
            "Accept": "*/*",
            "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.reddit.com",
            "Connection": "close",
            "Referer": "https://www.reddit.com/login/?d2x_sso=username_change",
            "Upgrade-Insecure-Requests": "1"
        }
    
    ############## CSRF ##############
    csrf = self.sess.req("GET", "login", headers=headers)
    if csrf.status_code > 399:
        self.error(f"[!] could not get CSRF token for login", csrf)
        return False
        
    csrf_token = csrf.text.split('name="csrf_token" value="')[1].split('">')[0]
    self.debug("CSRF:", csrf_token)

    ############# POST request #######
    data = {
        "csrf_token": csrf_token,
        "dest": "https://www.reddit.com",
        "username": user,
        "password": pwd
    }
        
    r = self.sess.req("POST", "login", headers=headers,data=data)
    if r.status_code == 200:
        self.info(f"[*] Logged in as {user}!")
        self.debug(r.cookies)
    else:
        self.debug(r.status_code)
        self.debug(r.headers)
        self.error(f"[!] could not log in with {user}:{pwd}. Are you sure that the credentials are correct?")
