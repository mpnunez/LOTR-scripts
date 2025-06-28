import requests
import boto3
from tqdm import tqdm

ALL_CARDS_URL = "https://ringsdb.com/api/public/cards/"
DDB_TABLE_NAME = "AwsLotrStack-PlayerCardsEAD479B2-QCT1UV83CK4J"

def main():
    cards = get_cards()
    print("Got cards")

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table(DDB_TABLE_NAME)

    for card in tqdm(cards):
        table.put_item(Item=card)
    print("Items added successfully")

def get_cards():
    
    response = requests.get(ALL_CARDS_URL)
    cards = response.json()

    # Validate that every card has a "code"
    assert all("code" in card for card in cards)
    return cards

def add_card(card: dict):
    import boto3





if __name__ == "__main__":
    main()
