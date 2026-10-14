SELECT DISTINCT sr.customer_id, sr.survey_id
FROM (
    SELECT customer_id,
           survey_id,
           RANK() OVER (
               PARTITION BY survey_id
               ORDER BY score DESC
           ) AS rnk
    FROM survey_results
    WHERE score IS NOT NULL
) AS sr
WHERE sr.rnk = 1
ORDER BY sr.survey_id, sr.customer_id;
 