from pymongo import MongoClient
import random
import datetime

client = MongoClient()

# Function to read records from mongo db
def all_records(db):
    try:
        empCol = db.definitions.find()
        print '\n All data from Database \n'
        for emp in empCol:
            print emp

    except Exception, e:
        print str(e)


# Function to fetches one specific record from mongo db
def find_by_index(db,index):
    try:
        emp = db.definitions.find()[index]
        print '\n Found index from Database \n'
        print index, ":", str(emp)
        return emp
        
    except Exception, e:
        print str(e)
        
        
def update_with_date(db, word):
    db.definitions.update({"word": word}, {'$push' : {"time": datetime.datetime.now()}})
    print "added time"

###def random_word_requester():
    ###'''
    ###This function should return a random word and its definition and also
    ###log in the MongoDB database the timestamp that it was accessed.
    ###'''
    
    ###rand = random.randint(0, 152)
    
    
    ###return


if __name__ == '__main__':
    db = client.csci2963
    collection = db.definitions
    size = collection.count()
    
    ##Fetch all records
    all_records(db)
    
    ##Fetch one record
    #rand = random.randint(0, 152)
    rand = 1
    randomWord = find_by_index(db, rand)
    update_with_date(db, randomWord["word"])
    rword = find_by_index(db, rand)
    print rword
    ##print random_word_requester()
