import os
import random

import tweepy

client = tweepy.Client(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
)


def passQuote(quote: str, log: list[str]) -> bool:
    return (
        True
        if quote and quote.strip() and not quote.startswith("#") and quote not in log
        else False
    )


def getQuote() -> str:
    with open("recent.txt", "r", encoding="utf-8") as f:
        log = f.read().splitlines()
        if len(log) < 11:
            log = [""] * (11 - len(log)) + log
    with open("quotes.txt", "r", encoding="utf-8") as f:
        quotes = [quote for quote in f.read().splitlines() if passQuote(quote, log)]
    random_quote = random.choice(quotes)
    log.pop(0)
    log.append(random_quote)
    with open("recent.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    return random_quote.replace("\\n", "\n")


client.create_tweet(text=getQuote())
