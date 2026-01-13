import psycopg2

# Establishing connection to the PostgreSQL database
conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="adminadmin",
                        port="5432")

# Creating a cursor object to execute SQL queries
cursor = conn.cursor()

# Executing SQL query to fetch all records from the 'games' table
GAMESSQL = cursor.execute("SELECT * FROM games")

# Fetching all results from the executed SQL query
Result = cursor.fetchall() 

import random

# List to store games with more than 3 occurrences
games3 = []

# Iterating through each game in the results
for games in Result:
    # Checking if the game has more than 3 occurrences
    if games[2] > 3 :
        # Appending the game to the 'games3' list
        games3.append(games)
    
    # Generating a random index within the range of 'games3'
    rand_idx = random.randrange(len(games3))

# Retrieving a random number from the selected games
random_num = games3[rand_idx][1]

# Printing the randomly selected number
print("Random selected Number is : " + str(random_num))
