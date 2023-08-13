SELECT
  client,
  STUFF(
    (SELECT  distinct protocol +', '
     FROM traffic
     WHERE client = a.client
     FOR XML PATH ('')),
    1,
    0,
    '') AS [protocol]
FROM traffic AS a
GROUP BY client
ORDER BY client