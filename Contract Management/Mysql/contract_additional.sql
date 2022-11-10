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
INSERT INTO `additional` VALUES (23,_binary '‰PNG\r\n\Z\n\0\0\0\rIHDR\0\0\0\á\0\0\0\á\0\0\0	m\"H\0\0\0xPLTEÿ\0\0ÿÿÿÿññÿAAÿ\Æ\Æÿ††ÿ..ÿžžÿ\Í\Íÿ‘‘ÿøøÿ³³ÿ\Â\ÂÿXXÿ½½ÿ\Ò\Òÿ\ß\ßÿ\ê\êÿ©©ÿššÿ==ÿ\â\âÿÿ]]ÿ55ÿÿÿŠŠÿzzÿ%%ÿ		ÿ¶¶ÿssÿQQÿHHÿddÿ{{ÿmmÿttÿ\×\×\â\ès\0\0fIDATxœ\å	bª0†Áö©€(\î\ÒZEm\ëýoø@+²%d™É¤\é€Æ¯d™Ifñ|l…ód²Xûx5üH7\ï°I?†«x,“d¢\ï!þ\íp}\â\Ý\Æ\ãi³‹ƒ\ã\Z“‹0‰².Z]/Y” ý\Âd¹•€{j»Ä „&L³T	\ï®4›€(a\Å\Zt\Åè²„#D\'\0¼»NÜ—„\"œ}\á\Ýõ5úe „\áh\ÌWh7™­\0„\É\ï®=À\æªM8S;DµÕž¬š„³3*_¡³&£\áŸ\ï\Æ8&\"L ?1\Å\Z\ëQ™0ü6\ÆW\è[y_U%\å+42J8Ö±=U•ª-GB\Ãô)¥©ª@8%\â+45@8¸z\ÞE\Ú$—%“ò’]’„o\Ô|¹\Þ	\çCjº›†s,\Â	5Z©	\á;5WE\ï„¡9+TD±ð\Ñ(Jh\É|Jx1\n^©:t…$¤4c\Ø3p„\Ô,- \Í{J¢ñ¨jŽB5¶úM¸^B»ûmž¢wõM\ÔB{7™§z¶>¡­\ÇD]üCƒKh\çA\ß÷\è\ç\Úhªu‹gÀq\çÔ¿[B3œM\Ú\æMð4d;SlB»üÁ>\Åò„6yô\"bzý,B{\îdDÅº»aþ¦]\æ!\Æn\Ã üM»\ÌCCB|s{9˜ÿ\è\ìová„øW÷•3ƒû«þ]„¸1ªn|{Z×³M!ú\ëR\Í8þ\á‹!º½ýZ\Ô\é°ÁÛ„!\äˆ:5,X´m½µ	‘Ÿ°£\æx°·\ßý„¸û\èW{/\06[ûi‹3Ê¢3ð˜0\í#D¼˜aoA[\Ík›!\Þ6sb\à¯û\Æf\ã!w\×\á\Û	?}›M0­\Ð\á«~\06þP}µ\×	\áýúU0\îy­•I<S\Ýß¯‚ž«\Ë\ÛQ$øÁQ«mi5BÍ€\Øh2-4y_¡ð;;?/JIg¡®£–#\Â\ÔPu\îT	ucš¥yP	«±B¨\íŠ\ÚCXýˆB\í´‹·]„úg¡E„•3ñI¨Ÿùb\á¾M`‘*b]\n•§UI\àT(b\Ý=—.FI}¦tbîš„·–Ÿÿ8úd9k€;5kB\'H¶\Åø\Â(\îL¡¯:!þ%0‹\ï)}P#Œ\Ð\Æi\Ø\à¥~CQ\Þ\rm\É8\á©Jˆ}\\ˆAˆx{V\rLRÂ¨Bh\"*Á<aü$4°“2	\áHC\ÞDwNK\Âq”R„YIh$#”€0}¢N5\Þü\à‚p‰9H)\n\Â\å!nÝ‡‡(·?„˜c<EA\è\Ý	\Í,C\Z\Â\äFh\Âdóˆ£a†:F)\Â\ìFÿ¼\Õ)Â—‚Ð„\çTˆ„0÷ <¼« †h\×9!d\\O4„Çœ\ÐTf\rašŠÉ§!ŒsBŒRk]¢!\Üù^ˆðŽ\Þ)\Z\ÂM\è‹Ê§!\ÌùY¥d„‰g,u„ˆp\âK¢$\"\\xf|Œp\éKe&\"<¼Òœ\r\î=ci†D„±·B¡\á\Ê3–¥FD8ô>G(EDø\á«ñHD˜z¦o*Âw@¡¡1>2BƒŒd\ß\Ðýu\èþ^\êþy\è¾M\ã¾]\ê¾o\á¾è¾\ïþ=ûwm\îß—º\ç\íþ»…ûoO\î¿þ7`÷\ßñÝ\Åp?ž\Æý˜(÷\ã\ÚüuŒR„±‰\îÇ—º#\ì~œ÷ˆ\Õw?\ß\Âýœ÷óžüq”R¤¹k\î\çºŸCJ™ŒHX\É¦\Ì\åF$¬\ær\æ\ã#Vóñ	k*\àžü*!]]<\Âz]º\Ú&x„õ\Ú&tõi\ÐõiKŒ<dš°Ycÿ\ê\Û0a«N~g\'Ã•?Úµ¾ÐD\ÃU”\Úõ\Ú\0j\îñ\Õ\rˆõŸ\í¨¹‡\î3\r\ÖMD¾®atñý£uÖ¾D>0˜]üP¶š\îú¥\Ú5h¹b·aF8§5hQ?\â†	ˆñYu„1?\"¯ƒøJdÖ‚F¬»\Õ\Õ\å)\è\Âó\ìz\Þh·[Ÿ/Ø—vNMv¬3±¿m\ïrð\ê\ê£ôF„*·^ß¡²¸½€m¨4~‹ºÚ’04Ÿ¾\00ùý-@\\Œtx¾¼/¦‰xmýÊ¿xðºx;\ëŸ÷ô(\Ñz\Ãx	F\Ñ8Y«•×¯k°¾GA¦ð#zû\Ì\èœý¤%¥²ñõ÷\n\Ò\Øl>¡	|G~O\Z›\r„\"=»\Ô_¢, ê»¦nD\Ñ\nö\ÎS¾¦\'\í¨ºŸ’\n÷°T\íFM(Ñ‡T±EQú,9\ï_ª—\ì\è\ì~O\ç?Ð—ûôV÷\Ã\ßÔ¹z\Èv\ÔØ„¿j·á´¸\á\"6×€Ö•CÁ#4\r {[¶\ß2šx·\Í}„ø/\Ã\0ê¹«\ì!4–¥® ‡ ¼]/´z/‡z	-G\ì¿ý\ê\'´z¢öMQ1B‹·›þ1Bk\rþ1!Ch\é\Ñ\Ï=\è%	­4\àx¦š<¡?·\Í\ÓŠö“%ôC»ü\ÅXø]K˜\Ð.¯Ÿ\é\ÑkZtw\Ã\Î\Ñ#´e1\n/AyB;L8\ÉgJIB\ÌVw‚ê¼º$ô\Ð\á=rºH¿¡K\Ò\Z8bfŒ.¡bDÝˆ\è[!¸C‰0_\Æ\êIV”Ê®@B\nJ\ÄS‚$4=U•&¨¡\ï\'\æ,\ÕX\"v0_Ž¨qÓ¥\Îj‚\Ð÷gøŒ\çYÿ\Ï@$\Ìq“¶š|\0„ùz\ÄË¶\Ùk¬?@\Â|_ad¾\íF\ÊûgU „¹f\Ð)š_\Ú\ÓóGP„¹IÁ¥KŸ\"ˆ Õ»\às…\ÄG ³ó!P\Â\\ƒi¦c³¦\Ù\î\ë\ÝMX(Yª \Û%À\Ö\Ùa¡$\Êd\êÀ½d2AýR\Â\",®A¼\ã\×G\Ý\ì\â\à¸]x\ra\ÞÎ“\Éb\ì\ã\Õð#\Ý¼\Ã&ý®\â}°\\L’9&\Û]ÿ¢Xt\Ì}\Ø \0\0\0\0IEND®B`‚','1.png','C:/Contract_management(Ð‘Ñ‹ÐºÐ¾Ð² Ð•.Ð˜.)/1.png',6),(24,_binary '‰PNG\r\n\Z\n\0\0\0\rIHDR\0\0\0\á\0\0\0\á\0\0\0	m\"H\0\0\0ŠPLTEÿ\0\0ÿÿÿÿAAÿ..ÿ\Ý\Ýÿööÿ\Í\Íÿ½½ÿ³³ÿ\Ò\Òÿ\Â\Âÿ‘‘ÿXXÿžžÿ††ÿ››ÿ\í\íÿyyÿúúÿ==ÿ\â\âÿ]]ÿóóÿ\è\èÿŠŠÿ©©ÿÿQQÿÿ%%ÿ		ÿ55ÿ¶¶ÿssÿHHÿddÿ\Ø\Øÿ~~ÿjjÿ¥¥ÿÿ@@ÿTTÿ\È\Èÿ\Z\Zÿtt.ÿ\0\0ŸIDATxœÍkcª<\Ça€¢²£\âmêœ—]\Îs6÷ý¿\Þ\â¥M›4¥ý¿\ëOJš¦I\Z„¶•/\âþr8g“hs\\½o«\ã&šd\ãÁpÙ¹õÿX|v>\Ý\r²\í1€t\Üfƒ\Ý\Ô&§-\Â8\Ý?h÷zÚ§±¥‘\Ø Œ‡3\ÜM³¡\rJn\ÂywÿJÂ«ôº\ïÎ™G\ÄJ˜¤\ßt}§	\ç ø\ç\éš¯\Ò:\å{“\\„½/6¼J_=¦‘±&\Ï[f¾R\Ûg–\Ù\Ê@-\àU\Z3Wc\Âme\Ð\Õ\Ìx²\ZöVùJ;öùNŒG„q\Ö\n_©\Ì\à{$&¿­ñ•ú%\ÛU*\ás«|¥ž[%\ì˜øžT½\Ò>G\na\Þ\î½é—²$vñ•\ê¶@8w\ïh—K\Øq\ÊW\nû5\"	?]óú´H¸ˆ\\Ó-lö]£]Õ·Cøâš«¦„y{^¨Ž2\í¥Q—p\ä\Ç\'xS4\â%üp\r$\Ð\'¡K7F.=G‹p\éšE¢%\á\Ð5‰TCÂk@\Â?®)@ý1\'d\\m¢\ídEðy\"ZJD¡ñ\Ý\Æ\Ë]o”$ùy\Îó$Yôº\ËÁ×„%R š¨\nB3#ó=\ìÀNò¢ó¼7FT˜˜\Ð`™8t#¹£î¯™\Ã/\Z !y¡Ÿ<£68\å±ñ\Ä\0\\ú!Bª«ö2\Å\áUšþGG„8€pDúgÿv¼J}ò+\à†\Ë	s\ÊÇ‘1Ó†\çŠ\ä›)9!a?hv„rf¤¥dxBüŽ~ƒ‰-\0\ê,«t\×/#\Ä\Çdt¼`M‘Va\Ù\ï+!\\`Ÿ¿…—‡ùG§_è§£gf§”\×(„û\0\×)^~\Þ\ç1¬_º\êÕ’öŠ0„\ØÀ¯\Ì\Â\ä?c±\ï9ª 	¡Kq¨XHˆ\ÝË‚B‹—ðW\ß\n\Ã4\ÅoB„?´ˆpŽ{\î·x„\Ê\åFa|s|–€\è\ØFDˆ[uß…Ã›j%¡¬á¹ŠvqDc\âü\í/\áØ´·•ð¾\0(ðÁ›„9\ê‘{\ÑÀ0\Æ^<.\Âd\áž\ÔôÞš„¨#l\á7ˆ3T\è\Ì3yC=+~Õ„¨\ámE£\Â\î*7bŒ|XÓž6Q±\Ñ2_ÈŽ\0a¸C>\ìUEˆÊ“­?S\äˆJ\Í Dl\â\êc\Þ\Ía‚y–Ð\'m l œ\å+ô=õ@ˆ13Â0ÅŽ§´.bù`l\î	Qßµ08‚Þ”T\ç\é?\ä\Ã\î\Óü\î	1ûú±p491¤\rÅ’°.÷ûý€ü(Id„h_\"Öµ¹³€w„WW¶#¤FÉ¡/»\0d„=\ÌSdùžÔ¤)0‚}X=\Ü^\'Ä¼Byºv4g	-óEØ‰Q‰5B\Ô+”O*\êÁA»µ—X#Ä”¬å£¡8¦\0!úg«®!j-¶u\Ô\ãñ\êsúL\ã¶&\ÞQ•/€\å£8¦¥6\áöi·\ß\ëJˆòHÁ39\ê\É.ôL\Ü\èJ]mýõ¹¨M8£¨eB`°}¼xuæ¯„¨\ê3pñ¢*ü@Eÿ]WŸ!j©€ó;©¦<\É\ÅgL\\Œ!\î7‹tˆ\Û¸dÿ³]‚€gBd$\Ä[…JÿA%8ƒó;B\ä.4\n96>v˜¡N\È)H\ï‘ûøŒŒ˜V\Zh\Â\Ô_\×	±.–#V%‚„\È\Ïè¤¤Fˆ\r…À\çõÄŒpòq§5Blv\0|\Ú@\Ü\æƒ\ß!…ðûFˆžp1\01+\Ì2¤\Ì\ÒÊšžÑ‹\Í?h09\Ñ1WRúR÷Jˆ\Ï„ª¨+>\è\n¢\Ï/J\í¯„øò°¨~\é_ˆ\çUžõz!$ü>ò¤0\ÜPSLˆCoOŠÏ„”\0 <‚K®÷´Ó‚á™²¡;È†B\Ý\âß‡\0¢••\ÍÎ„¤?–|5sz\î6˜µ@lS’Ì”dR¨a\0G1Ð§3g\Å\'Bâ˜Èž\Ò\ìÁY uG–ž\É\Ùò\ã‡U‘šþZ	Á\Ò²÷\'BtF\ÇMŸ½K–Á¨74˜ ¥@Oð/ñ¡O%!úù^\Û\Ã,[O\éJ\Ë!¹\ÍO^\Ò\Í;¯ ]u¥\0*ž\Z„;¶1\Z	y\Óû\ì\nBOŠ\ïÀ\Ý!½\ÑÁ  ô¤F\Ð›„6Z­\áNRƒV\Û0 &O0¬±3h˜v\Ì\ê~•YPöž‘µ_D¯”YÍ¤ÉšŒJ\ãÀvÐ¾\ÂlÁ\î^\ÔÚƒK…™±_>Û¯ À–\á$>,øPü\"!;l•½Öœ\Ú\ç¨i\ç\×q\àÞ¥‘†|J÷ö\Ë“\nc½BK¡yk±Ià¼³k¶WSQÀ°w5C\äð·6c·2£,\å104Æ†‚\0yü\ÉU@L+\à4E™\ÜI§|G(€Ï›t\Ç8\Z\ç²9\"o\î¾C(>\Ê\Øn\åÌ–B6†³y\Ú\Ñ\Ñz8ƒ\ÖK6n|\Zèœ¹û]\ä\Â/&f\ÄÝ¦\Òþ\Þ\"‚Aþ\Ýj\ÖúþJ§¢ždB\Z·¼\Çÿ&hj\Å$Z\ÓÌ€’¾2N\Ó^¬m\r\ÔÚ˜Ÿ•–­\ÅK#ùŸ?[l\Ó\ßo+\æ-¯jÊ‡V]ã¸syR\Þ\Âvk\ÍEgO¤.\ÚÔ¼k¢B\Ç\Üþù\á—ôL¢c÷š¡“¶\ÖÏ€\×\Ò]n·•£\Ù\Ìò9~$+Ê—-\Ýr2°›‹!ó\Ð\æM ‘\Ú\ÙÌ§y‘œ(}X7/5M\Ís¢dz—˜Ž+õ•\æµI%»\×g\×r\æÇ“Yn¢\\\âôÚ¤ýK¢öFù¥R}	Wø‘‹û1R“a™\Ät\ä¦ñyl\ç-“0õgÑ¦ù¬+¤\ç\êK´\íq®\îøº\æ\êómóEf\îð¥K½×‡¸47Kœ^<p©™!wA¸—`˜»\ÍÖ¹\Ö=±¬ˆ‘`‘º=~\röWB†@º <ò\ÇyÄ­þT y§f˜I¯©]\ÝjH\ÑuÀ:4n6©\Õ:nM³c¡©\êµ\ÜÔ²¢“\Z\'-\Óv®	Vª^O-¿D3Ô‡l\ÇRw=\èÓ´Q€ý\á\âšY¡\îûbP­i£XÉ—<ö6¡¯Wù‘óLÇ›úÓªÁƒ;\æA\Z\é±\Ç!ô\ÝH\íõ \Ýø¦FŸ(|2\îcÓ£Ä“5\â¬f¯/\ì’H¸]™Aú\'e\Í~m\È9¶°\'\í­¬ \çn¬{·´)ê›ˆ	\×h^\Ê/]Ba\ïKÄ‚\áhŠ†ú„\âþ¥\Ú¬csJ“PÒƒVû%ªï´&MBYaÝ—\è=¡´´n…Š÷„ò~Þšgú¾=\Ù5\"\ß	¡¾úzw#xNÞ \çzN\ßo¡µ\Åð›PqG‰\Ö†×„\Ê{ftV¯	\ÕwiŸ	5\î{\ÒÈ¯ñ™P\ç\Î.õI”Ç„Z÷®©;¬úK¨ywž2<\ì/¡\îý‡*{\ê-¡ö–ª¾Lp]«	÷*\îy}r&(nºK–§P¼e\á\îæª¤nQ\È;©-Q\Ý	}/·ikŸ¶E¸[=Ì§\Ã É»}QIM\ÂIr«´‚\Üµ}A§`o[\æ²jkOú\àþ\Ä^´:S\n¾©&dL®µ\'°¿’Ð§\ì‰Àž’\Z„^¤\àARnt”„ž#ªwrjB¯\'ªjŠ\êzlnFF›\Ð\ÛE^&0„ž.ýz)=z„^:pš	!š„œ›x\Î6‰0\Ìý\Ú/fPSW\Z¡_»~D¸A\èQ\ì¼CÓ€0\\øñ1F\à4F„&-üù„L\ÉB24…5|3¡9a87ºL\ÆX\ïP+;B·!3™@\æ®\êzµAC\Â\âktQ#\ë\Ó`…¡\Ï6Z\à…\ÈÃ¤Ý©úµsµC†q{žj_\Ïk‹°ø\Û)\"9\Ð>@\Â0\ì\Ùg<V>Œv+šgÆ•Æ„\Å÷h¯¢klðý1–­ul´\Ú>“\íg],„…z¬\í}qq.yJ/—~\Ô:E;\ØRñJRŽF^\ß)\Ëì¼ˆ•°Ð¼»7ñY_÷]¾·W‰›°T<¤­ ³!ƒ\él\Èa©8\ÝcúÀ=\íSt¥l–Ê§»A¶…û£·\Ù`7¥\ìûte“°R¾ˆû\Ë\á`œM¢\Íqõ¼­Ž›h’\Ãe?^\Ød«ô?Ö¼ 0ò0:§\0\0\0\0IEND®B`‚','2.png','C:/Contract_management(Ð‘Ñ‹ÐºÐ¾Ð² Ð•.Ð˜.)/2.png',6);
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
