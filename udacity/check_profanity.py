# import requests
import urllib.request
import urllib.parse


def read_text():
    quotes = open(r"C:\Users\juanj\Documents\PycharmProjects\python-basics\udacity\movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)


def check_profanity(text):
    # results = requests.get("http://www.wdylike.appspot.com/", params={'q': text})
    # print(results.text)
    params = urllib.parse.urlencode({'q': text})
    url = "http://www.wdylike.appspot.com/?%s" % params
    with urllib.request.urlopen(url) as response:
        output = response.read().decode('utf-8')
        if "true" in output:
            print("Profanity alert!")
        elif "false" in output:
            print("This document has no curse words!")
        else:
            print("Could not scan the document properly")


read_text()
