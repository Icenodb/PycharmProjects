
DROP TABLE IF EXISTS "comments";
CREATE TABLE "comments" (
  "cid" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "fno" text(20) NOT NULL,
  "content" text NOT NULL,
  "star" text(10) NOT NULL,
  "votes" integer NOT NULL
);
