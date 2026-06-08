# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     database="airline_db"
# )

# print("Connected Successfully!")

# conn.close()

from faker import Faker
import mysql.connector
import random

fake = Faker("en_IN")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="airline_db"
)

cursor = conn.cursor()
cursor.execute("SELECT MAX(USER_ID) FROM USERS")
max_id = cursor.fetchone()[0]

start_id = max_id + 1
end_id = start_id + 50

for user_id in range(start_id, end_id): # Generates 5 users

    gender = random.choice(["Male", "Female"])

    first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
    last_name = fake.last_name()

    dob = fake.date_of_birth(minimum_age=18, maximum_age=60)

    city = fake.city()
    state = fake.state()
    pin_code = fake.postcode()

    query = """
    INSERT INTO USERS
    (USER_ID, F_NAME, M_NAME, L_NAME, DOB, GENDER, CITY, STATE, PIN_CODE)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        user_id,
        first_name,
        None,
        last_name,
        dob,
        gender,
        city,
        state,
        pin_code
    )

    cursor.execute(query, values)

conn.commit()

print("5 users inserted successfully!")

cursor.close()
conn.close()