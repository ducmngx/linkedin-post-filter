import http.client 
import requests
import json
import os, sys
from dotenv import load_dotenv
from linkedin_api import Linkedin
import json
import lib.utils as utils
from lib.utils import JOB_TITLE_OF_INTEREST

load_dotenv()

class LinkedInCrawler:

    def __init__(self):
        self.user = os.getenv("LINKEDIN_USER")
        self.password = os.getenv("LINKEDIN_PASSWORD")
        self.linkedin = Linkedin(self.user, self.password)

    def getProfile(self, profileName):
        profile = self.linkedin.get_profile(profileName)

        return profile
    
    def getCompany(self, companyID):
        thisCompany = self.linkedin.get_company(companyID)

        return thisCompany
    
    def getJobPost(self, jobPostID):
        searchExactJob = self.linkedin.get_job(jobPostID)

        return searchExactJob
    
    def getJobSearch(self, jobTitle=JOB_TITLE_OF_INTEREST):
        jobqueries = []
        for keyword in JOB_TITLE_OF_INTEREST:
            searchJob = self.linkedin.search_jobs(keywords=keyword)
            jobqueries.append(searchJob)

        return jobqueries
    
    def extractCompanyInfo(self, query):
        # cName
        cName = query['name']
        
        # company field
        cField = query['companyIndustries'][0]['localizedName']
        # cFieldID = query['companyIndustries'][0]['entityUrn'].split(':')[-1]
        
        # cURL
        try:
            cURL = query['companyPageUrl']
        except:
            cURL = "n/a"
        
        try:
            cHQLocation = query['headquarter']
            try:
                cHQAddress = cHQLocation['line1'] + ", " \
                            + cHQLocation['city'] + ", " + cHQLocation['geographicArea'] + ", " + cHQLocation['country']
            except:
                cHQAddress = "n/a"

            try:
                cHQPostal = cHQLocation['postalCode']
            except:
                cHQPostal = 0
        except:
            cHQAddress = "n/a"
            cHQPostal = 0
        
        return cName, cField, cURL, cHQAddress, cHQPostal
    
    def extractJobInfoFromQuery(self, query):
        jobPostingID = query['dashEntityUrn'].split(":")[-1]
        companyID = query['companyDetails']['company'].split(':')[-1]
        jobLocation = query['formattedLocation']
        remoteOpt = query['workRemoteAllowed']
        
        return jobPostingID, companyID, jobLocation, remoteOpt

    def extractJobDetail(self, query):
        jobState = query['jobState']
        jobDesc = query['description']['text']
        jobTitle = query['title']
        
        # apply method
        try:
            unifyAble = query['applyMethod']['com.linkedin.voyager.jobs.ComplexOnsiteApply']['unifyApplyEnabled']
        except:
            unifyAble = 'n/a'
        
        try:
            applyLink = query['applyMethod']['com.linkedin.voyager.jobs.ComplexOnsiteApply']['easyApplyUrl']
        except:
            applyLink = 'n/a'
        
        return jobState, jobTitle, jobDesc, unifyAble, applyLink

