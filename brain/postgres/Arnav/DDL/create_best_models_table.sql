CREATE TABLE IF NOT EXISTS project_two.arnav_best_models AS
SELECT DISTINCT ON (dataset_used)
    dataset_used,
    model_used,
    accuracy AS best_accuracy,
    exp_id AS best_run_id
FROM project_two.arnav
ORDER BY dataset_used, accuracy DESC;
