
-- Table Schema
CREATE TABLE "hero" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "secret_name" TEXT NOT NULL,
    "age" INTEGER,
    PRIMARY KEY ("id")
);

-- Insert data into table
INSERT INTO "hero" (
    "name",
    "secret_name"
) VALUES (
    "Deadpond",
    "Dive Wilson"
);

-- Read Data from Table
SELECT
    id,
    name,
    secret_name,
    age
FROM
    hero
;