import tweepy
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#def gettwitterdata(keyword,dfile):

#Twitter APIを使用するためのConsumerキー、アクセストークン設定

Consumer_key = os.getenv('CONSUMER_KEY')
Consumer_secret = os.getenv('CONSUMER_SECRET')
Access_token = os.getenv('ACCESS_TOKEN')
Access_secret = os.getenv('ACCESS_TOKEN_SECRET')

#認証
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)
keyword='kubernetes'
#検索キーワード設定 
q = keyword

#つぶやきを格納するリスト
tweets_data =[]

#カーソルを使用してデータ取得
for tweet in tweepy.Cursor(api.search, q=q,tweet_mode='extended',lang='ja').items(10):

    #つぶやき時間がUTCのため、JSTに変換  ※デバッグ用のコード
    #jsttime = tweet.created_at + datetime.timedelta(hours=9)
    #print(jsttime)

    #つぶやきテキスト(FULL)を取得
    tweets_data.append(tweet.full_text + '\n')
    print(tweet.full_text)

print('Twitterからの収集完了：{}件'.format(len(tweets_data)))
with open("tweet.txt", "w",encoding="utf-8") as f:
    f.writelines(tweets_data)
