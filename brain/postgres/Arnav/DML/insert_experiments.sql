
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

INSERT INTO project_two.arnav (
    exp_id,
    exp_name,
    member_name,
    dataset_used,
    model_used,
    model_params,
    accuracy,
    remarks
)
VALUES(
    uuid_generate_v4(),
    'word predict',
    'Arnav',
    'PreTrained',
    'TFBertForMaskedLM',
    '{"model": "bert-base-uncased"}',
    0.79,
    'predicting masked words'
    ),
    (
    uuid_generate_v4(),
    'traffic signage',
    'Arnav',
    'gtsrb',
    'CNN',
    '{"epochs": 10, "optimiser": "adam", "loss": "categorical_crossentropy"}',
    0.81,
    'identification of traffic signs'
    );
