-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2020 at 10:17 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `site`
--

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `id` int(10) NOT NULL,
  `title` varchar(120) NOT NULL,
  `date` datetime(6) NOT NULL,
  `content` varchar(2500) NOT NULL,
  `user_id` text NOT NULL,
  `image_file` varchar(50) NOT NULL DEFAULT 'default.jpg',
  `slug` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`id`, `title`, `date`, `content`, `user_id`, `image_file`, `slug`) VALUES
(0, 'cccccc', '2020-10-04 08:13:54.531824', 'cccccccc', 'arjundave234', 'default.jpg', 'arjundave234cccccc'),
(1, 'The titke of the post', '2020-10-03 19:45:09.000000', 'The post content', 'arjundave234', 'WallpaperSunset.jpg', 'arjundave-the-title');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `designation` varchar(50) DEFAULT NULL,
  `email` varchar(60) NOT NULL,
  `image_file` varchar(50) DEFAULT NULL,
  `about` varchar(120) DEFAULT NULL,
  `password` varchar(60) NOT NULL,
  `followers` int(10) NOT NULL,
  `following` int(10) NOT NULL,
  `post_no` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `name`, `designation`, `email`, `image_file`, `about`, `password`, `followers`, `following`, `post_no`) VALUES
(3, 'arjundave234', 'Arjun Dave', 'Web dev', 'abcd@gmail.com', 'WallpaperSunset.jpg', NULL, '$2b$12$6IZow.Q0W4qnpGx8uHdFku7N8k6FzAVYfp6BUx/OBocZhf7I50wo6', 0, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `post`
--
ALTER TABLE `post`
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
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
