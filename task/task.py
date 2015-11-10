# Python application for pushing content to Google Tasks using the CLI
# This app does not work and needs some TLC

from sys import argv
from requests_oauthlib import OAuth2Session
from datetime import date
from ast import literal_eval


def authenticate():    # Credentials you get from registering a new application
    info = readData()
    client_id = info['installed']['client_id']    #<the id you get from google>.apps.googleusercontent.com'
    client_secret = info['installed']['client_secret']    #<the secret you get from google>'
    redirect_uri = info['installed']['redirect_uris'][0]      #https://your.registered/callback'

    print client_id
    print client_secret
    print redirect_uri

    # OAuth endpoints given in the Google API documentation
    authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
    token_url = "https://accounts.google.com/o/oauth2/token"
    scope = [
        'https://www.googleapis.com/auth/tasks',
        'https://www.googleapis.com/auth/tasks.readonly'
        ]

    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

    # Redirect user to Google for authorization
    authorization_url, state = google.authorization_url(authorization_base_url,
    # offline for refresh token
    # force to always make user click authorize
    access_type="offline", approval_prompt="force")
    print 'Please go here and authorize,', authorization_url

    # Get the authorization verifier code from the callback url
    redirect_response = raw_input('Paste the full redirect URL here:')

    # Fetch the access token
    google.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

    # Fetch a protected resource, i.e. user profile
    r = google.get('https://www.googleapis.com/tasks/v1/users/@me/lists')
    print r.content

def readData():  # opens client_secrets.json and reads it to an array
    f = open('client_secrets.json','r')
    info = literal_eval(f.read())
    f.close()
    return info

def content():    # Gets text from CLI
    text = raw_input("Enter text: ")
    return text

def push(text):    # Pushes text to Google Tasks
    today = date.today()
    print text + " " + str(today)

if __name__ == "__main__":
    args = []
    args = list(argv)
    print "Hello, this is the task app."
#    print "You entered: " + str(args)

    authenticate()