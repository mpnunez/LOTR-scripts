import requests

url = "https://ringsdb.com/api/public/cards/"

def main():

    response = requests.get(url)

    cards = response.json()
    for card in cards:
        print(card)

if __name__ == "__main__":
    main()
