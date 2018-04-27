/*
Navicat MySQL Data Transfer

Source Server         : Mysql
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-04-27 17:51:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add user', '2', 'add_user');
INSERT INTO `auth_permission` VALUES ('5', 'Can change user', '2', 'change_user');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete user', '2', 'delete_user');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add group', '4', 'add_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can change group', '4', 'change_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete group', '4', 'delete_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add admin', '7', 'add_admin');
INSERT INTO `auth_permission` VALUES ('20', 'Can change admin', '7', 'change_admin');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete admin', '7', 'delete_admin');
INSERT INTO `auth_permission` VALUES ('22', 'Can add rank', '8', 'add_rank');
INSERT INTO `auth_permission` VALUES ('23', 'Can change rank', '8', 'change_rank');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete rank', '8', 'delete_rank');
INSERT INTO `auth_permission` VALUES ('25', 'Can add userinfo', '9', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change userinfo', '9', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete userinfo', '9', 'delete_userinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can add userstest', '10', 'add_userstest');
INSERT INTO `auth_permission` VALUES ('29', 'Can change userstest', '10', 'change_userstest');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete userstest', '10', 'delete_userstest');
INSERT INTO `auth_permission` VALUES ('31', 'Can add testimgsrc', '11', 'add_testimgsrc');
INSERT INTO `auth_permission` VALUES ('32', 'Can change testimgsrc', '11', 'change_testimgsrc');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete testimgsrc', '11', 'delete_testimgsrc');
INSERT INTO `auth_permission` VALUES ('34', 'Can add iden', '12', 'add_iden');
INSERT INTO `auth_permission` VALUES ('35', 'Can change iden', '12', 'change_iden');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete iden', '12', 'delete_iden');
INSERT INTO `auth_permission` VALUES ('37', 'Can add user_now', '13', 'add_user_now');
INSERT INTO `auth_permission` VALUES ('38', 'Can change user_now', '13', 'change_user_now');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete user_now', '13', 'delete_user_now');
INSERT INTO `auth_permission` VALUES ('40', 'Can add item', '14', 'add_item');
INSERT INTO `auth_permission` VALUES ('41', 'Can change item', '14', 'change_item');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete item', '14', 'delete_item');
INSERT INTO `auth_permission` VALUES ('43', 'Can add coach', '15', 'add_coach');
INSERT INTO `auth_permission` VALUES ('44', 'Can change coach', '15', 'change_coach');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete coach', '15', 'delete_coach');
INSERT INTO `auth_permission` VALUES ('46', 'Can add weeek3', '16', 'add_weeek3');
INSERT INTO `auth_permission` VALUES ('47', 'Can change weeek3', '16', 'change_weeek3');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete weeek3', '16', 'delete_weeek3');
INSERT INTO `auth_permission` VALUES ('49', 'Can add week8', '17', 'add_week8');
INSERT INTO `auth_permission` VALUES ('50', 'Can change week8', '17', 'change_week8');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete week8', '17', 'delete_week8');
INSERT INTO `auth_permission` VALUES ('52', 'Can add week7', '18', 'add_week7');
INSERT INTO `auth_permission` VALUES ('53', 'Can change week7', '18', 'change_week7');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete week7', '18', 'delete_week7');
INSERT INTO `auth_permission` VALUES ('55', 'Can add week2', '19', 'add_week2');
INSERT INTO `auth_permission` VALUES ('56', 'Can change week2', '19', 'change_week2');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete week2', '19', 'delete_week2');
INSERT INTO `auth_permission` VALUES ('58', 'Can add week5', '20', 'add_week5');
INSERT INTO `auth_permission` VALUES ('59', 'Can change week5', '20', 'change_week5');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete week5', '20', 'delete_week5');
INSERT INTO `auth_permission` VALUES ('61', 'Can add week6', '21', 'add_week6');
INSERT INTO `auth_permission` VALUES ('62', 'Can change week6', '21', 'change_week6');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete week6', '21', 'delete_week6');
INSERT INTO `auth_permission` VALUES ('64', 'Can add week1', '22', 'add_week1');
INSERT INTO `auth_permission` VALUES ('65', 'Can change week1', '22', 'change_week1');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete week1', '22', 'delete_week1');
INSERT INTO `auth_permission` VALUES ('67', 'Can add week4', '23', 'add_week4');
INSERT INTO `auth_permission` VALUES ('68', 'Can change week4', '23', 'change_week4');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete week4', '23', 'delete_week4');
INSERT INTO `auth_permission` VALUES ('70', 'Can add week3', '16', 'add_week3');
INSERT INTO `auth_permission` VALUES ('71', 'Can change week3', '16', 'change_week3');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete week3', '16', 'delete_week3');
INSERT INTO `auth_permission` VALUES ('73', 'Can add weekly_info', '24', 'add_weekly_info');
INSERT INTO `auth_permission` VALUES ('74', 'Can change weekly_info', '24', 'change_weekly_info');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete weekly_info', '24', 'delete_weekly_info');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$lwy8sGmXwaOy$mlkIYoWXcsC193cQAh+nQwhssS+71qIjR2onwxXoBA8=', '2017-12-08 11:07:24.186627', '1', 'root', '', '', '843825244@qq.com', '1', '1', '2017-12-08 11:07:18.059256');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for blog_admin
-- ----------------------------
DROP TABLE IF EXISTS `blog_admin`;
CREATE TABLE `blog_admin` (
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `registerdate` date NOT NULL,
  `uid` char(32) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_admin
-- ----------------------------
INSERT INTO `blog_admin` VALUES ('汪国强', '1395eab878d7ec5cf61ab1dc41352571', '2018-03-27', '3e13395f00b6498ebf02beb6dcd52138');
INSERT INTO `blog_admin` VALUES ('徐畅', '7b4de9c196d421d8694fbb56d699f9d9', '2018-04-01', '474e80692044400ca23260b667072a1e');
INSERT INTO `blog_admin` VALUES ('谢达', '827ccb0eea8a706c4c34a16891f84e7b', '2018-03-31', '5ac0b8bc62be4646a8f0273c1a54dcd2');
INSERT INTO `blog_admin` VALUES ('张义', '840b478ce4e91e693156136483510887', '2018-03-31', 'd90e1ff2974e4daaada33cbffa56c5f3');

-- ----------------------------
-- Table structure for blog_coach
-- ----------------------------
DROP TABLE IF EXISTS `blog_coach`;
CREATE TABLE `blog_coach` (
  `uid` char(32) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `birth` date NOT NULL,
  `tel` varchar(11) NOT NULL,
  `registerdate` date NOT NULL,
  `charge_id` int(11) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `blog_coach_charge_id_f2e5c062_fk_blog_item_id` (`charge_id`),
  CONSTRAINT `blog_coach_charge_id_f2e5c062_fk_blog_item_id` FOREIGN KEY (`charge_id`) REFERENCES `blog_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_coach
-- ----------------------------
INSERT INTO `blog_coach` VALUES ('2968673920f345d3b4f4a9e397d4a986', '何欣慰', '04128f8e9b1425ab5fd36a78af4d7caa', '男', '1994-06-14', '18899948787', '2018-04-01', '3');
INSERT INTO `blog_coach` VALUES ('65d035dd92be450197f5108cd6f32d46', '沈唯蓬', '95fd6aebd1acc701fc6578a6de8aac8d', '男', '1993-01-16', '13688655721', '2018-04-01', '2');
INSERT INTO `blog_coach` VALUES ('9721713acf8b444591782604eb2c0d82', '张义', '840b478ce4e91e693156136483510887', '男', '1997-06-18', '15865984984', '2018-04-01', '4');
INSERT INTO `blog_coach` VALUES ('b90d777cac194ead92666dc1d1483123', '赵旭', 'd6047daf94ef8027abb48272e2423739', '男', '1994-10-02', '15800859605', '2018-04-01', '1');
INSERT INTO `blog_coach` VALUES ('e95a4332b9844c45b7931c382f071837', '胡晗', 'da785ec668c03c9cd33b76055f7f5e5b', '男', '1995-11-21', '13788991453', '2018-04-16', '3');

-- ----------------------------
-- Table structure for blog_iden
-- ----------------------------
DROP TABLE IF EXISTS `blog_iden`;
CREATE TABLE `blog_iden` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `iden_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_iden
-- ----------------------------
INSERT INTO `blog_iden` VALUES ('1', '管理员');
INSERT INTO `blog_iden` VALUES ('2', '教练');
INSERT INTO `blog_iden` VALUES ('3', '会员');

-- ----------------------------
-- Table structure for blog_item
-- ----------------------------
DROP TABLE IF EXISTS `blog_item`;
CREATE TABLE `blog_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemname` varchar(20) NOT NULL,
  `itemcost` varchar(20) NOT NULL,
  `itemtime` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_item
-- ----------------------------
INSERT INTO `blog_item` VALUES ('1', '热瑜伽+动感单车+游泳', '4800', '60');
INSERT INTO `blog_item` VALUES ('2', '健身操项目+跑步+游泳', '3000', '60');
INSERT INTO `blog_item` VALUES ('3', '室内有氧运动+健身+游泳', '3500', '60');
INSERT INTO `blog_item` VALUES ('4', '室外运动项目+室内有氧运动+健身', '2500', '60');
INSERT INTO `blog_item` VALUES ('5', '健身操项目+热瑜伽+跑步', '2000', '60');

-- ----------------------------
-- Table structure for blog_rank
-- ----------------------------
DROP TABLE IF EXISTS `blog_rank`;
CREATE TABLE `blog_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_rank
-- ----------------------------
INSERT INTO `blog_rank` VALUES ('1', '初级用户');
INSERT INTO `blog_rank` VALUES ('2', '中级用户');
INSERT INTO `blog_rank` VALUES ('3', '高级用户');

-- ----------------------------
-- Table structure for blog_testimgsrc
-- ----------------------------
DROP TABLE IF EXISTS `blog_testimgsrc`;
CREATE TABLE `blog_testimgsrc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_testimgsrc
-- ----------------------------
INSERT INTO `blog_testimgsrc` VALUES ('25', '../static/testimg\\图片1.png', '汪国强');
INSERT INTO `blog_testimgsrc` VALUES ('26', '../static/testimg\\1 - 副本.jpg', '222');
INSERT INTO `blog_testimgsrc` VALUES ('27', '../static/testimg\\3c85ef765b823e8ccab9c7a9611a520a.jpg', '汪国强');
INSERT INTO `blog_testimgsrc` VALUES ('28', '../static/testimg\\2 - 副本.jpg', '222');
INSERT INTO `blog_testimgsrc` VALUES ('29', '../static/testimg\\S51126-173855.jpg', '111');
INSERT INTO `blog_testimgsrc` VALUES ('30', '../static/testimg\\QQ图片20151025170339.png', '汪国强');
INSERT INTO `blog_testimgsrc` VALUES ('31', '../static/testimg\\无标题.png', '44444');
INSERT INTO `blog_testimgsrc` VALUES ('32', '../static/testimg\\QQ图片20151025170339.png', '汪国强');

-- ----------------------------
-- Table structure for blog_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `blog_userinfo`;
CREATE TABLE `blog_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `weight` double DEFAULT NULL,
  `height` double DEFAULT NULL,
  `registerdate` date NOT NULL,
  `birth` date NOT NULL,
  `choice_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_userinfo_username_d8e9f4f6_uniq` (`username`),
  KEY `blog_userinfo_choice_id_d3e0bc5f_fk_blog_item_id` (`choice_id`),
  CONSTRAINT `blog_userinfo_choice_id_d3e0bc5f_fk_blog_item_id` FOREIGN KEY (`choice_id`) REFERENCES `blog_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=520 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_userinfo
-- ----------------------------
INSERT INTO `blog_userinfo` VALUES ('31', '陈奕迅', '4@11.com', '056c52faa34ec1644a7b324e736c01f6', '男', '155', '172', '2017-12-17', '1991-07-10', '2');
INSERT INTO `blog_userinfo` VALUES ('503', '贾克斯', '2222@fff.com', 'd81f9c1be2e08964bf9f24b15f0e4900', '男', '156', '175', '2018-03-01', '1993-06-17', '3');
INSERT INTO `blog_userinfo` VALUES ('504', '菲奥娜', '123@878', 'd81f9c1be2e08964bf9f24b15f0e4900', '女', '130', '155', '2018-03-01', '1986-04-02', '4');
INSERT INTO `blog_userinfo` VALUES ('510', '张艺谋', 'zhangyimou@qq.com', '39ea8891d895b2e8512c15b4c32cd4b2', '男', '180', '180', '2018-04-02', '1985-05-14', '5');
INSERT INTO `blog_userinfo` VALUES ('511', '陈凯歌', 'kevinchen@139.com', '7921f358c9e17b25f1291235b6cadf85', '男', '156', '175', '2018-04-02', '1993-01-22', '2');
INSERT INTO `blog_userinfo` VALUES ('512', '林允儿', 'yuner@qq.com', '8eca6d0df81f2c38abeb60696efafb38', '女', '140', '175', '2018-04-02', '1993-01-16', '1');
INSERT INTO `blog_userinfo` VALUES ('513', '周星驰', 'Stephen@Chow.139.com', '7e796f44ce9ec61e9f5293819a6fb510', '男', '140', '175', '2018-04-02', '1970-06-24', '2');
INSERT INTO `blog_userinfo` VALUES ('514', '朱茵', 'zhuyin@qq.com', 'fddacbe1c9b0fddd4cbc0f2e0aa39b43', '女', '120', '150', '2018-04-02', '1993-01-01', '2');
INSERT INTO `blog_userinfo` VALUES ('515', '谢安琪', 'xieanqi@139.com', 'de228f24e57b4cae0c7a4f5b5dc30597', '女', '130', '175', '2018-04-02', '1993-01-01', '2');
INSERT INTO `blog_userinfo` VALUES ('516', '梁博', 'liangbo@qqq.com', 'de7b7ad7341b7dd53037d7fa2736f6b5', '男', '220', '183', '2018-04-03', '1989-06-14', '2');
INSERT INTO `blog_userinfo` VALUES ('517', '陈坤', 'chenkun@139.com', '12ce84dc583fe7c90438f2b28b45f7fb', '男', '246', '180', '2018-04-07', '1986-10-24', '1');
INSERT INTO `blog_userinfo` VALUES ('518', '周迅', 'xunzhou@126.com', '82c2eea9acee9a04e001e354cfa09aa7', '女', '156', '158', '2018-04-07', '1990-06-15', '1');
INSERT INTO `blog_userinfo` VALUES ('519', '梁非凡', 'liang@139.com', 'a6c03bb6608c9557da737f1894ef28b9', '男', '188', '171', '2018-04-11', '1996-04-27', '3');

-- ----------------------------
-- Table structure for blog_userstest
-- ----------------------------
DROP TABLE IF EXISTS `blog_userstest`;
CREATE TABLE `blog_userstest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_userstest
-- ----------------------------
INSERT INTO `blog_userstest` VALUES ('1', '测试国强', '123');

-- ----------------------------
-- Table structure for blog_user_now
-- ----------------------------
DROP TABLE IF EXISTS `blog_user_now`;
CREATE TABLE `blog_user_now` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `weight` double NOT NULL,
  `height` double NOT NULL,
  `uid` varchar(255) NOT NULL,
  `choice_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `blog_user_now_choice_id_b2d3f4e5_fk_blog_item_id` (`choice_id`),
  CONSTRAINT `blog_user_now_choice_id_b2d3f4e5_fk_blog_item_id` FOREIGN KEY (`choice_id`) REFERENCES `blog_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_user_now
-- ----------------------------
INSERT INTO `blog_user_now` VALUES ('2', '陈奕迅', '137', '172', '31', '2');
INSERT INTO `blog_user_now` VALUES ('3', '贾克斯', '148', '175', '503', '3');
INSERT INTO `blog_user_now` VALUES ('4', '菲奥娜', '128', '155', '504', '4');
INSERT INTO `blog_user_now` VALUES ('5', '张艺谋', '172', '180', '510', '5');
INSERT INTO `blog_user_now` VALUES ('6', '陈凯歌', '134', '175', '511', '2');
INSERT INTO `blog_user_now` VALUES ('7', '林允儿', '127', '175', '512', '1');
INSERT INTO `blog_user_now` VALUES ('8', '周星驰', '122', '175', '513', '2');
INSERT INTO `blog_user_now` VALUES ('9', '朱茵', '110', '150', '514', '2');
INSERT INTO `blog_user_now` VALUES ('10', '谢安琪', '116', '175', '515', '2');
INSERT INTO `blog_user_now` VALUES ('11', '梁博', '188', '183', '516', '2');
INSERT INTO `blog_user_now` VALUES ('12', '陈坤', '226', '180', '517', '1');
INSERT INTO `blog_user_now` VALUES ('13', '周迅', '144', '158', '518', '1');
INSERT INTO `blog_user_now` VALUES ('14', '梁非凡', '188', '171', '519', '3');

-- ----------------------------
-- Table structure for blog_weekly_info
-- ----------------------------
DROP TABLE IF EXISTS `blog_weekly_info`;
CREATE TABLE `blog_weekly_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(255) NOT NULL,
  `username` varchar(30) NOT NULL,
  `week1` double DEFAULT NULL,
  `week2` double DEFAULT NULL,
  `week3` double DEFAULT NULL,
  `week4` double DEFAULT NULL,
  `week5` double DEFAULT NULL,
  `week6` double DEFAULT NULL,
  `week7` double DEFAULT NULL,
  `week8` double DEFAULT NULL,
  `choice_id` int(11) NOT NULL,
  `week0` double DEFAULT NULL,
  `week1_suggest` longtext,
  `week2_suggest` longtext,
  `week3_suggest` longtext,
  `week4_suggest` longtext,
  `week5_suggest` longtext,
  `week6_suggest` longtext,
  `week7_suggest` longtext,
  `week8_suggest` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `blog_weekly_info_choice_id_2161b288_fk_blog_item_id` (`choice_id`),
  CONSTRAINT `blog_weekly_info_choice_id_2161b288_fk_blog_item_id` FOREIGN KEY (`choice_id`) REFERENCES `blog_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blog_weekly_info
-- ----------------------------
INSERT INTO `blog_weekly_info` VALUES ('1', '31', '陈奕迅', '148.5', '142', '137', '133', null, null, null, null, '2', '155', '基本完成周训练量，但是需要注意饮食，控制摄入量', '干的不错', '还可以', '', '', null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('2', '503', '贾克斯', '148', null, null, null, null, null, null, null, '3', '156', null, null, null, null, null, null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('3', '504', '菲奥娜', '128', null, null, null, null, null, null, null, '4', '130', null, null, null, null, null, null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('4', '510', '张艺谋', '172', null, null, null, null, null, null, null, '5', '180', null, null, null, null, null, null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('5', '511', '陈凯歌', '145', '138', '134', '120.5', null, null, null, null, '2', '156', '本周减重11斤，再接再厉', '再接再厉，争取到10', '再接再厉', '', '', null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('6', '512', '林允儿', '132', '127', null, null, null, null, null, null, '1', '140', '', '', null, null, null, null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('7', '513', '周星驰', '135', '130', '122', '120', null, null, null, null, '2', '140', '需要加强局部训练，注意饮食', '加强上肢训练', '', '', '', null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('8', '514', '朱茵', '116', '113', '110', '108', null, null, null, null, '2', '120', '基本完成训练', '', '', '', '', null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('9', '515', '谢安琪', '125', '120', '116', '114', '113', null, null, null, '2', '130', '加强腰腹训练，注意饮食', '', '', '', '', null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('10', '516', '梁博', '211', '200', '188', '179', '170', null, null, null, '2', '220', '注意饮食平衡，劳逸结合，避免训练过度', '', '', '', '', null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('11', '517', '陈坤', '238', '226', null, null, null, null, null, null, '1', '246', '', '', null, null, null, null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('12', '518', '周迅', '150', '144', null, null, null, null, null, null, '1', '156', '', '', null, null, null, null, null, null);
INSERT INTO `blog_weekly_info` VALUES ('13', '519', '梁非凡', null, null, null, null, null, null, null, null, '3', '188', null, null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2017-12-08 11:08:42.295170', '1', 'rank object', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2017-12-08 11:08:52.005190', '2', 'rank object', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2017-12-08 11:09:01.171628', '3', 'rank object', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2017-12-08 11:10:49.512577', '1', '汪国强', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2017-12-08 11:11:23.086959', '2', '赵旭', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2017-12-10 06:19:12.498204', '1', 'userstest object', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2017-12-10 06:37:46.956857', '3', '栗子', '1', '[{\"added\": {}}]', '9', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('7', 'blog', 'admin');
INSERT INTO `django_content_type` VALUES ('15', 'blog', 'coach');
INSERT INTO `django_content_type` VALUES ('12', 'blog', 'iden');
INSERT INTO `django_content_type` VALUES ('14', 'blog', 'item');
INSERT INTO `django_content_type` VALUES ('8', 'blog', 'rank');
INSERT INTO `django_content_type` VALUES ('11', 'blog', 'testimgsrc');
INSERT INTO `django_content_type` VALUES ('9', 'blog', 'userinfo');
INSERT INTO `django_content_type` VALUES ('10', 'blog', 'userstest');
INSERT INTO `django_content_type` VALUES ('13', 'blog', 'user_now');
INSERT INTO `django_content_type` VALUES ('22', 'blog', 'week1');
INSERT INTO `django_content_type` VALUES ('19', 'blog', 'week2');
INSERT INTO `django_content_type` VALUES ('16', 'blog', 'week3');
INSERT INTO `django_content_type` VALUES ('23', 'blog', 'week4');
INSERT INTO `django_content_type` VALUES ('20', 'blog', 'week5');
INSERT INTO `django_content_type` VALUES ('21', 'blog', 'week6');
INSERT INTO `django_content_type` VALUES ('18', 'blog', 'week7');
INSERT INTO `django_content_type` VALUES ('17', 'blog', 'week8');
INSERT INTO `django_content_type` VALUES ('24', 'blog', 'weekly_info');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-12-08 11:05:48.629360');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-12-08 11:05:58.007374');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-12-08 11:06:00.033130');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-12-08 11:06:00.080341');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-12-08 11:06:01.146571');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-12-08 11:06:02.576422');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-12-08 11:06:02.777565');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-12-08 11:06:02.841611');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-12-08 11:06:03.390923');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-12-08 11:06:03.439957');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-12-08 11:06:03.495998');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-12-08 11:06:04.263886');
INSERT INTO `django_migrations` VALUES ('13', 'blog', '0001_initial', '2017-12-08 11:06:04.624162');
INSERT INTO `django_migrations` VALUES ('14', 'blog', '0002_auto_20171204_1215', '2017-12-08 11:06:04.871318');
INSERT INTO `django_migrations` VALUES ('15', 'blog', '0003_auto_20171204_1406', '2017-12-08 11:06:05.164524');
INSERT INTO `django_migrations` VALUES ('16', 'blog', '0004_auto_20171204_1418', '2017-12-08 11:06:05.379680');
INSERT INTO `django_migrations` VALUES ('17', 'blog', '0005_admin', '2017-12-08 11:06:05.687897');
INSERT INTO `django_migrations` VALUES ('18', 'blog', '0006_auto_20171208_1543', '2017-12-08 11:06:06.962801');
INSERT INTO `django_migrations` VALUES ('19', 'blog', '0007_auto_20171208_1550', '2017-12-08 11:06:07.210980');
INSERT INTO `django_migrations` VALUES ('20', 'blog', '0008_auto_20171208_1847', '2017-12-08 11:06:11.417759');
INSERT INTO `django_migrations` VALUES ('21', 'blog', '0009_auto_20171208_1850', '2017-12-08 11:06:12.986930');
INSERT INTO `django_migrations` VALUES ('22', 'blog', '0010_auto_20171208_1856', '2017-12-08 11:06:13.050975');
INSERT INTO `django_migrations` VALUES ('23', 'blog', '0011_auto_20171208_1902', '2017-12-08 11:06:13.197249');
INSERT INTO `django_migrations` VALUES ('24', 'blog', '0012_auto_20171208_1903', '2017-12-08 11:06:13.246015');
INSERT INTO `django_migrations` VALUES ('25', 'sessions', '0001_initial', '2017-12-08 11:06:14.150392');
INSERT INTO `django_migrations` VALUES ('26', 'blog', '0013_auto_20171210_1513', '2017-12-10 07:13:43.798099');
INSERT INTO `django_migrations` VALUES ('27', 'blog', '0014_auto_20171210_1853', '2017-12-10 10:54:03.355385');
INSERT INTO `django_migrations` VALUES ('28', 'blog', '0015_testimgsrc', '2017-12-22 10:10:28.857634');
INSERT INTO `django_migrations` VALUES ('29', 'blog', '0016_testimgsrc_name', '2017-12-22 10:51:40.502837');
INSERT INTO `django_migrations` VALUES ('30', 'blog', '0017_auto_20180314_1639', '2018-03-14 16:39:26.313064');
INSERT INTO `django_migrations` VALUES ('31', 'blog', '0018_auto_20180327_2022', '2018-03-27 20:22:41.325633');
INSERT INTO `django_migrations` VALUES ('32', 'blog', '0019_remove_admin_email', '2018-03-27 20:31:49.213872');
INSERT INTO `django_migrations` VALUES ('33', 'blog', '0020_auto_20180402_1504', '2018-04-02 15:05:08.774222');
INSERT INTO `django_migrations` VALUES ('34', 'blog', '0021_remove_user_now_uid', '2018-04-02 23:29:10.737321');
INSERT INTO `django_migrations` VALUES ('35', 'blog', '0022_user_now_uid', '2018-04-02 23:36:26.155249');
INSERT INTO `django_migrations` VALUES ('36', 'blog', '0023_user_now_choice', '2018-04-03 00:55:56.044713');
INSERT INTO `django_migrations` VALUES ('37', 'blog', '0024_weeek3_week1_week2_week4_week5_week6_week7_week8', '2018-04-03 12:53:41.080756');
INSERT INTO `django_migrations` VALUES ('38', 'blog', '0025_auto_20180403_1254', '2018-04-03 12:54:11.743688');
INSERT INTO `django_migrations` VALUES ('39', 'blog', '0026_auto_20180403_1609', '2018-04-03 16:09:27.555687');
INSERT INTO `django_migrations` VALUES ('40', 'blog', '0027_auto_20180403_1610', '2018-04-03 16:10:31.146785');
INSERT INTO `django_migrations` VALUES ('41', 'blog', '0028_auto_20180404_1557', '2018-04-04 15:57:40.952781');
INSERT INTO `django_migrations` VALUES ('42', 'blog', '0029_weekly_info_week0', '2018-04-04 16:16:49.757979');
INSERT INTO `django_migrations` VALUES ('43', 'blog', '0030_auto_20180410_1144', '2018-04-10 11:44:43.026424');
INSERT INTO `django_migrations` VALUES ('44', 'blog', '0031_auto_20180410_1319', '2018-04-10 13:19:57.426838');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('4l6sp1xuydnokrkn9t0se6s7r9eytu4i', 'YjNlNDY5ZGU4MDgzMjVlYjMxMTZjMTI2NjA0YzQ5NWU3ZDYxMDJlMzp7fQ==', '2017-12-26 23:10:12.292420');
INSERT INTO `django_session` VALUES ('93sc1pebyrvepoyxeoxupvnovsbg4jvg', 'NDQzMDYyZTFkZGZkZjAyYzgxODRjYmNiNGY3MjYzNGRmNGE5YzFmYjp7InVzZXJuYW1lIjoiemVueGlhb3hpYW4ifQ==', '2017-12-26 22:17:15.428407');
INSERT INTO `django_session` VALUES ('be5taytoxoopweox5eg5r414ww8a1oys', 'NWZmYTc1YzFjOWE0ZjhkZjljMTg3NDIzZDQ0MjAwNzBlYmFhMjI3Zjp7InVzZXJuYW1lIjoiXHU2ODgxXHU1MzVhIn0=', '2018-01-05 15:56:43.623773');
INSERT INTO `django_session` VALUES ('epndcjuf3gu6b67txkogfhwh3e4ab8io', 'MWQ4MDZhYzUyY2E3NGM0ODdlMDdmMDE3Y2ZlNWY4ZjIzYmMzYmFmNzp7InVzZXJuYW1lIjoiXHU2Yzg4XHU1NTJmXHU4NGVjIiwiaW5kZW50aWZ5IjoiXHU3YmExXHU3NDA2XHU1NDU4In0=', '2018-05-07 15:21:17.668228');
INSERT INTO `django_session` VALUES ('f8oxp8rdzyfzgaryae9wsz51gaknmf3k', 'NDI4MTAwYzkzNGNiYjM4ZWExNDRlZWZiYWY3M2FkYzc1YjQ2ZjFjODp7InVzZXJuYW1lIjoiMTEifQ==', '2018-01-08 14:52:34.912815');
INSERT INTO `django_session` VALUES ('g92smd5eejquahbv0tpnwaifugj0r7oy', 'YjNlNDY5ZGU4MDgzMjVlYjMxMTZjMTI2NjA0YzQ5NWU3ZDYxMDJlMzp7fQ==', '2018-01-05 10:03:09.462358');
INSERT INTO `django_session` VALUES ('mpkhj2ajh3zffwvvsechfbrapi4m6dk3', 'NWZmYTc1YzFjOWE0ZjhkZjljMTg3NDIzZDQ0MjAwNzBlYmFhMjI3Zjp7InVzZXJuYW1lIjoiXHU2ODgxXHU1MzVhIn0=', '2018-01-04 15:17:56.063193');
INSERT INTO `django_session` VALUES ('nozlrfx7akwlagls1msy2ettfi9dlibf', 'NmQ4YjA4NTM2MTkxYjQwOWY5Y2U0NTcyNTljYTYwOGU1NzQxZTU2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJ1c2VybmFtZSI6IjY2NiIsIl9hdXRoX3VzZXJfaGFzaCI6IjY5YTIyYTc0MzczNTEwMjgyOGUwMGUwYjA4MTFiZWQ4MmUyM2U5MzUifQ==', '2017-12-26 16:57:22.676264');
INSERT INTO `django_session` VALUES ('rvs898ddlrr84vrtbj8zxblblajiw9j7', 'OTgwMDFhN2M3YWVlN2YwZWQ1MWNmMjM0YTU3MGM1MDFmZjkzZWMzYjp7InVzZXJuYW1lIjoiXHU5NTEwXHU5NmVmIn0=', '2018-01-03 19:09:35.806612');
INSERT INTO `django_session` VALUES ('wge6pwtotqpg8eh3qg6dtpa6ptpj5qqz', 'OTdjNGQzOWZlMWZiMzdmYmI1NDk3Y2E4Y2E1ODdjOWQ4YTRjOGU2NTp7InVzZXJuYW1lIjoiXHU2YzZhXHU1NmZkXHU1ZjNhIn0=', '2018-02-08 16:22:36.152488');
