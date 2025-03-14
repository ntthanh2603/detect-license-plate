-- create database --
CREATE DATABASE DBForBOT;

-- backup database --
/*
BACKUP DATABASE DBForBOT
TO DISK = 'E:\My Drive\road_toll_station_project'
WITH DIFFERENTIAL;
*/

-- create table Driver --
CREATE TABLE Driver (
	CID int NOT NULL PRIMARY KEY,
	Name varchar(255) NOT NULL,
	Money int DEFAULT 0,
	Password varchar(25) NOT NULL
);

-- create table LicensePlate --
CREATE TABLE LicensePlate (
	LicensePlate varchar(30) NOT NULL PRIMARY KEY,
	VehicleParameters varchar(255) NOT NULL,
	CID_ID int NOT NULL FOREIGN KEY REFERENCES Driver(CID)
);

-- create table RoadTollPlaza --
CREATE TABLE RoadTollPlaza (
	StationCode int NOT NULL PRIMARY KEY,
	NameStation varchar(255) NOT NULL,
	Location varchar(255),
	PasswordSatation int NOT NULL
);

-- create table TransactionHistory --
CREATE TABLE TransactionHistory (
	ThCode int NOT NULL PRIMARY KEY,
	LicensePlate_ID varchar(30) NOT NULL FOREIGN KEY REFERENCES LicensePlate(LicensePlate),
	SationCode_ID int NOT NULL FOREIGN KEY REFERENCES RoadTollPlaza(StationCode),
	Time DATETIME NOT NULL,
	Money int NOT NULL
);

