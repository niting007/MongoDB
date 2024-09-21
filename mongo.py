# Importing the 'pymongo' module for MongoDB interaction
import pymongo

# Try to create a MongoDB client and connect to the server
try:
    # Creating a MongoClient to connect to the local MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Selecting a specific database named 'your_database_name'
    database = client["nitin_first"]

    # Printing a message indicating a successful connection
    print("Connected to MongoDB")

except Exception as e:
    # Handling exceptions and printing an error message if connection fails
    print(f"Error: {e}")


# Try to create a 'students' collection within the selected database
try:
    # Creating a collection named 'students' within the selected database
    collection = database["tutorials"]

    # Printing a message indicating a successful collection creation
    print("Collection 'tutorials' created successfully")

except Exception as e:
    # Handling exceptions and printing an error message if collection creation fails
    print(f"Error: {e}")


try:
        # Creating a dictionary with student details
        data = {
            '_id': 'student.sid',
            'username': 'student.username',
            'email': 'student.email',
            'year': 'student.year',
            'department': 'student.department'
        }

        # Inserting the student data into the 'students' collection and obtaining the inserted ID
        sid = collection.insert_one(data).inserted_id

        # Printing a message indicating the successful insertion of data with the obtained ID
        print(f"Data inserted with ID: {sid}")
except Exception as e:
        # Handling exceptions and printing an error message if data insertion fails
        print(f"Error: {e}")


# fetch all students' data from the 'students' collection

try:
    # Querying the 'students' collection to find all data
    data = collection.find()
    print(data)
except Exception as e:
        # Handling exceptions and printing an error message if data insertion fails
        print(f"Error: {e}")    


# Method to update a specific student's data based on student ID
try:
    # Creating a dictionary with updated student details
    data = {
        'username': "Nitin",
        'email': "nitin.gmail.com",
        'year': "1099",
        'department': "computer"
    }
    # Updating the student data in the 'students' collection
    collection.update_one({'_id': 'student.sid'}, {"$set": data})        
except Exception as e:
        # Handling exceptions and printing an error message if data insertion fails
        print(f"Error: {e}")   

# Method to delete a specific student's data based on student ID
try:
    # Deleting a student's data from the 'students' collection based on student ID
    collection.delete_one({'_id': 'student.sid'})       
except Exception as e:
        # Handling exceptions and printing an error message if data insertion fails
        print(f"Error: {e}")    

finally:
    # Close the MongoDB client if it was initialized
    if client is not None:
        client.close()
        print("Connection closed.")