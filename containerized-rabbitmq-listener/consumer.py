import pika
import os

import requests
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def main():
    username = os.getenv("USERNAME")
    vhost = os.getenv("VHOST")
    host = os.getenv("HOST")
    password = os.getenv("PASSWORD")
    queueName = "TestQueue"
    exchange = 'choreo'

    serviceURL = os.getenv("SVC_URL")
    consumerKey = os.getenv("CONSUMER_KEY")
    consumerSecret = os.getenv("CONSUMER_SECRET")
    tokenURL = os.getenv("TOKEN_URL")

    if (username != None and vhost != None and host != None and password != None):
        
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, port='5672', virtual_host=vhost, credentials=credentials, socket_timeout=5))

        channel = connection.channel()
        channel.exchange_declare(exchange, durable=True, exchange_type='topic')

        # create a queue in rabbitMQ
        channel.queue_declare(queue=queueName)

        # defining callback function to incoming queue messages
        def callbackFunctionForQueueA(ch, method, properties, body):
            client = BackendApplicationClient(client_id=consumerKey)
            oauth = OAuth2Session(client=client)
            _ = oauth.fetch_token(token_url=tokenURL,client_id=consumerKey,client_secret=consumerSecret,auth=HTTPBasicAuth(consumerKey, consumerSecret))
            response = oauth.get(serviceURL)
            print('Message is received from Queue {}. Message is : '.format(
                queueName), body)
            print("Response from the service: ", response.text)

        # attaching consumer callback function to the queue
        channel.basic_consume(
            queue=queueName, on_message_callback=callbackFunctionForQueueA, auto_ack=True)

        print("Starting consumer session..")

        # starting the consumer session
        channel.start_consuming()
    else:
        print("One or many environment variables was/were not set.")

if __name__ == '__main__':
    main()
