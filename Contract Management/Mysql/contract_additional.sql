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
-- Table structure for table `additional`
--

DROP TABLE IF EXISTS `additional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `additional` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` blob,
  `name` varchar(45) DEFAULT NULL,
  `pure_path` varchar(200) DEFAULT NULL,
  `id_info` int NOT NULL,
  PRIMARY KEY (`id`,`id_info`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additional`
--

LOCK TABLES `additional` WRITE;
/*!40000 ALTER TABLE `additional` DISABLE KEYS */;
INSERT INTO `additional` VALUES (23,_binary '�PNG\r\n\Z\n\0\0\0\rIHDR\0\0\0\�\0\0\0\�\0\0\0	m\"H\0\0\0xPLTE�\0\0�������AA�\�\�����..����\�\�����������\�\��XX����\�\��\�\��\�\��������==�\�\���]]�55��������zz�%%�		����ss�QQ�HH�dd�{{�mm�tt�\�\�\�\�s\0\0fIDATx�\�	b�0�����(\�\�ZEm\��o�@+�%d�ɤ\��Ưd�If�|l��d�X�x5�H7\�I?��x,�d��\�!�\�p}\�\�\�\�i���\�\Z��0��.Z]/Y� �\�d���{j�Ġ�&L�T	\�4��(a\�\Zt\�貄#D\'\0��Nܗ�\"�}�\�\��5�e �\�h\�Wh7��\0�\�\�=�\�M8S;D�՞����3*_��&�\��\�\�8&\"L ?1\�\Z\�Q�0�6\�W\�[y_U%\�+42J8ֱ=U��-GB\��)���@8%\�+45@8�z\�E\�$�%���]���o\�|�\�	\�Cj���s,\�	5Z�	\�;5WE\���9+TD��\�(Jh\�|Jx1\n^��:t�$�4c\�3p�\�,-�\�{J��j�B5��M�^B��m��w�M\�B{7��z�>��\�D]�C�Kh\�A\��\�\�\�h�u�g�q\�Կ[B3�M\�\�M�4d;SlB���>\��6y�\"bz�,B{\�dDź�a��]\�!\�n\� �M�\�CCB|s{9��\�\�ovᝄ�W��3�����]��1�n|�{Z׳M!�\�R\�8�\�!���Z\�\��ۄ!\�:5,X�m��	����\�x��\�����\�W{/\06[�i�3ʢ3��0\�#D��aoA[\�k�!\�6sb\����\�f\�!w\�\�\�	?}�M�0��\�\�~\06�P}�\�	\���U0\�y��I<S\�߯���\�\�Q$��Q�mi5B̀\�h2-4y_��;;?/JIg����#\�\�Pu\�T	uc��yP	��B�\�\�CX��B\���]��g�E��3�I���b\�M`�*b]\n��UI\�T(b\�=�.FI�}�tb����8�d9k��;5kB\'H�\��\�(\�L��:!�%0�\�)}P#�\�\�i\�\�~CQ�\�\rm\�8\�J�}\\�A�x{V\rLR¨Bh\"*�<a�$4��2	\�HC\��DwNK\�q�R�YIh$#��0}�N5\��\��p�9H)\n\�\�!n݇�(�?��c<EA\�\�	\�,C\Z\�\�Fh\�d��a�:F)\�\�F��\�)�Є\�T��0��<����h\�9!d\\O4�ǜ\�Tf\ra���ɧ!�sB�Rk]�!\��^���\�)\Z\�M\��ʧ!\��Y�d��g,u��p\�K�$\"\\xf|��p\�Ke&\"<�Ҝ\r\�=ci�D���B�\�\�3��FD8�>�G(ED�\���HD�z�o*w@��1>2B��d\�\��u\��^\��y\�M\�]\�o\�辏\��=��wm\�ߗ�\�\�����oO\���7`�\��ݏ\�p?�\���(�\�\��u�R���\�Ǘ�#\�~���\�w?\�\������q�R��k\�\���CJ��HX\��\�\�F$�\�r\�\�#V��	k*\���*!]]<\�z]�\�&x��\�&t�i\��iK�<d��Yc�\�\�0a�N~g\'Õ?ڵ�ЏD\�U�\��\�\0j\��\�\r���\��\�3\r\�MD��at���u־D>0�]�P��\���\�5h�b�aF8�5hQ?\�	��Yu�1?\"���JdւF��\�\�\�)\�\��\�z\�h�[�/ؗvNMv�3��m\�r��\�\��F�*�^ߡ����m�4~��ڒ04���\00��-@\\�tx��/��xm�ʿx�x;\����(\�z\�x	F\�8Y��ׯk��GA��#z�\�\���%�����\n\�\�l>�	|G�~O\Z��\r�\"=�\�_�, 껦nD\�\n�\�S��\'\�����\n��T\�FM(чT�EQ�,9\�_��\�\�\�~O\�?З��V�\�\�Թz\�v\�؄�j�ᴸ\�\"6׀֕C�#4\r�{[��\�2�x�\�}��/\�\0깫\�!4��������]/�z/�z	-G\��\�\'�z��MQ1B����1Bk\r�1!Ch\�\�\�=\�%	�4\�x��<�?�\�\����%�C��\�X�]K�\�.��\�\�kZtw\�\�\�#�e1\n/AyB;L8\�gJIB\�Vw�꼺$�\�\�=r�H��K\�\Z8bf�.�bD݈\�[!�C�0_�\�\�IV�ʮ@B\n�J\�S�$4=U�&��\�\'\�,\�X\"v�0_��qӥ\�j�\��g��\�Y�\�@$\�q���|\0��z\�˶\�k�?@\�|_ad�\�F\��gU ��f\�)�_\�\��GP��I��K�\"� ջ\�s�\�G ��!P\�\\�i�c��\�\�\�\�MX(Y�� \�%�\�\�a�$\�d\���d2A�R\�\",��A�\�\�G\�\�\�\�]x\ra\�Γ\�b\�\�\��#\��\�&��\�}�\\L�9&\�]��Xt\�}\� �\0\0\0\0IEND�B`�','1.png','C:/Contract_management(Быков Е.И.)/1.png',6),(24,_binary '�PNG\r\n\Z\n\0\0\0\rIHDR\0\0\0\�\0\0\0\�\0\0\0	m\"H\0\0\0�PLTE�\0\0����AA�..�\�\�����\�\��������\�\��\�\�����XX����������\�\��yy����==�\�\��]]����\�\���������QQ��%%�		�55����ss�HH�dd�\�\��~~�jj�������@@�TT�\�\��\Z\Z�tt.�\0\0�IDATx�͝kc�<\�a����\�mꜗ]\�s6���\�\��M�4���\�OJ��I\Z���/\��r8g�hs\\�o�\�&�d\��pُ���X|v>\�\r�\�1�t\�f�\�\�&�-\�8\�?�h�zڧ���\� ��3\�M��\rJn\�yw�J«��\�ΙG\�J��\�t}�	\��\�\��\�:\�{�\\��/6�J_=���&\�[f�R\�g�\�\�@�-\�U\Z3Wc\�me\�\�\�x�\Z�V�J�;��N�G�q\�\n_�\�\�{$&����%\�U*\�s�|��[%\���T�\�>G\na\�\��闲�$v�\�@8w\�h�K\�q\�W\n�5\"	?]���H��\\ӝ-l�]�]շC�⚫��y{^��2\�Q�p\�\�\'xS4\�%�p\r$\�\'�K7F.=G�p\�E�%\�\�5�TCk@\�?�)@�1\'d\\m�\�dE�y\"ZJD��\�\�\�]o�$�y�\��$Y��\��ׄ%R���\nB3#�=\��N��7FT��\�`�8t#��\�/\Z !y��<�68\��\�\0\\�!B���2\�\�U��GG�8�pD�g�v�J}�+\��\�	s\�Ǒ1ӆ\�\�)9!a?hv�rf��dxB��~��-\0\�,�t\�/#\�\�dt�`M�Va\�\�+!\\`������G�_解gf��\�(���\0\�)^~\�\�1�_�\�Ւ��0�\���\�\�\�?c�\�9� 	�Kq�XH�\�˂B���W\�\n\�4\�oB�?��p�{\�x�\�\�Fa|s|��\�\�FD�[u߅Ûj%��ṊvqDc\��\�/\�ش���\0�(����9\�{\��0\�^<.\�d\�\��ޚ��#l\�7�3T\�\�3yC=+~Մ�\�mE�\�\�*7b�|XӞ6Q�\�2�_Ȏ\0a�C>\�UE�ʓ�?S\�J\� Dl\�\�c\�\�a�y�Н\'m�l �\�+��=�@�130Ŏ��.b�`l\�	Qߵ08�ޔT\�\�?\�\�\�\��\�	1���p491�\rŒ�.�����(Id�h_\"ֵ���w�WW�#�Fɡ/�\0d�=\�Sd��Ԥ)0�}X=\�^\'ļBy�v4g	-�E؉Q�5B\�+�O*\��A���X#Ĕ�壡8�\0!�g��!j-�u\�\��\�s�L\�&\�Q�/�\�8��6\��i�\�\�J��H�39\�\�.�L\�\�J]m����M8��eB`�}�xu毄�\�3p�*�@E�]W�!j���;��<\�\�gL\\�!\�7�t�\��d��]��gBd$\�[�J�A%8��;B\�.4\n96>v��N\�)H\�������V\Zh\�\�_\�	�.�#V%��\�\�褤F�\r��\��Čp���q�5Blv\0|\�@\�\�\�!���F��p1\01+\�2�\�\�ʚ�ы\�?h09\�1WR�R�J�\����+>\�\n�\�/J\���~\�_�\�U��z!$�>��0\�PSL�CoO�τ�\0�<�K����ӂᙐ��;ȆB\�\�߇\0���\�΄�?�|5sz\�6��@lS�̔dR��a\0G1Ч3g\�\'B⁘Ȟ\�\��Y uG��\�\��\�U���Z	�\���\'BtF\�M��K���74���@O�/�O%!��^\�\�,[O\�J�\�!�\�O^\�\�;��]u�\0*�\Z�;�1\Z	y\��\�\nBO�\��\�!�\��� ��F\���6Z�\�NR�V\�0�&O0��3h�v\�\�~�YP����_D��Yͤɚ�J\���vо\�l�\�^\�ڃK���_>ۯ���\�$>,�P�\"!;l���֜\�\�i\�\�q\�ޥ��|J��\��\nc�BK�yk�I༳k�WSQ��w5C\��6�c�2�,\�104Ɔ�\0y�\�U@L+\�4E�\�I�|G(�ϛt\�8�\Z\�9\"o\�C(>\�\�n\�̖B6��y\�\�\�z8�\�K6n|\Z萜��]\�\�/&f\�ݦ\��\�\"�A�\�j\���J���dB\Z��\��&hj\�$Z�\�̀���2N\�^�m\r\�ژ����\�K#��?[l\�\�o+\�-�jʇV]㸝syR\�\�vk\�EgO�.\�Լk�B\�\���\��L�c�����\�π\�\�]n���\�\��9~$+ʗ-\�r2���!�\�\�M �\�\�̧y��(}X7/5M\�s�dz���+��\�I%�\�g\�r\�ǓYn�\\\��ڤ�K��F��R}	W����1R�a�\�t\��yl�\�-�0�gѦ��+�\�\�K�\�q�\���\�\��m�Ef\���K�ׇ�47K�^<p��!wA��`��\�ֹ\�=����`��=~\r�WB�@��<�\�yĭ��T�y�f�I���]\�jH\�u�:4�n6�\�:nM�c��\�\�Բ��\Z\'-\�v�	V�^�O-�D3ԇl\�Rw=\�ӴQ��\�\�Y�\��bP�i�Xɗ<�6����W���LǛ�Ӑ���;\�A\Z\�\�!�\�H\�� \���F�(|2\�cӣē5\�f�/\�H�]�A�\'e\�~m\�9��\'\��\�n�{��)ꛈ	\�h^\�/]Ba\�KĂ\�h����\���\���csJ�P҃V�%�&MBYaݗ\�=���n�����~ޚg��=\�5\"\�	���zw#xNލ�\�zN\�o��\��PqG�\��ׄ\�{ftV�	\�wi�	5\�{\�ȯ�P\�\�.�I�ǄZ���;��K�yw�2<\�/�\���*{\�-�����Lp�]�	��*\�y}r&(n��K��P�e\�\�檤nQ\�;��-Q\�	}/�ik��E�[=̝�\� ɻ}QIM\�Ir����\��}A�`o[\�jkO�\��\�^�:S\n��&dL��\'���Ч\�����\Z�^�\�ARnt���#�wrjB�\'�j�\�zlnFF�\�\�E^&0��.�z)=z�^:p�	!�����x\�6�0\��\�/fPSW\Z�_�~D�A\�Q\��CӀ0\\��1F\��4F�&-���L\�B24�5|3�9a87�L\�X\�P+;B�!3�@\�\�z�AC\�\�ktQ#\�\�`���\�6Z\��\�äݩ��s�C�q{�j_\�k���\�)\"9\�>@\�0\�\�g<V>�v+�gƕƄ\��h��kl��1��ul�\�>�\�g],��z�\�}qq.yJ/�~\�:E;\�R�JR�F^\�)\�켈��м�7�Y_�]��W���T<�� �!�\�l\�a�8\�c��=\�St�l�ʧ�A�����\�`7�\��te��R���\�\�`�M�\�q�����h��\�e?^\�d��?ּ�0�0:�\0\0\0\0IEND�B`�','2.png','C:/Contract_management(Быков Е.И.)/2.png',6);
/*!40000 ALTER TABLE `additional` ENABLE KEYS */;
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
