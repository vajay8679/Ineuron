-- Adminer 4.8.1 MySQL 8.0.27-0ubuntu0.21.04.1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1,	'Can add log entry',	1,	'add_logentry'),
(2,	'Can change log entry',	1,	'change_logentry'),
(3,	'Can delete log entry',	1,	'delete_logentry'),
(4,	'Can view log entry',	1,	'view_logentry'),
(5,	'Can add permission',	2,	'add_permission'),
(6,	'Can change permission',	2,	'change_permission'),
(7,	'Can delete permission',	2,	'delete_permission'),
(8,	'Can view permission',	2,	'view_permission'),
(9,	'Can add group',	3,	'add_group'),
(10,	'Can change group',	3,	'change_group'),
(11,	'Can delete group',	3,	'delete_group'),
(12,	'Can view group',	3,	'view_group'),
(13,	'Can add user',	4,	'add_user'),
(14,	'Can change user',	4,	'change_user'),
(15,	'Can delete user',	4,	'delete_user'),
(16,	'Can view user',	4,	'view_user'),
(17,	'Can add content type',	5,	'add_contenttype'),
(18,	'Can change content type',	5,	'change_contenttype'),
(19,	'Can delete content type',	5,	'delete_contenttype'),
(20,	'Can view content type',	5,	'view_contenttype'),
(21,	'Can add session',	6,	'add_session'),
(22,	'Can change session',	6,	'change_session'),
(23,	'Can delete session',	6,	'delete_session'),
(24,	'Can view session',	6,	'view_session'),
(25,	'Can add brand',	7,	'add_brand'),
(26,	'Can change brand',	7,	'change_brand'),
(27,	'Can delete brand',	7,	'delete_brand'),
(28,	'Can view brand',	7,	'view_brand'),
(29,	'Can add model',	8,	'add_model'),
(30,	'Can change model',	8,	'change_model'),
(31,	'Can delete model',	8,	'delete_model'),
(32,	'Can view model',	8,	'view_model');

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1,	'admin',	'logentry'),
(3,	'auth',	'group'),
(2,	'auth',	'permission'),
(4,	'auth',	'user'),
(5,	'contenttypes',	'contenttype'),
(7,	'mobile',	'brand'),
(8,	'mobile',	'model'),
(6,	'sessions',	'session');

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1,	'contenttypes',	'0001_initial',	'2022-05-20 05:34:14.549410'),
(2,	'auth',	'0001_initial',	'2022-05-20 05:34:17.582306'),
(3,	'admin',	'0001_initial',	'2022-05-20 05:34:18.077277'),
(4,	'admin',	'0002_logentry_remove_auto_add',	'2022-05-20 05:34:18.109125'),
(5,	'admin',	'0003_logentry_add_action_flag_choices',	'2022-05-20 05:34:18.139340'),
(6,	'contenttypes',	'0002_remove_content_type_name',	'2022-05-20 05:34:18.505906'),
(7,	'auth',	'0002_alter_permission_name_max_length',	'2022-05-20 05:34:18.739451'),
(8,	'auth',	'0003_alter_user_email_max_length',	'2022-05-20 05:34:18.778144'),
(9,	'auth',	'0004_alter_user_username_opts',	'2022-05-20 05:34:18.794740'),
(10,	'auth',	'0005_alter_user_last_login_null',	'2022-05-20 05:34:18.971938'),
(11,	'auth',	'0006_require_contenttypes_0002',	'2022-05-20 05:34:18.981735'),
(12,	'auth',	'0007_alter_validators_add_error_messages',	'2022-05-20 05:34:19.016607'),
(13,	'auth',	'0008_alter_user_username_max_length',	'2022-05-20 05:34:19.213308'),
(14,	'auth',	'0009_alter_user_last_name_max_length',	'2022-05-20 05:34:19.455550'),
(15,	'auth',	'0010_alter_group_name_max_length',	'2022-05-20 05:34:19.494356'),
(16,	'auth',	'0011_update_proxy_permissions',	'2022-05-20 05:34:19.508841'),
(17,	'auth',	'0012_alter_user_first_name_max_length',	'2022-05-20 05:34:19.717967'),
(18,	'mobile',	'0001_initial',	'2022-05-20 05:34:20.083486'),
(19,	'sessions',	'0001_initial',	'2022-05-20 05:34:20.281844');

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `mobile_brand`;
CREATE TABLE `mobile_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created` date DEFAULT NULL,
  `company_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `mobile_brand` (`id`, `name`, `created`, `company_name`) VALUES
(1,	'OnePlus Nord',	'2022-05-20',	'OnePlus'),
(2,	'realme 9',	'2022-05-20',	'realme India'),
(3,	'OnePlus CE',	'2022-05-20',	'OnePlus'),
(4,	'OnePlus Nord',	'2022-05-20',	'OnePlus'),
(5,	'realme A10',	'2022-05-20',	'realme India'),
(6,	'OPPO A',	'2022-05-12',	'OPPO'),
(7,	'VIVO Y',	'2022-05-20',	'VIVO');

DROP TABLE IF EXISTS `mobile_model`;
CREATE TABLE `mobile_model` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` varchar(10) NOT NULL,
  `launch_date` date DEFAULT NULL,
  `brand_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobile_model_brand_id_c6eadb09_fk_mobile_brand_id` (`brand_id`),
  CONSTRAINT `mobile_model_brand_id_c6eadb09_fk_mobile_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `mobile_brand` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `mobile_model` (`id`, `name`, `price`, `launch_date`, `brand_id`) VALUES
(1,	'realme Narzo 10A',	'11500',	'2022-05-20',	2),
(2,	'realme Narzo 10',	'9990',	'2022-05-18',	5),
(3,	'OnePlus Nord 9',	'25900',	'2022-05-18',	1),
(4,	'VIVO Y22',	'32999',	'2022-05-18',	7);

-- 2022-05-20 06:27:53
