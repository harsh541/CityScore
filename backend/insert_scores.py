import sqlite3
from datetime import datetime
from calculate_scores import *
from sqlite3 import Error



def create_connection(db_file):
  try:
    conn = sqlite3.connect(db_file)
    return conn
  except Error as e:
    print(e)
  return None


def insert_topic_data(conn, data):
  """
    Create a new data row
    :param conn:
    :param task:
    :return:
  """
  sql = ''' INSERT INTO score_data(date, topic, day, month, year) VALUES(?, ?, ?, ?, ?) '''
  curr = conn.cursor()
  curr.execute(sql, data)
  return curr.lastrowid

def delete_all_rows(conn):
  sql = ''' DELETE FROM score_data '''
  curr = conn.cursor()
  curr.execute(sql)


def main():
  database = "scores.db"
  today = datetime.now().strftime("%m-%d-%Y")
  conn = create_connection(database)
  with conn:
    delete_all_rows(conn)

    (pothole_topic, pothole_day, pothole_month, pothole_year) = pothole_scores()
    (trash_topic, trash_day, trash_month, trash_year) = trash_scores()
    (street_topic, street_day, street_month, street_year) = street_light_scores()
    (graffiti_topic, graffiti_day, graffiti_month, graffiti_year) = graffiti_scores()
    (other_topic, other_day, other_month, other_year) = other_scores()

    pothole_row = (today, pothole_topic, pothole_day, pothole_month, pothole_year)
    trash_row = (today, trash_topic, trash_day, trash_month, trash_year)
    street_row =(today, street_topic, street_day, street_month, street_year)
    graffiti_row = (today, graffiti_topic, graffiti_day, graffiti_month, graffiti_year)
    other_row = (today, other_topic, other_day, other_month, other_year)

    # insert row
    insert_topic_data(conn, pothole_row)
    insert_topic_data(conn, trash_row)
    insert_topic_data(conn, street_row)
    insert_topic_data(conn, graffiti_row)
    insert_topic_data(conn, other_row)



if __name__ == '__main__':
  main()