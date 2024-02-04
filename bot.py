import os
import random
import sys

from dotenv import load_dotenv
import tweepy

os.chdir(sys.path[0])
load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
)


def passQuote(quote: str, log: list[str]) -> bool:
    return quote.strip() and not quote.startswith("#") and quote not in log


def getQuote() -> str:
    with open("recent.txt", "r", encoding="utf-8") as f:
        log = f.read().splitlines()
        if len(log) < 11:
            log = [""] * (11 - len(log)) + log
    with open("quotes.txt", "r", encoding="utf-8") as f:
        quotes = [quote for quote in f.read().splitlines()
                  if passQuote(quote, log)]
    random_quote = random.choice(quotes)
    log.pop(0)
    log.append(random_quote)
    with open("recent.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    return random_quote.replace("\\n", "\n")


if __name__ == "__main__":
    tweet = client.create_tweet(text=getQuote())
    print(tweet.data["id"])
