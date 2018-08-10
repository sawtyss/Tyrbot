CREATE TABLE IF NOT EXISTS `news` (`news_id` INTEGER PRIMARY KEY AUTO_INCREMENT, `time` INT NOT NULL, `author` VARCHAR(30), `news` TEXT, `sticky` TINYINT NOT NULL, `deleted` TINYINT NOT NULL);
CREATE TABLE IF NOT EXISTS `news_read` (`char_id` INTEGER NOT NULL, `news_id` INTEGER NOT NULL);