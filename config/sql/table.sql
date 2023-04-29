CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE item (
    id          UUID                     NOT NULL DEFAULT uuid_generate_v4(),
    name        TEXT                     NOT NULL,
    description TEXT,
    state       TEXT                     NOT NULL -- ENUM: TODO, IN_PROGRESS, or DONE
);
