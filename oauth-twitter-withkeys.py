
from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.CONSUMER_KEY
client_secret = secrets.CONSUMER_SECRET

resource_owner_key = secrets.ACCESS_KEY
resource_owner_secret = secrets.ACCESS_SECRET

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
twitter = json.loads(r.text)
print (twitter)
