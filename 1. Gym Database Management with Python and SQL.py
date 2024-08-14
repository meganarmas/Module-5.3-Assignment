from connect_database import connect_database


# add members using the database - going off of a my.sql connector

def add_members():
    conn = connect_database()
    print(conn)
    if conn is not None:
        try:
            print("testing")
            cursor = conn.cursor()
            new_member = ('Emma Swan', 105, 28)

            query = "INSERT INTO Members (name, id, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New Member added.")

        except:
            print(f"Error in adding new member.")
        finally:
            cursor.close()
            conn.close()
add_members()


# add a workout session

def add_workout_session(member_id, date, duration_minutes, calories_burned):
     if conn is not None:
        try:
            cursor = conn.cursor()
            n_workout_session = (105, '2024-08-01', 15, 50)

            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)", (member_id, date, duration_minutes, calories_burned)

            cursor.execute(query, n_workout_session)
            conn.commit()
            print("New Workout Session has been added.")

        except:
            print(f"Error in updating workout session")

        finally:
            cursor.close()
            conn.close()



# update member information, using member 101, Jane Doe
def update_member_age(member_id, age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            updating_member = (304, 22)

            query = "UPDATE Members SET age = %s where id = %s"

            cursor.execute(query, updating_member)
            conn.commit()
            print(f"Member {member_id} age updated.")

        except:
            print(f"Error updating Member age")
                    
        finally:
            cursor.close()
            conn.close()

# delete a workout session

def delete_workout_session(session_id):
     if conn is not None:
        try:
            cursor = conn.cursor()
            delete_session = (4321)

            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"

            cursor.execute(query, delete_session)
            conn.commit()
            print(f"Workout {session_id} deleted.")

        except:
            print(f"Error deleting workout session.")

        finally:
            cursor.close()
            conn.close()


#task 1: SQL Between Usages

def get_members_in_age_range(start_age, end_age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            get_members = (25, 30)

            query = "SELECT age FROM Members BETWEEN %s AND %s"
            cursor.execute(query, start_age, end_age)
            conn.fetchall()
            print(f"Members in age range: {get_members}")

        except:
            print(f"Error.")

        finally:
            cursor.close()
            conn.close()