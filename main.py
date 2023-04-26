
import pymongo
import pandas as pd


def save_query(industry, query_result, db):
    print(query_result)
    df = pd.DataFrame(list(query_result))
    if df.empty:
        print(f"No results found for industry: {industry}")
        return
    # Export to CSV
    df.to_csv("results.csv", index=False)

    # Create new collection in MongoDB
    new_collection = db[industry]
    new_collection.insert_many(df.to_dict("records"))


def make_query(industry):
    # Use a breakpoint in the code line below to debug your script.
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select a database and a collection
    db = client["Industries"]
    collection = db["companies"]

    # Define a query to retrieve documents
    query = {"co_active_industries": industry}

    # Execute the query and retrieve the results
    results = collection.find(query)
    # Print the results

    save_query(industry, results, db)
# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    industries_list = ['Energy', 'Utilities & Waste',
                       'Finance', 'Government', 'Healthcare Services', 'Holding Companies & Conglomerates',
                       'Hospitality', 'Hospitals & Physicians Clinics',
                       'Insurance', 'Law Firms & Legal Services', 'Manufacturing']
    for instance in industries_list:
        make_query(instance)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
