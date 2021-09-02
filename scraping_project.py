from csv_scrapper import scrape_quotes

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess =''
    while guess.lower() != quote["author"].lower():
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses - 1}\n")
        remaining_guesses -= 1
        if guess.lower() == quote["author"].lower():
            print("You Win, now I die! unless....")  
            break
        elif remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint kiddo! The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's another friend... The author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Last hint oooooooooh... The author's last name starts with {last_initial}")
        else:
            print("you lose")
            guess = quote["author"]

    again = ''
    while again.lower() not in ('y','yes','n','no'):
        again = input("Would you like to play again (y/n)?:\n")
    if again.lower() in ('yes','y'):
        print('lets play again')
        return start_game(quotes)
    else:
        print("okay bye..")


start_game(scrape_quotes())