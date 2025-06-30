import requests
import boto3
from tqdm import tqdm

ALL_CARDS_URL = "https://ringsdb.com/api/public/cards/"
ALL_PACKS_URL = "https://ringsdb.com/api/public/packs/"

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
dynamodb_client = boto3.client('dynamodb')
table_names = dynamodb_client.list_tables()['TableNames']

def get_table_containing(name: str):
    table_name = filter(lambda x: name in x, table_names)[0]
    table = dynamodb.Table(table_name)
    return table

def populate_player_cards():
    cards = get_cards()
    print("Got cards")

    table = get_table_containing("PlayerCards")

    for card in tqdm(cards):
        table.put_item(Item=card)
    print("Items added successfully")

def populate_packs():
    cards = get_packs()
    print("Got packs")

    table = get_table_containing("Packs")

    for card in tqdm(cards):
        table.put_item(Item=card)
    print("Items added successfully")

def get_cards():
    
    response = requests.get(ALL_CARDS_URL)
    cards = response.json()

    # Validate that every card has a "code"
    assert all("code" in card for card in cards)
    return cards

def get_packs():
    
    response = requests.get(ALL_PACKS_URL)
    cards = response.json()

    # Validate that every card has a "code"
    assert all("id" in card for card in cards)
    return cards

if __name__ == "__main__":
    populate_player_cards()
    populate_packs()
