import pymongo #Import driver

#Connection
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")

#Database Creation
my_database = mongo_client["Covid19"]

def show_all_database():
    print(mongo_client.list_database_names())
show_all_database()

#Create a collection/table
# my_collection = my_database["patient_Statistics_in_Bangladesh"]
my_collection = my_database["patient_Statistics_Covid19"]


# How to change the collection name. For example: "patient statistics in Bangladesh" will be "patient statistics"
def show_collection():
    print(my_database.list_collection_names())
#show_collection()


#CRUD operation
#Insert data into the collection [Create Single]
my_data = {"country_name": "China", "infected_case": 345, "total_recovery": 9190, "death_case": 23870, "date": "17-05_2020"}
#my_collection.insert_one(my_data)

#Insert many

#Multi dimension data [Create Multiple]
my_data_many = [{"country_name":"Canada", "infected_case": 345, "total_recovery": 9190, "death_case": 23870, "date": "17-05_2020"},

{"country_name":"Japan", "infected_case": 45, "total_recovery": 190, "death_case": 70, "date": "17-05_2020"},

{"country_name":"Indonesia", "infected_case": 50, "total_recovery": 90, "death_case": 3870, "date": "17-05_2020"},

{"country_name":"Mexico", "infected_case": 30, "total_recovery": 910, "death_case": 230, "date": "17-05_2020"}
]

#Insert many data
def insert_multiple():
    x = my_collection.insert_many(my_data_many)
    print(x)
#insert_multiple()

#Finding part[Read part]

def find_many_collection(): # Read multiple data
    for x in my_collection.find():
        #print(x['country_name']) #for name only
        print(x) # for all value
#find_many_collection()

#One collection
def find_one_collection(): # Read one data
    x = my_collection.find_one()
    print(x)
#find_one_collection()

###Update part

# Update a country name

def update_country_name():
    myquery = {"country_name": "UK"}
    updated_values = {"$set": {"country_name": "United Kingdom"}}
    my_collection.update(myquery,updated_values)

#update_country_name()
#print("---------------------------------------------------")
#find_many_collection()

#update statistics
def update_statistics():
    myquery = {"infected_case": 345, "country_name": "Bangladesh"}
    updated_values = {"$set": {"infected_case": 2000}}
    myquery2 = {"date": "17-05_2020","country_name": "Bangladesh"}
    updated_date = {"$set": {"date": "18-05_2020"}}
    my_collection.update(myquery,updated_values)
    my_collection.update(myquery2, updated_date)

#update_statistics()
#find_many_collection()

#Delete part
def delete_one_data(country_name):
    myquery = {"country_name":country_name}
    #every space is counted notice it
    #my_collection.delete_one(myquery)
    x = my_collection.delete_one(myquery)
    print(x.deleted_count) # how much data is deleted

#delete_one_data("China")
#insert_multiple()
print("------------------------------")
find_many_collection()












