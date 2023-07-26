import os, sys
sys.path.insert(0, os.path.abspath("."))
import lib.utils as utils
from lib.clsMySQLDB import clsMySqlDatabase
from datetime import datetime as dt

import http.client 
import requests
import json
from linkedin_api import Linkedin
import json

# credentials should be stored in a different file

# Authenticate using any Linkedin account credentials

if __name__ == "__main__":
    now = dt.now().date().isoformat()

    print(dt.now().date().weekday() )