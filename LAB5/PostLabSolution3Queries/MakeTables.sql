CREATE TABLE ADVENTURE_TRIP (
    TRIP_ID DECIMAL(3,0) NOT NULL,  -- Trip ID (primary key)
    TRIP_NAME VARCHAR(75),          -- Trim name
    START_LOCATION CHAR(50),        -- Start location for trip
    STATE CHAR(2),                  -- Trip State
    DISTANCE NUMBER(4, 0),          -- Distance (length) of trip
    MAX_GRP_SIZE NUMBER(4, 0),      -- Maximum number of persons
    TYPE CHAR(20),                  -- Trip type
    SEASON CHAR(20),                -- Trip season
);