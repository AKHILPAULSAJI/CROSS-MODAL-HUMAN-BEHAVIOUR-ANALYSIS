-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 29, 2020 at 10:51 AM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hr`
--

-- --------------------------------------------------------

--
-- Table structure for table `pb_candidate_details`
--

CREATE TABLE IF NOT EXISTS `pb_candidate_details` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `college` varchar(100) NOT NULL,
  `resume` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `Stream` varchar(100) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `pb_candidate_details`
--

INSERT INTO `pb_candidate_details` (`c_id`, `name`, `age`, `college`, `resume`, `photo`, `degree`, `experience`, `mobile`, `email`, `Stream`) VALUES
(1, 'gokul vishnu', '45', 'Viswajyothi college of Eng & Tech', 'candidate/Resume/gokul.vishnu587@gmail.com_yadav2014.pdf', 'candidate/Images/gokul.vishnu587@gmail.com__Image.jpeg', 'btech', '12', '7558840004', 'gokul.vishnu587@gmail.com', 'it'),
(2, 'abcd vfad', '23', 'Mar Agustianos College Ramapuram', 'candidate/Resume/aa@gmail.com_yadav2014.pdf', 'candidate/Images/aa@gmail.com__Image.jpeg', 'dvdsfdvdsdgg', '5', '8989898989', 'aa@gmail.com', 'fdg');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
