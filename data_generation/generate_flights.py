import mysql.connector
import random
from datetime import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="airline_db"
)

cursor = conn.cursor()

cursor.execute("SELECT MAX(FLIGHT_NO) FROM FLIGHT")
max_flight = cursor.fetchone()[0]

start_flight = max_flight + 1
end_flight = start_flight + 20

cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Kolkata",
    "Pune"
]

airlines = [101, 102]

for flight_no in range(start_flight, end_flight):

    source = random.choice(cities)

    destination = random.choice(cities)
    while destination == source:
        destination = random.choice(cities)

    airline_id = random.choice(airlines)

    dep_hour = random.randint(5, 20)
    dep_time = f"{dep_hour:02d}:00:00"

    arr_hour = dep_hour + random.randint(1, 4)
    arr_time = f"{arr_hour:02d}:00:00"

    query = """
    INSERT INTO FLIGHT
    (FLIGHT_NO, SOURCE, DESTINATION, DEP_TIME, ARR_TIME, AIRLINE_ID)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        flight_no,
        source,
        destination,
        dep_time,
        arr_time,
        airline_id
    )

    cursor.execute(query, values)

conn.commit()

print(f"{end_flight - start_flight} flights inserted successfully!")

cursor.close()
conn.close()