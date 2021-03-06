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

--
-- Table structure for table `file_diffs`
--

DROP TABLE IF EXISTS `file_diffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file_diffs` (
  `scan_id` int(11) NOT NULL,
  `type` char(3) DEFAULT NULL,
  `filename` varchar(45) DEFAULT NULL,
  `file_hash` varchar(100) DEFAULT NULL,
  `wp_hash` varchar(100) DEFAULT NULL,
  `location` varchar(500) DEFAULT NULL,
  `wp_location` varchar(500) DEFAULT NULL,
  `line_diff` longtext,
  KEY `scan_id_idx` (`scan_id`),
  CONSTRAINT `scan_id` FOREIGN KEY (`scan_id`) REFERENCES `diff_scan` (`scan_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_diffs`
--

LOCK TABLES `file_diffs` WRITE;
/*!40000 ALTER TABLE `file_diffs` DISABLE KEYS */;
INSERT INTO `file_diffs` VALUES (8,'E','admin.php','f00b53d690d6b703e000b48818bbd678','48f1fe3370f9d713b027655b6785e694','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\admin.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\admin.php',NULL),(8,'N','wp-config.php','5f4a31f182e62e66cec29b5659bb0265',NULL,'C:\\xampp\\htdocs\\wordpress\\wp-config.php',NULL,NULL),(8,'E','404.php','ccd85b4730350dd323f1338e587daaf4','38c8974713403d0c1d2f36bc28c90de0','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\404.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\404.php',NULL),(8,'E','back-compat.php','752e45881a02b231573db7cd5c231365','9b9bcb80065e860f6cea17ae74f1df8c','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php',NULL),(8,'E','profile.php','9099e2f29d1b8b113fb39ca4562de2f7','6874157fda181bc2866fd860d93376b9','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\profile.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\profile.php',NULL),(8,'E','xmlrpc.php','e5fbc058005156ff75a60b6dac0bb1ca','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\xmlrpc.php',NULL),(8,'E','searchform.php','ecb78583c68d24e5b3919b149c9257bd','82db8fd49b68a57525d03ebcd700235e','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php',NULL),(8,'D','wp-settings.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-settings.php',NULL),(8,'D','wp-blog-header.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-blog-header.php',NULL),(9,'E','admin.php','f00b53d690d6b703e000b48818bbd678','48f1fe3370f9d713b027655b6785e694','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\admin.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\admin.php',NULL),(9,'N','wp-config.php','5f4a31f182e62e66cec29b5659bb0265',NULL,'C:\\xampp\\htdocs\\wordpress\\wp-config.php',NULL,NULL),(9,'E','404.php','ccd85b4730350dd323f1338e587daaf4','38c8974713403d0c1d2f36bc28c90de0','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\404.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\404.php',NULL),(9,'E','back-compat.php','752e45881a02b231573db7cd5c231365','9b9bcb80065e860f6cea17ae74f1df8c','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php',NULL),(9,'E','profile.php','9099e2f29d1b8b113fb39ca4562de2f7','6874157fda181bc2866fd860d93376b9','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\profile.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\profile.php',NULL),(9,'E','xmlrpc.php','e5fbc058005156ff75a60b6dac0bb1ca','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\xmlrpc.php',NULL),(9,'E','searchform.php','ecb78583c68d24e5b3919b149c9257bd','82db8fd49b68a57525d03ebcd700235e','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php',NULL),(9,'D','wp-settings.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-settings.php',NULL),(9,'D','wp-blog-header.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-blog-header.php',NULL),(12,'E','admin.php','f00b53d690d6b703e000b48818bbd678','48f1fe3370f9d713b027655b6785e694','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\admin.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\admin.php','9: \n10: \"lorem ipsum dolor\"\n37: \n38: \n39: ?>\n40: \n41: <<!DOCTYPE html>\n42: <html lang=\"en\">\n43: <head>\n44: <title></title>\n45: <meta charset=\"UTF-8\">\n46: <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n47: <link href=\"css/style.css\" rel=\"stylesheet\">\n48: </head>\n49: <body>\n50: <p>lorem ipsum dolor hehe</p>\n51: \n52: </body>\n53: </html>'),(13,'E','admin.php','f00b53d690d6b703e000b48818bbd678','48f1fe3370f9d713b027655b6785e694','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\admin.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\admin.php','9: \n10: \"lorem ipsum dolor\"\n37: \n38: \n39: ?>\n40: \n41: <<!DOCTYPE html>\n42: <html lang=\"en\">\n43: <head>\n44: <title></title>\n45: <meta charset=\"UTF-8\">\n46: <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n47: <link href=\"css/style.css\" rel=\"stylesheet\">\n48: </head>\n49: <body>\n50: <p>lorem ipsum dolor hehe</p>\n51: \n52: </body>\n53: </html>'),(13,'N','wp-config.php','5f4a31f182e62e66cec29b5659bb0265',NULL,'C:\\xampp\\htdocs\\wordpress\\wp-config.php',NULL,NULL),(13,'E','404.php','ccd85b4730350dd323f1338e587daaf4','38c8974713403d0c1d2f36bc28c90de0','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\404.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\404.php','11: There is another line change here'),(13,'E','back-compat.php','752e45881a02b231573db7cd5c231365','9b9bcb80065e860f6cea17ae74f1df8c','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php','7: * relies on many newer fdunctions and markup changes introduced in 4.4.\n8: *awdawd\n9: *awdawd\n43: printf( \'This is a change<div class=\"error\"><p>%s</p></div>\', $message );\n72: add_action( \'templaddadte_redirect\', \'twentysixteen_preview\' );'),(13,'E','profile.php','9099e2f29d1b8b113fb39ca4562de2f7','6874157fda181bc2866fd860d93376b9','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\profile.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\profile.php','14: \n15: To be or not to be that is the question'),(13,'E','xmlrpc.php','e5fbc058005156ff75a60b6dac0bb1ca','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\xmlrpc.php','64: Both line 64 and 65 are tampered\n65: include_once(ABSPATH . WPINC . \'/class-wp-xmlrpc-erver.php\');\n89: The quick brown fox'),(13,'E','searchform.php','ecb78583c68d24e5b3919b149c9257bd','82db8fd49b68a57525d03ebcd700235e','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php','18: \n19: There is a diff in line 19\n20: and 20\n21: and 21\n22: and 22'),(13,'D','wp-settings.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-settings.php',NULL),(13,'D','wp-blog-header.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-blog-header.php',NULL),(14,'E','admin.php','f00b53d690d6b703e000b48818bbd678','48f1fe3370f9d713b027655b6785e694','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\admin.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\admin.php','9: \n10: \"lorem ipsum dolor\"\n37: \n38: \n39: ?>\n40: \n41: <<!DOCTYPE html>\n42: <html lang=\"en\">\n43: <head>\n44: <title></title>\n45: <meta charset=\"UTF-8\">\n46: <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n47: <link href=\"css/style.css\" rel=\"stylesheet\">\n48: </head>\n49: <body>\n50: <p>lorem ipsum dolor hehe</p>\n51: \n52: </body>\n53: </html>'),(14,'N','wp-config.php','5f4a31f182e62e66cec29b5659bb0265',NULL,'C:\\xampp\\htdocs\\wordpress\\wp-config.php',NULL,NULL),(14,'E','404.php','ccd85b4730350dd323f1338e587daaf4','38c8974713403d0c1d2f36bc28c90de0','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\404.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\404.php','11: There is another line change here'),(14,'E','back-compat.php','752e45881a02b231573db7cd5c231365','9b9bcb80065e860f6cea17ae74f1df8c','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\inc\\back-compat.php','7: * relies on many newer fdunctions and markup changes introduced in 4.4.\n8: *awdawd\n9: *awdawd\n43: printf( \'This is a change<div class=\"error\"><p>%s</p></div>\', $message );\n72: add_action( \'templaddadte_redirect\', \'twentysixteen_preview\' );'),(14,'E','profile.php','9099e2f29d1b8b113fb39ca4562de2f7','6874157fda181bc2866fd860d93376b9','C:\\xampp\\htdocs\\wordpress\\wp-admin\\network\\profile.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-admin\\network\\profile.php','14: \n15: To be or not to be that is the question'),(14,'E','xmlrpc.php','e5fbc058005156ff75a60b6dac0bb1ca','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\xmlrpc.php','64: Both line 64 and 65 are tampered\n65: include_once(ABSPATH . WPINC . \'/class-wp-xmlrpc-erver.php\');\n89: The quick brown fox'),(14,'E','searchform.php','ecb78583c68d24e5b3919b149c9257bd','82db8fd49b68a57525d03ebcd700235e','C:\\xampp\\htdocs\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-content\\themes\\twentysixteen\\searchform.php','18: \n19: There is a diff in line 19\n20: and 20\n21: and 21\n22: and 22'),(14,'D','wp-settings.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-settings.php',NULL),(14,'D','wp-blog-header.php',NULL,NULL,NULL,'C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.7.5\\wordpress\\wp-blog-header.php',NULL),(15,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(16,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(17,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(18,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(19,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(20,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(21,'E','xmlrpc.php','10ba1dc833eca0b7b1a5076353c6cf91','6c53e2ff076280c5cfc410a3c632c785','C:\\xampp\\htdocs\\wordpress-1\\xmlrpc.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\wp-files\\4.8\\wordpress\\xmlrpc.php','10: * There is a change here.'),(22,'E','link-template.php','8e664493e338ccf0004195cd4a981b1f','d081ee36e511afab6ba4d5ab201fd5bd','wp-includes\\link-template.php','C:\\Users\\Allendale\\Desktop\\Projects\\wp-scanner\\ftp\\wp-files\\4.8\\wordpress\\wp-includes\\link-template.php','7: */ Change here lol.'),(22,'N','wp-config.php','9de92490bb1e23d48d2f72b80251142f',NULL,'wp-config.php',NULL,NULL),(23,'N','wp-config.php','fbe9754524aa3e091bd56ebbef1eb2a6',NULL,'wp-config.php',NULL,NULL),(23,'D','wp-config-sample.php',NULL,NULL,NULL,'C:\\Users\\natoa\\Documents\\Github Repos\\wp-scanner\\main\\wp-files\\4.9\\wordpress\\wp-config-sample.php',NULL);
/*!40000 ALTER TABLE `file_diffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_plugins`
--

DROP TABLE IF EXISTS `wp_plugins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wp_plugins` (
  `scan_id` int(11) NOT NULL,
  `verified_plugins` longtext,
  `unverified_plugins` longtext,
  KEY `scan_id_idx` (`scan_id`),
  CONSTRAINT `plugin_scan` FOREIGN KEY (`scan_id`) REFERENCES `diff_scan` (`scan_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_plugins`
--

LOCK TABLES `wp_plugins` WRITE;
/*!40000 ALTER TABLE `wp_plugins` DISABLE KEYS */;
INSERT INTO `wp_plugins` VALUES (8,'This is a test','Another test'),(23,'akismet','');
/*!40000 ALTER TABLE `wp_plugins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'wp_scan'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-08 15:54:00
