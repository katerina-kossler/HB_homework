-- Intermediate SQL concepts for Dig Deeper Study Hall


-- Simple views can be editable

CREATE VIEW podlings AS SELECT * FROM prisoners WHERE species_code='p';



-- Can use "check constraints" for validation

ALTER TABLE consumption ADD CONSTRAINT check_qty CHECK (qty > 0);



-- Can use UNIQUE for validation

ALTER TABLE prisoners ADD cage_seq INTEGER CHECK (cage_seq BETWEEN 1 AND 5);
UPDATE prisoners SET cage_seq = prisoner_id;  -- seed wiht sample values
ALTER TABLE prisoners ALTER cage_seq SET NOT NULL;
ALTER TABLE prisoners ADD CONSTRAINT check_cage_seq UNIQUE(cage_id, cage_seq);



-- Can log cage changes

CREATE TABLE cage_log (cage_log_id SERIAL PRIMARY KEY, 
	               prisoner_id INTEGER NOT NULL REFERENCES prisoners,
		       old_cage_id INTEGER REFERENCES cages,
		       new_cage_id INTEGER REFERENCES cages,
		       moved_at TIMESTAMP DEFAULT current_timestamp);

CREATE FUNCTION log_prisoner_move() RETURNS trigger AS '
  BEGIN
    IF NEW.cage_id <> OLD.cage_id THEN
      INSERT INTO cage_log (prisoner_id, old_cage_id, new_cage_id) 
        VALUES (NEW.prisoner_id, OLD.cage_id, NEW.cage_id);
    END IF;
  RETURN NEW;
  END;
' LANGUAGE 'plpgsql';

CREATE TRIGGER log_prisoner_move
  AFTER INSERT OR UPDATE OR DELETE
  ON prisoners
  FOR EACH ROW EXECUTE PROCEDURE log_prisoner_move();

-- Create some examples of prisoners moving so we can see log of this
UPDATE prisoners SET cage_id = 4 WHERE prisoner_id = 1;
UPDATE prisoners SET cage_id = 1 WHERE prisoner_id = 1;
	


-- Materialized view example

CREATE MATERIALIZED VIEW prisoner_report_mv AS
  SELECT prisoner_id, 
    species.name AS species, 
    arrived_at::date AS arrival_date, 
    cage_id, 
    essence_in, 
    essence_in - COALESCE(sum(consumption.qty), 0) AS essence, 
    essence_in - COALESCE(sum(consumption.qty), 0) <= 0 AS is_dead 
  FROM prisoners 
    JOIN species USING (species_code) 
    LEFT JOIN consumption USING (prisoner_id) 
  GROUP BY prisoner_id, species.name 
  ORDER BY prisoner_id;

