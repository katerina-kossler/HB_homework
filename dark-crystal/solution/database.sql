-- PostgreSQL-flavored solution for the Dark Crystal

CREATE TABLE cages (
    cage_id SERIAL PRIMARY KEY
);


CREATE TABLE species (
    species_code VARCHAR(5) PRIMARY KEY,
    name VARCHAR(20) UNIQUE,
    max_essence INTEGER NOT NULL
);


CREATE TABLE prisoners (
    prisoner_id SERIAL PRIMARY KEY,
    species_code VARCHAR(5) NOT NULL REFERENCES species,
    arrived_at TIMESTAMP DEFAULT current_timestamp,
    cage_id INTEGER NOT NULL REFERENCES cages,
    essence_in INTEGER NOT NULL
);


CREATE TABLE skeksis (
    skeksis_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE consumption (
    consumption_id SERIAL NOT NULL,
    consumption_at TIMESTAMP DEFAULT current_timestamp,
    qty INTEGER NOT NULL,
    skeksis_id INTEGER NOT NULL REFERENCES skeksis,
    prisoner_id INTEGER NOT NULL REFERENCES prisoners
);


-- Add species

INSERT INTO species VALUES ('g', 'Gelfling', 10000);
INSERT INTO species VALUES ('p', 'Podling', 500);

-- Add five cages

INSERT INTO cages DEFAULT VALUES;
INSERT INTO cages DEFAULT VALUES;
INSERT INTO cages DEFAULT VALUES;
INSERT INTO cages DEFAULT VALUES;
INSERT INTO cages DEFAULT VALUES;


-- Add five sample prisoners

INSERT INTO prisoners (species_code, cage_id, essence_in) VALUES ('p', 1, 100);
INSERT INTO prisoners (species_code, cage_id, essence_in) VALUES ('p', 1, 100);
INSERT INTO prisoners (species_code, cage_id, essence_in) VALUES ('p', 2, 100);
INSERT INTO prisoners (species_code, cage_id, essence_in) VALUES ('g', 1, 1000);
INSERT INTO prisoners (species_code, cage_id, essence_in) VALUES ('g', 2, 1000);


-- Add five sample skeksis

INSERT INTO skeksis (name) VALUES ('Scrawny');
INSERT INTO skeksis (name) VALUES ('Slimy');
INSERT INTO skeksis (name) VALUES ('Screechy');
INSERT INTO skeksis (name) VALUES ('Slappy');
INSERT INTO skeksis (name) VALUES ('Sketchy');


-- Add sample consumptions

INSERT INTO consumption (prisoner_id, skeksis_id, qty) VALUES (1, 1, 50);
INSERT INTO consumption (prisoner_id, skeksis_id, qty) VALUES (1, 1, 50);
INSERT INTO consumption (prisoner_id, skeksis_id, qty) VALUES (2, 1, 80);
INSERT INTO consumption (prisoner_id, skeksis_id, qty) VALUES (4, 2, 50);
INSERT INTO consumption (prisoner_id, skeksis_id, qty) VALUES (5, 3, 50);



-- Create some useful views

CREATE VIEW consumption_battle AS
 SELECT skeksis_id,
    skeksis.name,
    count(consumption_id) AS num,
    max(qty) AS biggest,
    sum(qty) AS total
   FROM skeksis
     LEFT JOIN consumption USING (skeksis_id)
     LEFT JOIN prisoners USING (prisoner_id)
  GROUP BY skeksis_id;


CREATE VIEW cage_report AS
  SELECT cage_id,
    count(prisoner_id) AS num_prisoners
  FROM cages
    LEFT JOIN prisoners USING (cage_id)
  GROUP BY cage_id
  ORDER BY cage_id;


CREATE VIEW prisoner_report AS
  SELECT prisoner_id, 
    species.name AS species, 
    arrived_at::date AS arrival_date, 
    cage_id, 
    essence_in, 
    essence_in - coalesce(sum(consumption.qty), 0) AS essence, 
    essence_in - coalesce(sum(consumption.qty), 0) = 0 AS is_dead 
  FROM prisoners 
    JOIN species USING (species_code) 
    LEFT JOIN consumption USING (prisoner_id) 
  GROUP BY prisoner_id, species.name 
  ORDER BY prisoner_id;
