from connect_database import connect_database


conn = connect_database()

# add members using the database - going off of a my.sql connector
def add_members():
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_member = (105, 'Emma Swan', 28)
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, new_member)
            conn.commit()
            print("New Member added.")

        except:
            print(f"Error.")

        finally:
            cursor.close()
            conn.close()
#add_members()

# add a workout session

def add_workout_session():
    if conn is not None:
        try:
            cursor = conn.cursor()
            n_workout_session = (101, '2024-08-01', 9802)
            query = "INSERT INTO WorkoutSessions (member_id, session_date, session_id) VALUES (%s, %s, %s)"
            cursor.execute(query, n_workout_session)
            conn.commit()
            print("New Workout Session has been added.")

        except:
            print("Error in updating workout session")

        finally:
            cursor.close()
            conn.close()
#add_workout_session()


# update member information, using member 101, Jane Doe
def update_member_age():
    if conn is not None:
        try:
            cursor = conn.cursor()
            updating_member = (22, 304)

            query = "UPDATE Members SET age = %s where id = %s"

            cursor.execute(query, updating_member)
            conn.commit()
            print("Member's age updated.")

        except:
            print("Error updating Member age")
                    
        finally:
            cursor.close()
            conn.close()
#update_member_age()

# delete a workout session

def delete_workout_session():
    if conn is not None:
        try:
            cursor = conn.cursor()
            delete_session = (5673)
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            conn.commit()
            print(f"Workout {delete_session} was deleted.")

        except:
            print("Error deleting workout session.")

        finally:
            cursor.close()
            conn.close()
#delete_workout_session()

#task 1: SQL Between Usages

def get_members_in_age_range(start_age, end_age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))
            print(f"Members between {start_age} years old and {end_age} years old: ")
            for member in cursor.fetchall():
                print(member)
        except:
            print(f"Error.")
        finally:
            cursor.close()
            conn.close()
get_members_in_age_range(25, 30)