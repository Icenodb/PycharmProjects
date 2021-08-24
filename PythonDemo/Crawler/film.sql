DROP TABLE IF EXISTS "film";
CREATE TABLE "film" (
  "fid" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "fno" text(20) NOT NULL,
  "fname" text(50) NOT NULL
);
INSERT INTO "film"("fno", "fname") VALUES ('30435124', '白蛇2');
INSERT INTO "film"("fno", "fname") VALUES ('35161768', '夏日友晴天 Luca');
INSERT INTO "film"("fno", "fname") VALUES ('35158124', '盛夏未来');


