INSERT INTO `dojos` (`nombre`)
VALUES ('Chile'), ('Canada'), ('Online');

SET SQL_SAFE_UPDATES = 0;

INSERT INTO `dojos` (`nombre`)
VALUES ('Chile'), ('Canada'), ('Online');

SELECT * FROM `dojos`;

INSERT INTO `ninja` (`nombre`, `apellido`, `edad`, `id_del_dojo`)
VALUES ("Juan", "Perez", 21, 4), ("Pedro", "Diaz", 32, 4), ("Diego", "Chiaz", 22, 4);

INSERT INTO `ninja` (`nombre`, `apellido`, `edad`, `id_del_dojo`)
VALUES ("Nicolas", "Che", 34, 5), ("Jose", "Dio", 42, 5), ("Pablo", "Solar", 28, 5);

INSERT INTO `ninja` (`nombre`, `apellido`, `edad`, `id_del_dojo`)
VALUES ("Luis", "Gonzales", 24, 6), ("Jose", "Dio", 29, 6), ("Pablo", "Solar", 19, 6);

SELECT * FROM `dojos`
LEFT JOIN `ninja` ON `dojos`.`id` = `ninjas`.`id_del_dojo`
WHERE `dojos`.`id` = 4;

SELECT * FROM `dojos`
LEFT JOIN `ninja` ON `dojos`.`id` = `ninjas`.`id_del_dojo`
WHERE `dojos`.`id` = (SELECT `id` FROM `dojos` ORDER BY `id` DESC LIMIT 1);

SELECT * FROM `dojos`
WHERE `dojos`.`id` = (SELECT `id_del_dojo` FROM `ninjas` ORDER BY `id_del_dojo` DESC LIMIT 1);
