CREATE TABLE IF NOT EXISTS datetime_dimension(
	service_date DATE NOT NULL,
	service_week VARCHAR(50) NOT NULL,
	service_year INT NOT NULL,
	service_yearmonth DATE NOT NULL,
	service_quarter INT NOT NULL,
	PRIMARY KEY (service_date) 
);
