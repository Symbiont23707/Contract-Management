-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: contract
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `number` varchar(45) NOT NULL,
  `subject` varchar(45) NOT NULL,
  `costing` double NOT NULL,
  `end_date` date NOT NULL,
  `id_executiver` int NOT NULL,
  `payment` varchar(100) NOT NULL,
  `contr_time` varchar(10) NOT NULL,
  `approval` date NOT NULL,
  `status` varchar(12) NOT NULL,
  `note` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `index_date` (`date`),
  KEY `index_number` (`number`),
  KEY `index_subject` (`costing`),
  KEY `index_end_date` (`end_date`),
  KEY `index_executiver` (`id_executiver`),
  KEY `index_payment` (`payment`),
  KEY `index_contr_time` (`contr_time`),
  KEY `index_approval` (`approval`),
  KEY `index_status` (`status`),
  KEY `index_note` (`note`),
  CONSTRAINT `info_ibfk_1` FOREIGN KEY (`id_executiver`) REFERENCES `employee_name` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES (1,'2020-09-13','4563ERG3','Командировка',2100,'2021-01-08',2,'50% аванс','360 р.д.','2020-10-26','исполнено',''),(2,'2023-09-20','N2131HJ','Обучение',40000,'2028-10-20',1,'100% аванс','20 б.д.','2020-09-20','не исполнено','\n'),(3,'2008-08-20','7KMND2','Страхование',6666,'2008-08-20',4,'10 к.д. с ТТН','10 к.д.','2008-08-20','не исполнено',''),(4,'2012-08-20','65EFWE','Оплата труда',66665,'2012-08-20',5,'30 б.д. с ТТН','30 б.д.','2012-08-20','не исполнено',''),(5,'2008-08-20','3NDMDS','Здоровье',4500,'2008-08-20',3,'15 р.д. с ТН','15 р.д.','2008-08-20','исполнено',''),(6,'2021-04-20','3NSAFN','Покупка',4445,'2022-05-30',8,'100% аванс','67 к.д.','2021-04-09','не исполнено','');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-10 22:26:56
