CREATE DATABASE  IF NOT EXISTS `wp_scan` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `wp_scan`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: wp_scan
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `diff_scan`
--

DROP TABLE IF EXISTS `diff_scan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diff_scan` (
  `scan_id` int(11) NOT NULL AUTO_INCREMENT,
  `scan_time` datetime NOT NULL,
  `wp_version` varchar(20) NOT NULL,
  `path_location` varchar(500) NOT NULL,
  PRIMARY KEY (`scan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diff_scan`
--

LOCK TABLES `diff_scan` WRITE;
/*!40000 ALTER TABLE `diff_scan` DISABLE KEYS */;
INSERT INTO `diff_scan` VALUES (8,'2017-06-23 04:28:33','4.7.5','C:\\xampp\\htdocs\\wordpress'),(9,'2017-06-23 04:44:33','4.7.5','C:\\xampp\\htdocs\\wordpress'),(10,'2017-06-23 05:02:45','4.7.5','C:\\xampp\\htdocs\\wordpress'),(11,'2017-06-23 05:06:56','4.7.5','C:\\xampp\\htdocs\\wordpress'),(12,'2017-06-23 05:08:12','4.7.5','C:\\xampp\\htdocs\\wordpress'),(13,'2017-06-23 05:11:03','4.7.5','C:\\xampp\\htdocs\\wordpress'),(14,'2017-06-28 12:53:22','4.7.5','C:\\xampp\\htdocs\\wordpress'),(15,'2017-06-28 03:35:59','4.8','C:\\xampp\\htdocs\\wordpress-1'),(16,'2017-07-03 11:49:13','4.8','C:\\xampp\\htdocs\\wordpress-1'),(17,'2017-07-03 11:52:33','4.8','C:\\xampp\\htdocs\\wordpress-1'),(18,'2017-07-03 11:53:49','4.8','C:\\xampp\\htdocs\\wordpress-1'),(19,'2017-07-03 12:12:20','4.8','C:\\xampp\\htdocs\\wordpress-1'),(20,'2017-07-03 12:35:55','4.8','C:\\xampp\\htdocs\\wordpress-1'),(21,'2017-07-03 12:37:48','4.8','C:\\xampp\\htdocs\\wordpress-1'),(22,'2017-07-19 02:52:12','4.8','localhost'),(23,'2017-12-08 11:36:40','4.9','localhost');
/*!40000 ALTER TABLE `diff_scan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-08 15:51:48
