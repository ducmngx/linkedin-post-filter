DROP TABLE IF EXISTS jobPost_facts;
-- Active: 1687149754613@@127.0.0.1@3306@LinkedInDB
CREATE TABLE IF NOT EXISTS jobPost_facts(
    jobPostingID VARCHAR(30) NOT NULL,
    companyID VARCHAR(30) NOT NULL,
    jobTitle VARCHAR(100) NOT NULL,
    workRemoteAllowed BIT NOT NULL,
    jobLocation VARCHAR(50) NOT NULL,
    jobDesc VARCHAR(10000) NULL,
    applyLink VARCHAR(100) NOT NULL,
    jobState BIT NOT NULL,
    openDate DATE NOT NULL,
    closeDate DATE NULL,
    PRIMARY KEY (jobPostingID),
    FOREIGN KEY (companyID) REFERENCES company_dimension (companyID),
    FOREIGN KEY (openDate) REFERENCES datetime_dimension (service_date),
    FOREIGN KEY (closeDate) REFERENCES datetime_dimension (service_date)
);