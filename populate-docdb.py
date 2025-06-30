from pymongo import MongoClient

def main():
    # Replace with your DocumentDB cluster endpoint, username, and password
    cluster_endpoint = "mydocdbclusterccbd30a4-07xk4eoivd1h.cluster-cbyg8uccwraq.us-west-2.docdb.amazonaws.com:27017"
    username = "Marcel"
    password = None
    ca_file_path = "global-bundle.pem" # Path to the downloaded certificate

    ##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
    #client = MongoClient(f'mongodb://{username}:{password}@mydocdbclusterccbd30a4-07xk4eoivd1h.cluster-cbyg8uccwraq.us-west-2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false') 
    client = MongoClient(
        "mongodb://{username}:{password}@{cluster_endpoint}/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false"
    )

    ##Specify the database to be used
    db = client.sample_database

    ##Specify the collection to be used
    col = db.sample_collection

    ##Insert a single document
    col.insert_one({'hello':'Amazon DocumentDB'})

    ##Find the document that was previously written
    x = col.find_one({'hello':'Amazon DocumentDB'})

    ##Print the result to the screen
    print(x)

    ##Close the connection
    client.close()

if __name__ == "__main__":
    main()
