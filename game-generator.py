import psycopg2
import random

# Connect to PostgreSQL
conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="****",
                        port="****")

cursor = conn.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM games")
result = cursor.fetchall()

# Filter games based on score criteria (> 4)
games3 = [game for game in result if game[2] > 4]

# Randomly select a game from filtered list
if games3:
    random_game = random.choice(games3)
    random_game_name = random_game[1]
    print("Randomly selected game is:", random_game_name)
else:
    print("No games meet the criteria.")

# Close cursor and connection
cursor.close()
conn.close()
