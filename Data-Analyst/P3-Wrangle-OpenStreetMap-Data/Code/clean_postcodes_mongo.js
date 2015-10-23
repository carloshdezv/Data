// QUERIES FOR CLEANING POSTCODES

// Update "01001" to “01000”

db.mexico.update(
   {"address.postcode": "01001"},
   {
     $set: {
     "address.postcode": "01000"
    }
   }
)

// Update "57745" to “57740”

db.mexico.update(
   {"address.postcode": "57745"},
   {
     $set: {
     "address.postcode": "57740"
    }
   }
)

// Remove document with postcode “62510”

db.mexico.remove( { "address.postcode" : "62510" }, 1 )
// Remove document with postcode “62515”

db.mexico.remove( { "address.postcode" : "62515" }, 1 )

// Remove document with postcode “62523”

db.mexico.remove( { "address.postcode" : "62523" }, 1 )

// Update "C.P. 03810" to “03810”

db.mexico.update(
   {"address.postcode": "C.P. 03810"},
   {
     $set: {
     "address.postcode": "03810"
    }
   }
)

// Update "MEX 11520 Ciudad de México, D.F., Miguel Hidalgo, Granada" to “11520”

db.mexico.update(
   {"address.postcode": "MEX 11520 Ciudad de México, D.F., Miguel Hidalgo, Granada"},
   {
     $set: {
     "address.postcode": "11520"
    }
   }
)

// Update "MEX 11530 Mexico, D.F., Col. Los Morales, Sección Alameda" to “11530”

db.mexico.update(
   {"address.postcode": "MEX 11530 Mexico, D.F., Col. Los Morales, Sección Alameda"},
   {
     $set: {
     "address.postcode": "11530"
    }
   }
)

// Update "México, D.F., Polanco" to “11550”

db.mexico.update(
   {"address.postcode": "México, D.F., Polanco"},
   {
     $set: {
     "address.postcode": "11550"
    }
   }
)
