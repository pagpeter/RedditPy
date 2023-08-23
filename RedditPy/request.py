import tls_client

class Session():
    def __init__(self, proxy, timeout):
        self.proxy = proxy
        self.base_url = "https://reddit.com"
        self.timeout = timeout
        self._sess = tls_client.Session(client_identifier="chrome112")

    def log(self, *kwars):
        print("[REQUEST]", *kwars)
    
    def req(self, method, path, data="", headers={}):
        if "https://" in path: url = path
        else: url = f"{self.base_url}/{path}"
        
        self.log(method, url)

        return self._sess.execute_request(
            method, 
            url, 
            data=data, 
            headers=headers, 
            timeout_seconds=self.timeout, 
            proxy=self.proxy, 
            allow_redirects=True, 
            insecure_skip_verify=True,
        )
