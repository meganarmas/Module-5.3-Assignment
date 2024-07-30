from connect_database import connect_database
import Error

conn = connect_database

# add members using the database - going off of a my.sql connector

def add_members(id, name, age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_member = ("Michael Art", 105, 24)

            query = "INSERT INTO Members (name, id, age)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New Member added.")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()



# add a workout session

def add_workout_session(member_id, date, duration_minutes, calories_burned):
     if conn is not None:
        try:
            cursor = conn.cursor()
            n_workout_session = (105, 2024-08-01, 15, 50)

            query = "INSERT INTO WorkoutSessions"

            cursor.execute(query, n_workout_session)
            conn.commit()
            print("New Workout Session has been added.")

        except Error as e:
            print(f"Error in updating workout session: {e}")

        finally:
            cursor.close()
            conn.close()



# update member information, using member 101, Jane Doe
def update_member_age(member_id, age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            n_workout_session = (105, 2024-08-01, 15, 50)

            query = "INSERT INTO WorkoutSessions"

            cursor.execute(query, n_workout_session)
            conn.commit()
            print(f"Member {member_id} age updated.")

        except Error as e:
            print(f"Error updating Member age: {e}")
                    
        finally:
            cursor.close()
            conn.close()

# delete a workout session

def delete_workout_session(session_id):
     if conn is not None:
        try:
            cursor = conn.cursor()
            n_workout_session = (105, 2024-08-01, 15, 50)

            query = "INSERT INTO WorkoutSessions"

            cursor.execute(query, n_workout_session)
            conn.commit()
            print(f"Workout {session_id} deleted.")

        except Error as e:
            print(f"Error deleting workout session: {e}")

        finally:
            cursor.close()
            conn.close()
