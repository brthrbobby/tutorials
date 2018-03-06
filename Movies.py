def read_text():
    quotes = open(r"C:\Users\Bobby Musser\tutorials\movie_quotes.txt")
    print(quotes.read())

    quotes.close()

read_text()