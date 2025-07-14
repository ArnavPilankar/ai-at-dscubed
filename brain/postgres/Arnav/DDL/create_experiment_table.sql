CREATE SCHEMA IF NOT EXISTS project_two;

CREATE TABLE IF NOT EXISTS project_two.Arnav (
    exp_id UUID PRIMARY KEY,
    exp_name TEXT NOT NULL,
    member_name TEXT NOT NULL,
    dataset_used TEXT NOT NULL,
    model_used TEXT NOT NULL,
    model_params JSON,
    accuracy FLOAT,
    remarks TEXT
);