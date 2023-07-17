import os, sys
sys.path.insert(0, os.path.abspath("."))
import lib.utils as utils
from lib.clsMySQLDB import clsMySqlDatabase

if __name__ == "__main__":
    # Execute the main function which starts the whole pipeline
    
    myDB = clsMySqlDatabase()

    myDB.start_connection()


    myDB.end_connection()
