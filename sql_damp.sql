BEGIN TRANSACTION;CREATE TABLE cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );INSERT INTO "cars" VALUES(1,'Audi',52642);INSERT INTO "cars" VALUES(2,'Mersedes',57127);INSERT INTO "cars" VALUES(3,'Skoda',9000);INSERT INTO "cars" VALUES(4,'Volvo',29000);INSERT INTO "cars" VALUES(5,'Bentley',350000);DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('cars',5);COMMIT;