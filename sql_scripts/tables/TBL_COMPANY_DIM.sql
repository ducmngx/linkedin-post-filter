DROP TABLE IF EXISTS company_dimension;

CREATE TABLE IF NOT EXISTS company_dimension (
    companyID VARCHAR(30) NOT NULL,
    cName VARCHAR(100) NOT NULL,
    cHQAddress VARCHAR(50) NOT NULL,
    cHQZipcode INT NOT NULL,
    cURL VARCHAR(100) NULL,
    cField VARCHAR(50) NULL,
    PRIMARY KEY (companyID)
);