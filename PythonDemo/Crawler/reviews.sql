DROP TABLE IF EXISTS "reviews";
CREATE TABLE "reviews" (
  "rid" integer NOT NULL,
  "fno" text,
  "uname" text,
  "star" text,
  "content" text,
  "votes" text,
  PRIMARY KEY ("rid")
);

PRAGMA foreign_keys = true;