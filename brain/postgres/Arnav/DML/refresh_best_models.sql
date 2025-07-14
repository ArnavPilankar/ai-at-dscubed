TRUNCATE TABLE project_two.arnav_best_models;

INSERT INTO project_two.arnav_best_models
SELECT DISTINCT ON (dataset_used)
    dataset_used,
    model_used,
    accuracy AS best_accuracy,
    exp_id AS best_run_id
FROM project_two.arnav
ORDER BY dataset_used, accuracy DESC;
