CREATE TABLE IF NOT EXISTS company_dimension {
    companyID INT NOT NULL,
    cName VARCHAR(20) NOT NULL,
    cHQLocation VARCHAR(50) NOT NULL,
    cWebsite VARCHAR(100) NULL,
    cField VARCHAR(50) NULL,
    PRIMARY KEY (companyID)
}