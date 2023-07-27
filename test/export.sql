-- Active: 1687149754613@@127.0.0.1@3306@LinkedInDB
select * from company_dimension;

SELECT 
   *
FROM
    `company_dimension`
INTO OUTFILE 'company_dimension.csv' 
FIELDS ENCLOSED BY '\"' 
TERMINATED BY ';' 
ESCAPED BY '\"' 
LINES TERMINATED BY '\r\n';