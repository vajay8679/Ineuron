-- Adminer 4.8.1 MySQL 8.0.34-0ubuntu0.20.04.1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `Persons`;
CREATE TABLE `Persons` (
  `PersonID` int DEFAULT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Persons` (`PersonID`, `LastName`, `FirstName`, `Address`, `City`) VALUES
(1,	'Kumar',	'jay',	'indore',	'UP'),
(2,	'Verma',	'Ajay',	'Bhopa',	'MP'),
(3,	'Jaiswal',	'Ravi',	'CHW',	'MP'),
(4,	'Veer',	'Raj',	'indore',	'UP'),
(5,	'Ram',	'Kumar',	'Surat',	'GJ'),
(5,	'AA',	'BB',	'Indore',	'MP'),
(6,	'AA1',	'BB1',	'Indore',	'MP'),
(7,	'AA2',	'BB2',	'Bhopal',	'UP'),
(3,	'AA3',	'BB3',	'Indore',	'MP'),
(6,	'AA4',	'BB4',	'Surat',	'GJ'),
(9,	'AA5',	'BB5',	'Bhopal',	'UP');

-- 2023-08-30 03:49:45
