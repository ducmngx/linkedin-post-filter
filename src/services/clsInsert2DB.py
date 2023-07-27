"""
Class that handles ingesting new data into the database.
"""
from datetime import datetime as dt
import os, sys
sys.path.insert(1, os.path.abspath("."))

from lib.clsMySQLDB import clsMySqlDatabase
from lib.linkedinCrawler import LinkedInCrawler

import lib.utils as utils


class UpdateDatabaseNewData():
    
    def __init__(self):
        self.logger = utils.create_log()
        self.db = self.create_database_connection()
        self.linkedin = LinkedInCrawler()
        self.datetime = dt.now().date()

    def create_database_connection(self):
        """Connect to the database.
        :return: a MySQL database connection.
        """
        db = clsMySqlDatabase()
        db.start_connection()
        return db
    
    def close_database_connection(self):
        """Disconnect to the database.
        """
        self.db.end_connection()

    def update_datetime_table(self):
        service_date = self.datetime
        service_week = self.datetime.isocalendar().week
        service_year = self.datetime.year
        service_yearmonth = self.datetime.month 
        service_quarter = 1 + (service_yearmonth // 3)

        datetime_args = [service_date, service_week, service_year, service_yearmonth, service_quarter]
        self.db.call_procedure('UPDATEDATETIME', datetime_args)

    def checkJobPostExistence(self, jobPostingID):
        query = f"SELECT count(*) FROM (SELECT * FROM `jobPost_facts` WHERE `jobPostingID` = '{jobPostingID}') as tbl;"
        dt = self.db.get_data(query)

        if dt[0][0] == 0:
            return False # not in DB yet
        else:
            return True # already in DB
        
    def checkCompanyExistence(self, companyID):
        query = f"SELECT count(*) FROM (SELECT * FROM `company_dimension` WHERE `companyID` = '{companyID}') as tbl;"
        dt = self.db.get_data(query)

        if dt[0][0] == 0:
            return False # not in DB yet
        else:
            return True # already in DB
     
    def insertion_flow(self):
        # UPDATE TIME BEFORE CRAWLING DATA
        self.update_datetime_table()

        # CRAWLING FLOW
        boards_by_title = self.linkedin.getJobSearch() 
        # self.logger.info(f"{utils.get_current_datetime()}: Successfully crawled boards_by_title")
        
        self.logger.info(f"{utils.get_current_datetime()}: Successfully extracted {len(boards_by_title)} job boards by title")

        # self.logger.info(f"{utils.get_current_datetime()}: Start extracting data for job post")

        num = 1
        for title_board in boards_by_title:
            self.logger.info(f"{utils.get_current_datetime()}: Job board {num} with {len(title_board)} jobs")
            num +=1 

            for board in title_board:
                '''
                This would be a single job post (board)
                '''
                try:
                    jobPostingID, companyID, jobLocation, remoteOpt = self.linkedin.extractJobInfoFromQuery(board)

                    # company
                    print(self.checkCompanyExistence(companyID))
                    if not self.checkCompanyExistence(companyID):
                        thisCompany = self.linkedin.getCompany(companyID)

                        cName, cField, cURL, cHQAddress, cHQPostal = self.linkedin.extractCompanyInfo(thisCompany)

                        # Call UPDATECOMPANY procedure to insert to company table
                        company_args = [companyID, cName, cHQAddress, cHQPostal, cURL, cField]
                        self.db.call_procedure('UPDATECOMPANY', company_args)
                    else:
                        self.logger.info(f"{utils.get_current_datetime()}: Company {companyID} listed is already in database.")

                    # jobPost
                    if not self.checkCompanyExistence(jobPostingID): 
                        thisJob = self.linkedin.getJobPost(jobPostingID)
                        jobState, jobTitle, jobDesc, _, applyLink = self.linkedin.extractJobDetail(thisJob)

                        if jobState == 'LISTED':
                            jobStateBoolean = 1
                        else:
                            jobStateBoolean = 0

                        # self.logger.info(f"{utils.get_current_datetime()}: Incoming jobPostID: {jobPostingID}")
                        string_jobID = str(jobPostingID)
                        fact_args = [string_jobID, companyID, jobTitle, remoteOpt, jobLocation, jobDesc, applyLink, jobStateBoolean, self.datetime, None]
                        
                        # self.logger.info(f"{utils.get_current_datetime()}: jobPostingID {jobPostingID}")
                        self.db.call_procedure('UPDATEJOBPOST', fact_args)
                    else:
                        self.logger.info(f"{utils.get_current_datetime()}: Job {jobPostingID} is already in database.")
                except:
                    self.logger.error(f"{utils.get_current_datetime()}: Failed to read job post")

        self.logger.info(f"{utils.get_current_datetime()}: Successfully extracted data for job post")