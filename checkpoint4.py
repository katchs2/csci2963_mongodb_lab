from pymongo import MongoClient
client = MongoClient()

# Function to insert data into mongo db
def insert(db):
    try:
        word = raw_input('Enter word ==> ')
        definition = raw_input('Enter definition ==> ')
       
        db.definitions.insert_one(
               {
                "definition": definition,
                "word": word     
               })
        print '\nInserted data successfully\n'        
        
    except Exception, e:
        print str(e)


# Function to read records from mongo db
def all_records(db):
    try:
        empCol = db.definitions.find()
        print '\n All data from Database \n'
        for emp in empCol:
            print emp

    except Exception, e:
        print str(e)


# Function to read records from mongo db
def one_record(db):
    try:
        emp = db.definitions.find_one()
        print '\n One data from Database \n'
        print emp

    except Exception, e:
        print str(e)

# Function to fetches one specific record from mongo db
def find_by_name(db,word):
    try:
        emp = db.definitions.find({'word': word})
        print '\n Found ' +word+ ' from Database \n'
        print word, ":", str(emp)
        
    except Exception, e:
        print str(e)

# Function to fetches one specific record from mongo db
def find_by_obj_id(db,id):
    try:
        emp = db.definitions.find({_id: ObjectId("56fe9e22bad6b23cde07b8ce")})
        print '\n Found ' +id+ ' from Database \n'
        print id, ":", str(emp)
    

    except Exception, e:
        print str(e)

if __name__ == '__main__':
    
    db = client.csci2963
    collection = db.definitions
    
    ##Fetch all records
    all_records(db)
    
    ##Fetch one record
    one_record(db)
    

    
    ###Fetch a record by object id
    find_by_obj_id(db, '56fe9e22bad6b23cde07b8b7')
    
    ##Insert a new record    
   # insert(db)
    
    ##Fetch a specific record
    find_by_name(db, 'zone')