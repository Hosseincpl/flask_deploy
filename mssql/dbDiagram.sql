USE MASTER
GO

IF DB_ID('PensionInflowDB') > 0
	DROP DATABASE PensionInflowDB
GO

CREATE DATABASE PensionInflowDB
GO

USE PensionInflowDB
GO 

----------------------------------