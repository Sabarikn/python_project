import requests,ast,json

from requests_oauthlib import OAuth1Session

API_KEY = "p9fKktOiQSRqQQMEnG3cWQBc3"
API_SECRET = "w4P0lBXG4JrEI7UT5mPy9AXgefFlSNJWhmYVRmNfmp2bHjg7Zw"
ACCESS_TOKEN = "1163272818-5iX5o0QcVQpowFuXYettYJbLydOpFzC2txmhoRg"
ACCESS_TOKEN_SECRET = " Jn7eoCGnIiZNE9do9rnDCYzqbjpcdZrhVzIGouqSFQqQa"

username = raw_input("ENTER THE USER_NAME:")
test = OAuth1Session(API_KEY,API_SECRET)
user_timeline= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=7"

r = test.get(user_timeline)
# for k in r.content.split(','):
tweets = json.loads(r.text)
print "Tweets"
print "-"*20
for i in tweets:
    print i["created_at"]+"\n"+i["text"]+"\n\n"
    print "-"*100



# print ("\n".join(r.content.split(',')))