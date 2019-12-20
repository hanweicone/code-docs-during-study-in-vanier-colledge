-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 31, 2019 at 05:45 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qzss`
SET NAMES UTF8;
DROP DATABASE IF EXISTS qzss;
CREATE DATABASE qzss CHARSET=UTF8;
USE qzss;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(2351, 'admin', 'e10adc3949ba59abbe56e057f20f883e');

-- --------------------------------------------------------

--
-- Table structure for table `advert`
--

CREATE TABLE `advert` (
  `id` int(10) UNSIGNED NOT NULL,
  `img` varchar(100) NOT NULL,
  `pos` tinyint(3) UNSIGNED NOT NULL,
  `url` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL,
  `writer` varchar(50) NOT NULL,
  `img` varchar(100) NOT NULL,
  `info` mediumtext NOT NULL,
  `oldprice` float(8,2) UNSIGNED NOT NULL,
  `nowprice` float(8,2) UNSIGNED NOT NULL,
  `class_id` int(10) UNSIGNED NOT NULL,
  `stock` int(10) UNSIGNED NOT NULL,
  `sales` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `supplier` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `shelf` tinyint(3) UNSIGNED NOT NULL,
  `recommend` tinyint(3) UNSIGNED NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `name`, `writer`, `img`, `info`, `oldprice`, `nowprice`, `class_id`, `stock`, `sales`, `supplier`, `shelf`, `recommend`) VALUES
(3, 'western economics', 'Frances', '1572460281719339426.jpg', 'economics', 60.00, 50.00, 8, 20, 0, 0, 1, 0),
(4, 'Art History', 'Jack', '1572460387507027271.jpg', 'history of arts', 235.00, 150.00, 10, 10, 0, 0, 1, 1),
(5, 'Public Tax Management', 'Kookto', '15724606041395549144.jpg', 'tax management', 50.00, 40.00, 8, 33, 0, 0, 1, 0),
(6, 'Capital Expense', 'uhame', '15724606842098775132.jpg', 'capital', 66.00, 55.00, 1, 7, 0, 0, 1, 0),
(7, 'How To Find Job', 'Jim', '1572460745848194390.JPG', 'job', 77.00, 66.00, 8, 22, 0, 0, 1, 1),
(8, 'Principles', 'moka', '15724608891651228209.JPG', 'priciple', 67.00, 56.00, 8, 17, 0, 0, 1, 1),
(9, 'Wolf Tolem', 'KaiHua', '15724609691694508160.jpg', 'fiction', 55.00, 33.00, 3, 67, 0, 0, 1, 1),
(10, 'Revolution of China', 'weihuazhang', '1572461051223791310.JPG', 'china', 57.00, 35.00, 8, 45, 0, 0, 1, 0),
(11, 'Ferryman', 'Cole', '1572461164636107869.JPG', 'fiction', 176.00, 45.00, 3, 45, 0, 0, 1, 0),
(12, 'Learn Tao', 'LiDan', '1572461268620891549.JPG', 'laozi', 78.00, 66.00, 3, 57, 0, 0, 1, 1),
(13, 'Food Culture ', 'Huanwei', '1572461339436926154.JPG', 'food', 67.00, 33.00, 5, 10, 0, 0, 1, 1),
(14, 'Future', 'Bob Dilian', '1572461405928950126.JPG', 'business', 45.00, 34.00, 8, 11, 0, 0, 1, 1),
(15, 'Relative', 'Ayshuwa', '15724614681099892727.JPG', 'sicence', 45.00, 37.00, 1, 11, 0, 0, 1, 1),
(16, ' Do God use dice ?', 'Caotianyuan', '1572461561636629665.JPG', 'sicence', 77.00, 67.00, 1, 12, 0, 0, 1, 1),
(17, 'Dinosaur Kingdom', 'Cerirs', '15724616831118385969.JPG', 'children', 55.00, 50.00, 1, 12, 0, 0, 1, 1),
(18, 'Never ', 'Kinle', '1572461792251192849.JPG', 'success', 67.00, 55.00, 8, 11, 0, 0, 1, 1),
(19, 'Data Structure', 'Kuban', '1572461890673277384.JPG', '', 88.00, 77.00, 10, 13, 0, 0, 1, 1),
(20, 'Think', 'Joe', '15724619821324287444.JPG', 'sdf', 34.00, 23.00, 7, 33, 0, 0, 1, 1),
(21, 'Math', 'Liyongle', '1572462428279045220.JPG', 'math', 44.00, 20.00, 6, 1, 0, 2325, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `bookshelf`
--

CREATE TABLE `bookshelf` (
  `id` int(10) UNSIGNED NOT NULL,
  `book_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bookshelf`
--

INSERT INTO `bookshelf` (`id`, `book_id`, `user_id`) VALUES
(1, 20, 2325),
(2, 15, 2326);

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`id`, `name`) VALUES
(1, 'Science Fiction and Fantasy'),
(2, 'Mystery, Thriller and Suspense'),
(3, 'Literature and Fiction'),
(4, 'History'),
(5, 'Cooking, Food & Wine'),
(6, 'children book'),
(7, 'Comics and Graphic Novels'),
(8, 'Business & Investing'),
(9, 'Biographies and Memoirs'),
(10, 'Arts & Photography');

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `content` text,
  `book_id` int(10) UNSIGNED NOT NULL,
  `time` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `indent`
--

CREATE TABLE `indent` (
  `id` int(10) UNSIGNED NOT NULL,
  `code` varchar(50) NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `touch_id` int(10) UNSIGNED NOT NULL,
  `book_id` int(10) UNSIGNED NOT NULL,
  `price` float(8,2) UNSIGNED NOT NULL,
  `num` int(10) UNSIGNED NOT NULL,
  `status_id` int(11) NOT NULL DEFAULT '1',
  `confirm` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `paytype` int(10) UNSIGNED NOT NULL DEFAULT '1',
  `posttype` int(10) UNSIGNED NOT NULL DEFAULT '1',
  `time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `touch`
--

CREATE TABLE `touch` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL,
  `addr` varchar(100) NOT NULL,
  `postcode` varchar(10) NOT NULL,
  `tel` varchar(50) NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(32) NOT NULL,
  `realname` varchar(20) NOT NULL,
  `img` varchar(100) NOT NULL DEFAULT 'moren.gif',
  `sex` tinyint(3) UNSIGNED NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `realname`, `img`, `sex`) VALUES
(2325, 'cone', 'e10adc3949ba59abbe56e057f20f883e', 'rfgerg', '', 0),
(2326, 'hanwei', 'e10adc3949ba59abbe56e057f20f883e', '捍卫', 'moren.gif', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `advert`
--
ALTER TABLE `advert`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookshelf`
--
ALTER TABLE `bookshelf`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `indent`
--
ALTER TABLE `indent`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `touch`
--
ALTER TABLE `touch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2352;

--
-- AUTO_INCREMENT for table `advert`
--
ALTER TABLE `advert`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `bookshelf`
--
ALTER TABLE `bookshelf`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `indent`
--
ALTER TABLE `indent`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `touch`
--
ALTER TABLE `touch`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2327;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
