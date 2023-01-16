import tweepy

"""
مفاتيح تويتر غير الاكس للمفاتيح حقت حسابك
تقدر تجيب مفاتيح لحسابك بتويتر من هنا
developer.twitter.com 
"""    
consumer_key = "n0JKPJt1wZ9omLIttqTtcMkZR"
consumer_secret = "vIkuurPc7XqeL553RqVHr7wwsTC3ETeKxCXrR5DmSOn3mC2kmI"
access_token= "1305148587010031617-QUPMmg7QInrSutTbejwGGXbgxRrkek"
access_secret = "n2GfLIIWtH1hg282xV8nUsJoBnRBmvYyO4uUxqpzIEN2T"

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
