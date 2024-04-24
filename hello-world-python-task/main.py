import os
print("Hello World")
serviceURL = os.getenv("SVC_URL")
consumerKey = os.getenv("CONSUMER_KEY")
consumerSecret = os.getenv("CONSUMER_SECRET")
tokenURL = os.getenv("TOKEN_URL")

print("serviceURL:", serviceURL)
print("consumerKey:", consumerKey)
print("consumerSecret:", consumerSecret)
print("tokenURL:", tokenURL)
print("*****************")
env_variables = dict(os.environ.items())
print('env_variables',env_variables)
