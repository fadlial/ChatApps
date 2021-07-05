-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 05, 2021 at 12:52 PM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `raf_chat`
--

-- --------------------------------------------------------

--
-- Table structure for table `publik`
--

CREATE TABLE IF NOT EXISTS `publik` (
`id` int(254) NOT NULL,
  `nickname` varchar(120) NOT NULL,
  `pesan` text NOT NULL,
  `waktu` varchar(240) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `publik`
--

INSERT INTO `publik` (`id`, `nickname`, `pesan`, `waktu`) VALUES
(1, 'Raflesia', 'tes1', '04-07-2021 15:37:05'),
(2, 'Raflesia', 'Halo Halo Semua ', '04-07-2021 15:37:13'),
(3, 'Raflesia', '', '04-07-2021 15:37:13'),
(4, 'Raflesia', 'hehehe Akhir Running juga', '04-07-2021 15:37:25'),
(5, 'Raflesia', 'sekarang coba kita tes privat chat ', '04-07-2021 15:37:52'),
(6, 'Client 33', 'Nuhun ', '04-07-2021 16:01:26'),
(7, 'Client 33', 'numpang gabung chatingan Xixixix', '04-07-2021 16:01:53'),
(8, 'Nick 1', 'hahahah Gabung Aja pake izin ', '04-07-2021 16:02:11'),
(9, 'Client 33', 'Mau Coba Tes Privat Chat yuk', '04-07-2021 16:02:30'),
(10, 'Nick 1', 'Lah hayuuu.', '04-07-2021 16:02:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `publik`
--
ALTER TABLE `publik`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `publik`
--
ALTER TABLE `publik`
MODIFY `id` int(254) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
