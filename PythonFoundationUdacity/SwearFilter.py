#use urllib and an API from google to check for profanity
import requests
import urllib3


def read_text():
    content = open('movie_quotes.txt')
    text = content.read()
    content.close()
    return text


#connect to What Do You Love profanity checker
def check_profanity(txt):
    connection = requests.get("http://www.wdylike.appspot.com/?q=" + txt)
    print(connection.content)
    connection.close()

txtCheck = read_text()
check_profanity(txtCheck)