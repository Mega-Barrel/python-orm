
-- Table Schema
CREATE TABLE "hero" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "secret_name" TEXT NOT NULL,
    "age" INTEGER,
    "team_id" INTEGER,
    PRIMARY KEY ("id")
    FOREIGN KEY(team_id) REFERENCES team(id)
);

CREATE TABLE "team" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "headquarters" TEXT NOT NULL,
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

-- Filter data
SELECT
    id,
    name,
    secret_name,
    age
FROM
    hero
WHERE
    name = 'Deadpond'
;

-- Creating Index on table
CREATE INDEX ix_hero_name
ON hero (name);

-- Update statement
UPDATE 
    hero
SET 
    age = 16
WHERE
    name = 'Spider-Boy'
;

-- Delete statement
DELETE
FROM 
    hero
WHERE
    name = "Spider-Yongster"
;