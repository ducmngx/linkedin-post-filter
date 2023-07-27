import os, sys
sys.path.insert(0, os.path.abspath("."))
from services.clsInsert2DB import UpdateDatabaseNewData

if __name__ == "__main__":
    
    task = UpdateDatabaseNewData()

    task.insertion_flow()

    task.close_database_connection()