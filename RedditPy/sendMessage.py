def send_message(self, recipient, subject, text):

    path = "api/compose?embedded=true"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "214",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "origin": "https://www.reddit.com",
        "referer": "https://www.reddit.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": self.device["ua"],
        "x-requested-with": "XMLHttpRequest"
    }


    data = {
        "uh": "nqhbb15ir4ff19a7eb7390884a444ae56853ec0eff1e100c82", # i have no idea what this is, but it wont work without it.
        "to": recipient,
        "subject": subject, 
        "text": text,
        "source": "compose",
        "embedded": "web2x",
        "id": "#compose-message",
        "renderstyle": "html"
    }
    r = self.sess.req("POST", path, headers=headers, data=data)
    
    if r.json()["success"]: self.info("[*] successfully send the message!")
    else: self.error("[!] couldnt send the message.")
