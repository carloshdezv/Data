// AUDIT QUERIES

// Sorting top 5 post codes (ascending)

db.mexico1.aggregate([{$match:{"address.postcode" : {$exists: true }}},
                {$group:{"_id":"$address.postcode",
                           "count":{$sum:1}}},
                {$sort:{"_id":1}},
                {"$limit":5}])                

// Sorting top 10 post codes (descending)  

db.mexico.aggregate([{$match:{"address.postcode" : {$exists: true }}},
                {$group:{"_id":"$address.postcode",
                           "count":{$sum:1}}},
                {$sort:{"_id":-1}},
                {"$limit":10}])

// List of Operators (ascending)

db.mexico.aggregate([{$match:{"operator" : {$exists: true }}},
                        {"$group":{"_id":"$operator",
                        "count":{"$sum":1}}},
                        {$sort:{"count":-1}}
                        ])

// QUERIES FOR ANALYSIS

//Number of documents
                
db.mexico.find().count()

//Number of nodes

db.mexico.find({"type":"node"}).count()

//Number of ways

db.mexico.find({"type":"way"}).count()

// Number of unique users

db.mexico.distinct("created.user").length

// Top 3 contributing users

db.mexico.aggregate([{$group:{"_id":"$created.user",
                      "count":{$sum:1}}},
                      {$sort:{"count":-1}},
                      {"$limit":3}])

// Top 10 amenities

db.mexico.aggregate([{"$match":{"amenity":{"$exists":1}}},
                     {"$group":{"_id":"$amenity",
                    "count":{"$sum":1}}},
                    {"$sort":{"count":-1}},
                    {"$limit":10}])

// Top 5 Coffee house types
               
db.mexico.aggregate([{"$match":{"cuisine":{"$exists":1}, "amenity":"cafe"}}, 
                     {"$group":{"_id":"$cuisine","count":{"$sum":1}}},
                     {"$sort":{"count":-1}},
                     {"$limit":5}])

// Top 3 Banks

db.mexico.aggregate([{"$match":{"operator":{"$exists":1},"amenity":"bank"}},
                        {$group:{"_id":"$operator",
                        "count":{$sum:1}}}, 
                        {$sort:{"count":-1}}, 
                        {"$limit":3}])      
