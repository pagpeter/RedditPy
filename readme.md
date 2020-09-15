# About:
RedditPy aims to be a unofficial open-source python API for reddit, that doesn't require any tokens except your password and username.

If you like this project, star it!

# RedditPy Documentation

## Getting started

```
from RedditPy import RedditPy

re = RedditPy("<username>", "<password>") # optional: proxy=True
```
### Upvoting a Post:
```
re.vote("<post-url>", "1") # 1 for upvote, -1 for downvote, 0 for no vote
```
### Sending a message: (message, not chat.)
```
re.send_message("<recipient>", "<title>", "<body>")
```
### Posting a text-post:
```
re.post_text("<subreddit>", "<title>", "<body>") # optional: NSFW=True, Spoiler=True, OC=True
```
### subscribing to a subreddit/user:
```
re.subscribe("<subreddit/user>") # optional: Type="user", unsub=True
```