DROP TABLE IF EXISTS "film";
CREATE TABLE "film" (
  "fid" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "fno" text(20) NOT NULL,
  "fname" text(50) NOT NULL
);
