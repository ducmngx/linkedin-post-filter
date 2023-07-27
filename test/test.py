import os, sys
sys.path.insert(0, os.path.abspath("."))
import lib.utils as utils
from lib.clsMySQLDB import clsMySqlDatabase
from lib.linkedinCrawler import LinkedInCrawler
from datetime import datetime as dt

import http.client 
import requests
import json
from linkedin_api import Linkedin
import json

# credentials should be stored in a different file

# Authenticate using any Linkedin account credentials

if __name__ == "__main__":
    # now = dt.now().date().isoformat()

    # print(dt.now().date().weekday() )

    # db = clsMySqlDatabase()
    # db.start_connection()

    # jobPostingID = '3634164629'
    # query = f"SELECT count(*) FROM (SELECT * FROM `jobPost_facts` WHERE `jobPostingID` = '{jobPostingID}') as tbl;"
    # dt = db.get_data(query)

    # print(dt)

    # print(dt[0][0])

    # print(query)

    # linkedin = LinkedInCrawler()

    # output = linkedin.getJobSearch(jobTitle=["Electrical Engineering", "Designer"])

    # print(output)

    user = os.getenv("LINKEDIN_USER")
    password = os.getenv("LINKEDIN_PASSWORD")
    linkedin = Linkedin(user, password)

    tmp = linkedin.search_jobs(keywords="Cloud Engineer")

    print(tmp)