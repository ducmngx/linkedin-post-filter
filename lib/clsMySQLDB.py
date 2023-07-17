'''
This is an implementation of class clsAbstractDatabase for MySQL Database.
'''
import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import lib.utils as utils 
from datetime import date, datetime, timedelta
from lib.clsAbstractDB import clsAbstractDatabase

load_dotenv()

class clsMySqlDatabase(clsAbstractDatabase):
    def __init__(self):
        """Initialize required params for the class
        """
        self.logger = utils.create_log()
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        # self.port = os.getenv("PORT")
        self.database = os.getenv("DATABASE")
        self.conn = None

    def start_connection(self):
        try:
            self.conn = mysql.connector.connect(user=self.user, password=self.password,
                                    host=self.host,
                                    database=self.database)
            self.logger.info(f"{utils.get_current_datetime()}: MySQL connection is created.")
        except Exception as e:
            self.logger.error(f"{utils.get_current_datetime()}: Error while connecting to MySQL database {e}")

        print("Connection established to MySQL Database: " + self.database)

    def end_connection(self):
        self.conn.close()
        self.logger.info(f"{utils.get_current_datetime()}: MySQL connection is closed.")
        print("Database Session Closed")

    def run_query(self, query: str):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
            self.commit()
            self.logger.info(f"{utils.get_current_datetime()}: Successfully executed query: {query}")
        except Exception as e:
            self.logger.error(f"{utils.get_current_datetime()}: Error while trying to execute query: {query} : {e} ")
        finally:
            cursor.close()

    def get_data(self, query: str):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            self.logger.info(f"{utils.get_current_datetime()}: Successfully fetched data from executing query: {query}")
        except Exception as e:
            self.logger.error(f"{utils.get_current_datetime()}: Error while trying to fetch data from executing query: {query} : {e}")
        finally:
            cursor.close()
        return result

    def get_headers(self, query: str):
        pass

    def combine_headers_and_records_to_df(self, headers: list, records: list) -> pd.DataFrame:
        pass
    
    def reset_table(self, table_name: str):
        """Delete all data from a given table.
        :param table_name: name of the table to be resetted.
        :return:
        """
        query = f'DELETE FROM "{table_name}";'
        self.run_query(query)

    def drop_table(self, table_name: str):
        """Drop all data from a given table.
        :param table_name: name of the table to be dropped.
        :return:
        """
        query = f'DROP TABLE "{table_name}";'
        self.run_query(query)

    def call_procedure(self, procedure_name: str):
        """Call a given procedure.
        :param procedure_name: name of the procedure.
        :return: None
        """
        query = f'CALL {procedure_name};'
        self.run_query(query)
    
    def commit(self):
        """Commit action.
        """
        self.conn.commit()