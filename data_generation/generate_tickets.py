import mysql.connector
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="airline_db"
)

cursor = conn.cursor()

# Get current max PNR
cursor.execute("SELECT MAX(PNR_NO) FROM TICKET")
max_pnr = cursor.fetchone()[0]

start_pnr = max_pnr + 1
end_pnr = start_pnr + 200

# Get available users
cursor.execute("SELECT USER_ID FROM USERS")
users = [row[0] for row in cursor.fetchall()]

# Get available flights
cursor.execute("SELECT FLIGHT_NO FROM FLIGHT")
flights = [row[0] for row in cursor.fetchall()]

for pnr in range(start_pnr, end_pnr):

    user_id = random.choice(users)

    flight_no = random.choice(flights)

    # 70% Economy, 30% Business
    class_id = random.choices(
        [1, 2],
        weights=[70, 30]
    )[0]

    seat_row = random.choice(["A", "B", "C", "D", "E", "F"])
    seat_no = f"{seat_row}{random.randint(1,30)}"

    # 80% booked, 20% cancelled
    status = random.choices(
        ["BOOKED", "CANCELLED"],
        weights=[80, 20]
    )[0]

    start_date = datetime(2026, 1, 1)
    random_days = random.randint(0, 180)

    ticket_date = start_date + timedelta(days=random_days)

    query = """
    INSERT INTO TICKET
    (PNR_NO, USER_ID, FLIGHT_NO, CLASS_ID, SEAT_NO, DATE_TIME, STATUS)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        pnr,
        user_id,
        flight_no,
        class_id,
        seat_no,
        ticket_date,
        status
    )

    cursor.execute(query, values)

conn.commit()

print(f"{end_pnr - start_pnr} tickets inserted successfully!")

cursor.close()
conn.close()