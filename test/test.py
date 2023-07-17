import os, sys
sys.path.insert(0, os.path.abspath("."))
import lib.utils as utils
from lib.clsMySQLDB import clsMySqlDatabase

if __name__ == "__main__":
    # Execute the main function which starts the whole pipeline
    
    myDB = clsMySqlDatabase()

    myDB.start_connection()

    # query = "INSERT INTO company_dimension VALUES (124, \"Meta\", \"CA\", \"www.meta.com\", \"tech\");"

    # myDB.run_query(query)

    get_query = "SELECT * FROM company_dimension;"
    data = myDB.get_data(get_query)

    for da in data:
        print(da)

    myDB.end_connection()
