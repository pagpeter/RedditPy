# ⚠️⚠️ THIS IS CURRENTLY BROKEN; THE CODE IS OUTDATED! ⚠️⚠️

# About:

RedditPy aims to be a unofficial open-source python API for reddit, that doesn't require any tokens except your password and username.

It only supports a few actions.

# RedditPy Documentation

## Getting started

```py
from RedditPy import RedditPy

re = RedditPy("<username>", "<password>") # optional: proxy=True
```

## Logging in

```py
re.login()
```

### Upvoting a Post:

```py
re.vote("<post-url>", "1") # 1 for upvote, -1 for downvote, 0 for no vote
```

### Sending a message: (message, not chat.)

```py
re.send_message("<recipient>", "<title>", "<body>")
```

### Posting a text-post:

```py
re.post_text("<subreddit>", "<title>", "<body>") # optional: NSFW=True, Spoiler=True, OC=True
```

### subscribing to a subreddit/user:

```py
re.subscribe("<subreddit/user>") # optional: Type="user", unsub=True
```
