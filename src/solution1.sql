with protocols_organized (protocol,client)
	as (
	SELECT
		protocol, client
		FROM traffic
		group by client, protocol
	)



SELECT
  distinct t.client,
  t.protocol
FROM traffic
INNER JOIN (
    SELECT
    STRING_AGG(protocol, ',') AS protocol, client
    FROM protocols_organized
    group by client
  ) AS t
ON traffic.client = t.client
ORDER BY client