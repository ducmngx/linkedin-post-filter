-- Active: 1687149754613@@127.0.0.1@3306@LinkedInDB
INSERT INTO company_dimension
VALUES (123, "GoogleX", "DC", "www.googlex.com", "tech");
-- SELECT *
-- FROM company_dimension;
-- DROP PROCEDURE IF EXISTS UPDATEDATETIME;

-- CREATE PROCEDURE UPDATEDATETIME(
-- 	IN SERVICE_DATE DATE,
-- 	IN SERVICE_WEEK VARCHAR(50),
-- 	IN SERVICE_YEAR INT,
-- 	IN SERVICE_YEARMONTH DATE,
-- 	IN SERVICE_QUARTER INT
-- ) BEGIN
-- INSERT INTO
-- 	datetime_dimension
-- VALUES
-- 	(
-- 		service_date,
-- 		service_week,
-- 		service_year,
-- 		service_yearmonth,
-- 		service_quarter
-- 	);
-- END

SELECT User FROM mysql.user;
