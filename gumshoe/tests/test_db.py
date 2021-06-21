import logging
from datetime import datetime
import sqlite3
from sqlite3 import Error
import os

database = os.path.join(os.path.dirname(__file__), "../database/test_gumshoe.db")
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), "../logs/app.log"), filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Database:

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_into_table(self, conn, insert_into_table_sql):
        """ insert into table from the insert_sql statements
        :param conn: Connection object
        :param insert_into_table_sql: a INSERT statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(insert_into_table_sql)
            conn.commit()

        except Error as e:
            print(e)

    def test_setup(self):
        sql_create_habits_table = """ CREATE TABLE IF NOT EXISTS habits (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            name text NOT NULL UNIQUE,
                                            quota integer NOT NULL,
                                            period text NOT NULL,
                                            created_at text NOT NULL
                                     ); """

        sql_create_activity_table = """CREATE TABLE IF NOT EXISTS activity (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        habit_id integer NOT NULL,
                                        created_at text NOT NULL,
                                        FOREIGN KEY (habit_id) REFERENCES habits (id)
                                    );"""


        sql_insert_into_habits = """INSERT INTO "habits" ("name", "quota", "period", "created_at")
                                    VALUES ("habit1", 1, "daily", date('now', '-20 days')),("habit2", 4, "weekly", date('now', '-60 days')),
                                    ("habit3", 2, "daily", date('now', '-20 days')),("habit4", 8, "monthly", date('now', '-180 days'));
                                    """

        sql_insert_into_activity_habit1 = """INSERT INTO "activity" ("habit_id", "created_at")
                                            VALUES (1, strftime('%Y-%m-%d %H:%M',date('now'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-1 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-2 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-4 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-5 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-6 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-7 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-9 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-10 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-11 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-12 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-13 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-14 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-15 days'))),
                                            (1, strftime('%Y-%m-%d %H:%M',date('now', '-16 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-17 days')));
                                            """

        sql_insert_into_activity_habit2 = """INSERT INTO "activity" ("habit_id", "created_at")
                                            VALUES (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-10 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-11 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-12 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-13 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-14 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-15 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-16 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-21 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-22 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-23 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-24 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-25 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-30 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-31 days'))),
                                            (2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-32 days'))),(2, strftime('%Y-%m-%d %H:%M',date('now', 'weekday 0', '-33 days')));
                                            """

        sql_insert_into_activity_habit3 = """INSERT INTO "activity" ("habit_id", "created_at")
                                            VALUES (3, strftime('%Y-%m-%d %H:%M',date('now'))),(3, strftime('%Y-%m-%d %H:%M',date('now'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-2 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-2 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-3 days'))),(1, strftime('%Y-%m-%d %H:%M',date('now', '-3 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-4 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-4 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-5 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-5 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-6 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-6 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-8 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-8 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-9 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-9 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-10 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-10 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-11 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-11 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-12 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-12 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-13 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-13 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-14 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-14 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-15 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-15 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-16 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-16 days'))),
                                            (3, strftime('%Y-%m-%d %H:%M',date('now', '-17 days'))),(3, strftime('%Y-%m-%d %H:%M',date('now', '-17 days')));
                                            """

        sql_insert_into_activity_habit4 = """INSERT INTO "activity" ("habit_id", "created_at")
                                            VALUES (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-10 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-12 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-13 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-14 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-20 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-21 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-22 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-23 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-10 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-11 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-12 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-13 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-14 days'))),(4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-15 days'))),
                                            (4, strftime('%Y-%m-%d %H:%M',date('now', 'start of month', '-1 month', '-16 days')));
                                            """

        # create a database connection
        conn = self.create_connection(database)

        # create tables
        if conn is not None:
            try:
                # create habits table
                self.create_table(conn, sql_create_habits_table)

                # create activity table
                self.create_table(conn, sql_create_activity_table)

                #create habits
                self.insert_into_table(conn, sql_insert_into_habits)

                # create activities
                self.insert_into_table(conn, sql_insert_into_activity_habit1)
                self.insert_into_table(conn, sql_insert_into_activity_habit2)
                self.insert_into_table(conn, sql_insert_into_activity_habit3)
                self.insert_into_table(conn, sql_insert_into_activity_habit4)
                return True
            except Exception as e:
                return False

        else:
            print("Error! cannot create the database connection.")

db = Database()
assert db.test_setup()
