-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2021 at 05:37 PM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `treatment`
--

-- --------------------------------------------------------

--
-- Table structure for table `casesheet`
--

CREATE TABLE IF NOT EXISTS `casesheet` (
  `pid` varchar(15) NOT NULL,
  `eno` int(11) NOT NULL,
  `problem` varchar(100) NOT NULL,
  `prescription` varchar(100) NOT NULL,
  `drcomment` varchar(100) NOT NULL,
  `drid` varchar(15) NOT NULL,
  `bno` int(11) NOT NULL,
  `edate` date NOT NULL,
  PRIMARY KEY (`pid`,`eno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `casesheet`
--

INSERT INTO `casesheet` (`pid`, `eno`, `problem`, `prescription`, `drcomment`, `drid`, `bno`, `edate`) VALUES
('p10001', 1, 'ggg', 'hhh', 'jjjj', 's10003', 1, '2021-04-10'),
('p10001', 2, 'kkkkkkkkkkkkkkkkkkkkkkk', 'lllllllllllllllllllllllllllllllllllllllllll', 'dddddddddddddddddddddddddddddddddddddd', 's10003', 1, '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE IF NOT EXISTS `complaint` (
  `cmpno` int(5) NOT NULL,
  `pid` varchar(15) DEFAULT NULL,
  `staffid` varchar(15) DEFAULT NULL,
  `complaint` varchar(100) NOT NULL,
  `cdate` date NOT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `rdate` date DEFAULT NULL,
  PRIMARY KEY (`cmpno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`cmpno`, `pid`, `staffid`, `complaint`, `cdate`, `reply`, `rdate`) VALUES
(1, 'p10001', NULL, 'dddd', '2021-04-10', 'Null', '2021-04-10'),
(2, 'p10001', NULL, 'Hellloooo', '2021-04-10', 'Null', '2021-04-10'),
(3, 'p10001', NULL, 'hhhh', '2021-04-10', 'jjjjj', '2021-04-10'),
(4, 'p10001', NULL, 'jjjj', '2021-04-10', 'jjjjj', '2021-04-10'),
(5, NULL, 's10001', 'sssss', '2021-04-10', 'jjjjj', '2021-04-10'),
(6, NULL, 's10001', 'llkkjjjhhhggg', '2021-04-10', 'jjjjj', '2021-04-10'),
(7, NULL, 's10001', 'hai', '2021-04-10', 'kkkkk', '2021-04-10'),
(8, NULL, 's10001', 'good', '2021-04-10', 'ooooo', '2021-04-10'),
(9, 'p10001', NULL, 'Fine', '2021-04-10', 'kkkkk', '2021-04-10'),
(10, 'p10001', NULL, 'Thank you', '2021-04-10', 'kkkkk', '2021-04-10'),
(11, 'p10001', NULL, 'gggg', '2021-04-10', 'tttt', '2021-04-10'),
(12, NULL, 's10001', 'k jj h g f d', '2021-04-10', NULL, NULL),
(13, NULL, 's10004', 'fffff ggggggg', '2021-04-10', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dropdays`
--

CREATE TABLE IF NOT EXISTS `dropdays` (
  `staffid` varchar(15) NOT NULL,
  `opday` varchar(20) NOT NULL,
  `ftime` varchar(10) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `npatient` int(3) NOT NULL,
  PRIMARY KEY (`staffid`,`opday`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dropdays`
--

INSERT INTO `dropdays` (`staffid`, `opday`, `ftime`, `duration`, `npatient`) VALUES
('s10003', 'Sunday', '4:00:Pm', '2-Hrs', 8),
('s10003', 'Wednesday', '10:00:Am', '3-Hrs', 20);

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE IF NOT EXISTS `hospital` (
  `hospid` varchar(15) NOT NULL,
  `location` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `district` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `htype` varchar(15) NOT NULL,
  `regdate` date NOT NULL,
  `nbed` int(4) NOT NULL,
  PRIMARY KEY (`hospid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`hospid`, `location`, `place`, `pin`, `phone`, `district`, `email`, `htype`, `regdate`, `nbed`) VALUES
('H12346', 'Adoor', 'Adoor', '691523', '9911334455', 'Pathanamthitta', 'aaa@gmail.com', 'Taluk Hospital', '2021-04-10', 200);

-- --------------------------------------------------------

--
-- Table structure for table `hosplab`
--

CREATE TABLE IF NOT EXISTS `hosplab` (
  `tname` varchar(30) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  PRIMARY KEY (`tname`,`hospid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hosplab`
--

INSERT INTO `hosplab` (`tname`, `hospid`) VALUES
('aaaaaa', 'H12346'),
('bbbbb', 'H12346');

-- --------------------------------------------------------

--
-- Table structure for table `labmaster`
--

CREATE TABLE IF NOT EXISTS `labmaster` (
  `tname` varchar(50) NOT NULL,
  `ttype` varchar(15) NOT NULL,
  `tcontent` varchar(15) NOT NULL,
  `tduration` int(11) NOT NULL,
  `tdunit` varchar(10) NOT NULL,
  `tresultduration` int(11) NOT NULL,
  `trdunit` varchar(10) NOT NULL,
  PRIMARY KEY (`tname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `labmaster`
--

INSERT INTO `labmaster` (`tname`, `ttype`, `tcontent`, `tduration`, `tdunit`, `tresultduration`, `trdunit`) VALUES
('aaaaaa', 'Internal', 'Blood', 10, 'Min', 2, 'Hrs'),
('bbbbb', 'External', 'Urine', 10, 'Min', 2, 'Hrs');

-- --------------------------------------------------------

--
-- Table structure for table `labtestitems`
--

CREATE TABLE IF NOT EXISTS `labtestitems` (
  `ltestno` int(5) NOT NULL,
  `tname` varchar(30) NOT NULL,
  PRIMARY KEY (`ltestno`,`tname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `labtestitems`
--

INSERT INTO `labtestitems` (`ltestno`, `tname`) VALUES
(1, 'aaaaaa'),
(1, 'bbbbb'),
(2, 'aaaaaa'),
(2, 'bbbbb'),
(3, 'aaaaaa'),
(3, 'bbbbb'),
(4, 'aaaaaa');

-- --------------------------------------------------------

--
-- Table structure for table `labtestmaster`
--

CREATE TABLE IF NOT EXISTS `labtestmaster` (
  `ltestno` int(5) NOT NULL,
  `pid` varchar(15) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `edate` date NOT NULL,
  PRIMARY KEY (`ltestno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `labtestmaster`
--

INSERT INTO `labtestmaster` (`ltestno`, `pid`, `hospid`, `staffid`, `edate`) VALUES
(1, 'p10001', 'H12346', 's10001', '2021-04-10'),
(2, 'p10002', 'H12346', 's10001', '2021-04-10'),
(3, 'p10001', 'H12346', 's10001', '2021-04-10'),
(4, 'p10001', 'H12346', 's10001', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `labtestresult`
--

CREATE TABLE IF NOT EXISTS `labtestresult` (
  `ltestno` int(5) NOT NULL,
  `rfile` varchar(50) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `rdate` date NOT NULL,
  PRIMARY KEY (`ltestno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `labtestresult`
--

INSERT INTO `labtestresult` (`ltestno`, `rfile`, `staffid`, `rdate`) VALUES
(1, '1.png', 's10001', '2021-04-10'),
(2, '2_x575Pwq.png', 's10001', '2021-04-10'),
(3, '2.png', 's10001', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `userid` varchar(15) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`userid`, `password`) VALUES
('admin', 'bbb');

-- --------------------------------------------------------

--
-- Table structure for table `meddamage`
--

CREATE TABLE IF NOT EXISTS `meddamage` (
  `dno` int(11) NOT NULL,
  `medname` varchar(30) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `dqty` int(11) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `ddate` date NOT NULL,
  PRIMARY KEY (`dno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `meddamage`
--

INSERT INTO `meddamage` (`dno`, `medname`, `hospid`, `dqty`, `reason`, `staffid`, `ddate`) VALUES
(1, 'M2233', 'H12346', 3, 'ggg', 's10001', '2021-04-10'),
(2, 'M1122', 'H12346', 1, 'hhhh', 's10001', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `medsalechild`
--

CREATE TABLE IF NOT EXISTS `medsalechild` (
  `sno` int(5) NOT NULL,
  `medname` varchar(30) NOT NULL,
  `qty` int(5) NOT NULL,
  PRIMARY KEY (`sno`,`medname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medsalechild`
--

INSERT INTO `medsalechild` (`sno`, `medname`, `qty`) VALUES
(1, 'M2233', 10),
(2, 'M1122', 20),
(2, 'M2233', 3),
(3, 'M1122', 2),
(3, 'M2233', 3);

-- --------------------------------------------------------

--
-- Table structure for table `medsalemaster`
--

CREATE TABLE IF NOT EXISTS `medsalemaster` (
  `sno` int(5) NOT NULL,
  `pid` varchar(15) NOT NULL,
  `sdate` date NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medsalemaster`
--

INSERT INTO `medsalemaster` (`sno`, `pid`, `sdate`, `staffid`, `hospid`) VALUES
(1, 'p10002', '2021-04-10', 's10001', 'H12346'),
(2, 'p10001', '2021-04-10', 's10001', 'H12346'),
(3, 'p10001', '2021-04-10', 's10001', 'H12346');

-- --------------------------------------------------------

--
-- Table structure for table `medstock`
--

CREATE TABLE IF NOT EXISTS `medstock` (
  `medname` varchar(30) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `cstock` int(11) NOT NULL,
  PRIMARY KEY (`medname`,`hospid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medstock`
--

INSERT INTO `medstock` (`medname`, `hospid`, `cstock`) VALUES
('M1122', 'H12346', 117),
('M2233', 'H12346', 144);

-- --------------------------------------------------------

--
-- Table structure for table `medstockentry`
--

CREATE TABLE IF NOT EXISTS `medstockentry` (
  `eno` int(11) NOT NULL,
  `medname` varchar(30) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `qty` int(11) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `edate` date NOT NULL,
  PRIMARY KEY (`eno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medstockentry`
--

INSERT INTO `medstockentry` (`eno`, `medname`, `hospid`, `qty`, `staffid`, `edate`) VALUES
(1, 'M2233', 'H12346', 100, 's10001', '2021-04-10'),
(2, 'M2233', 'H12346', 50, 's10001', '2021-04-10'),
(3, 'M1122', 'H12346', 100, 's10001', '2021-04-10'),
(4, 'M1122', 'H12346', 100, 's10001', '2021-04-10'),
(5, 'M1122', 'H12346', 100, 's10001', '2021-04-10'),
(6, 'M1122', 'H12346', 10, 's10001', '2021-04-10'),
(7, 'M1122', 'H12346', 10, 's10001', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `opbooking`
--

CREATE TABLE IF NOT EXISTS `opbooking` (
  `bno` int(11) NOT NULL,
  `drid` varchar(15) NOT NULL,
  `bdate` date NOT NULL,
  `tno` int(3) NOT NULL,
  `pid` varchar(15) NOT NULL,
  `cdate` date NOT NULL,
  `staffid` varchar(15) DEFAULT NULL,
  `hospid` varchar(15) NOT NULL,
  PRIMARY KEY (`bno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `opbooking`
--

INSERT INTO `opbooking` (`bno`, `drid`, `bdate`, `tno`, `pid`, `cdate`, `staffid`, `hospid`) VALUES
(1, 'S10003', '2021-06-02', 1, 'p10001', '2021-04-10', 's10003', 'H12346'),
(2, 'S10003', '2021-04-07', 1, 'p10001', '2021-04-07', 's10003', 'H12346');

-- --------------------------------------------------------

--
-- Table structure for table `opcancel`
--

CREATE TABLE IF NOT EXISTS `opcancel` (
  `bno` int(11) NOT NULL,
  `cdate` date NOT NULL,
  `staffid` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`bno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE IF NOT EXISTS `patient` (
  `pid` varchar(15) NOT NULL,
  `name` varchar(20) NOT NULL,
  `hname` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `ph` varchar(13) NOT NULL,
  `district` varchar(20) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `age` int(3) NOT NULL,
  `adharno` varchar(12) NOT NULL,
  `regdate` date NOT NULL,
  `password` varchar(20) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`pid`, `name`, `hname`, `place`, `pin`, `ph`, `district`, `gender`, `age`, `adharno`, `regdate`, `password`, `staffid`, `hospid`) VALUES
('P10001', 'Ram', 'RR House', 'Adoor', '778877', '9988778877', 'Pathanamthitta', 'F', 44, '667786767656', '2021-04-10', 'aaa', 's10001', 'H12346'),
('P10002', 'Arun', 'ggg', 'hhh', '777777', '44556655665', 'Thiruvananthapuram', 'F', 22, '334455667788', '2021-04-10', '44556655665', 's10001', 'H12346'),
('P10003', 'Arun', 'ggg', 'hhh', '777777', '9933445566', 'Thiruvananthapuram', 'F', 22, '334455667788', '2021-04-10', '9933445566', 's10001', 'H12346'),
('P10004', 'Arun', 'ggg', 'hhh', '777777', '9911223311', 'Thiruvananthapuram', 'F', 22, '334455667788', '2021-04-10', '9911223311', 's10001', 'H12346');

-- --------------------------------------------------------

--
-- Table structure for table `pharmacymed`
--

CREATE TABLE IF NOT EXISTS `pharmacymed` (
  `medname` varchar(50) NOT NULL,
  `medtype` varchar(15) NOT NULL,
  `company` varchar(20) NOT NULL,
  `content` varchar(100) NOT NULL,
  `medunit` varchar(10) NOT NULL,
  PRIMARY KEY (`medname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pharmacymed`
--

INSERT INTO `pharmacymed` (`medname`, `medtype`, `company`, `content`, `medunit`) VALUES
('M1122', 'Tab', 'gggg', 'hhhh', 'Mg'),
('M2233', 'Tab', 'uuuuu', 'ggggg', 'Gm');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE IF NOT EXISTS `session` (
  `userid` varchar(15) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `desig` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`userid`, `hospid`, `desig`) VALUES
('s10004', 'H12346', 'Office Staff');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE IF NOT EXISTS `staff` (
  `staffid` varchar(15) NOT NULL,
  `name` varchar(20) NOT NULL,
  `hname` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `ph` varchar(13) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `spl` varchar(20) DEFAULT NULL,
  `qualification` varchar(15) NOT NULL,
  `experience` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staffid`, `name`, `hname`, `place`, `pin`, `ph`, `gender`, `spl`, `qualification`, `experience`, `password`) VALUES
('S10001', 'Ram', 'ggg', 'Adoor', '691523', '9988776655', 'M', NULL, 'SSLC', '2 years', 'aaa'),
('S10002', 'Anu', 'ggg', 'Adoor', '691523', '9988776655', 'F', NULL, 'Plus Two', 'No Exp', 'S10002'),
('S10003', 'Arjun', 'ggggg', 'ffff', '668877', '7788776655', 'F', 'MBBS', 'General', 'jjhjhj', 'S10003'),
('S10004', 'Kiran', 'hhhh', 'jjjj', '888888', '9999965432', 'M', NULL, 'Degree', 'hhhh', 'S10004'),
('S10005', 'Anu Krishnan', 'yyuuyy', 'fffff', '665544', '9988776655', 'F', NULL, 'MLT', 'hhhh', 'S10005');

-- --------------------------------------------------------

--
-- Table structure for table `staffhospital`
--

CREATE TABLE IF NOT EXISTS `staffhospital` (
  `staffid` varchar(15) NOT NULL,
  `wno` int(3) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `regdate` date NOT NULL,
  PRIMARY KEY (`staffid`,`wno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staffhospital`
--

INSERT INTO `staffhospital` (`staffid`, `wno`, `hospid`, `designation`, `regdate`) VALUES
('S10001', 1, 'H12346', 'Pharmacist', '2021-04-10'),
('S10002', 1, 'H12346', 'Pharmacist', '2021-04-10'),
('S10003', 1, 'H12346', 'DMO', '2021-04-10'),
('S10004', 1, 'H12346', 'Office Staff', '2021-04-10'),
('S10005', 1, 'H12346', 'Lab Staff', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `temp`
--

CREATE TABLE IF NOT EXISTS `temp` (
  `itemno` int(11) NOT NULL,
  `tname` varchar(50) NOT NULL,
  PRIMARY KEY (`itemno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `temp1`
--

CREATE TABLE IF NOT EXISTS `temp1` (
  `itemno` int(5) NOT NULL,
  `medname` varchar(30) NOT NULL,
  `qty` int(5) NOT NULL,
  PRIMARY KEY (`itemno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
