import sqlite3, os, logging
from file_handling.file_handling import *
from file_handling.loggers.log_maker import *


class SQL_handler():
    """
    jobs:
        connect to database
        get and update application setting
        fetch store and update info about
            data_classes
                names
                time
                tags
                duration
            tags
                totals in weekly and daily
                names

    """

    def __init__(self, memory=False, schema=None, debug=False):
        self.path = os.path.dirname(__file__)

        self.log = create_logger(__name__, logging.DEBUG, self.path, debug)

        self.conn = None
        self.cursor = None
        if memory:
            self.connect()
        elif schema:
            self.connect(schema+".db")
        else:
            self.log.error("No Database opened")
            raise Exception("NO DATABASE OPENED")

        self.set_cursor()


    def connect(self, name=":memory:"):
        if name == ":memory:":
            self.conn = sqlite3.Connection(name)
            return True
        else:
            file = self.path + os.sep + name
            if not file_exist(self.path, name):
                create_file(self.path, name)

            self.conn = sqlite3.Connection(file)
            return

    def set_cursor(self):
        try:
            self.cursor = self.conn.cursor()
            return True
        except Exception:
            self.log.error("failed to get cursor")
            return False

    def create_database(self, tables, indexes):
        for table in tables:
            self.execute_statement(table)
        for index in indexes:
            self.execute_statement(index)

    def reset_database(self):
        pass

    def make_col_string(self, *collumns):
        """
            collumns = [column_name, sqlite_datatype]
        """
        print(collumns)
        statement = ""
        for col in collumns:
            statement += " ".join(col)
            if col != collumns[-1]:
                statement += ", "

        return statement

    def create_table(self, name, cols):
        return "CREATE TABLE IF NOT EXIST {} ({})".format(name, self.make_col_string(cols))

    def insert(self, name, cols):
        return "INSERT INTO {} ({})".format(name, self.make_col_string(cols))

    def select(self, name, cols):
        return "SELECT {} FROM {}".format(self.make_col_string(cols), name)

    #todo conditions is a bad name for this because it is to be used for creating
    #   conditional statements for where, and for creating the update statement. ie. col1=val1
    def logical_statement(self, *conditions):
        """
            conditions = [column, logical operator, conditional value]
        """
        cons = ''
        try:
            for con in conditions:
                cons += "{}\n".format(" ".join(con))
        except Exception as e:
            self.log.exception("could not create logical statement. prefix: {} . conditiosn: {}".format(conditions) )
            return False
        return cons

    def where(self, *conditions):
        """
            conditions = [column, logical operator, conditional value]
        """
        cons = ''
        try:
            for con in conditions:
                cons += "WHERE {}\n".format(" ".join(con))
        except Exception:
            self.log.exception("could not create logical statement. prefix: {} . conditiosn: {}".format(conditions))
            return False
        return cons

    def update(self, table, colvals, condtions):
        return "UPDATE {} SET \n{}{}".format(table, self.logical_statement(*colvals), self.where(*condtions))

    def delete(self, table, conditions):
        return "DELETE FROM {} {}".format(table, self.where(*conditions))

    def get_table_info(self, table):
        pass

    def get_cols(self, table_info):
        """make list of columns for given table for display or creating sql statement"""
        pass

    def execute_statement(self, sql, data= None, fetch=False):
        try:
            if data:
                self.cursor.execute(sql, data)
            else:
                self.cursor.execute(sql)
            if fetch:
                ret_val = self.cursor.fetchall()

                if not ret_val:
                    logging.debug('retrieved nothing')
                return ret_val
            self.log.debug(f"""sql: {sql}
                            data: {data},
                            fetch: {fetch}""")
            self.conn.commit()
        except:
            self.log.error("""
            sql problem: sql: {}
            data: {}
            fetch: {}
            error: {}""".format(sql, data, fetch))
