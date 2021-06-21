
SELECT au.firstname || ' ' || au.lastname as FullName,
	   COUNT(ar.id) as NoOfArticles
FROM article ar
INNER JOIN author au ON ar.author_id = au.id
GROUP BY ar.author_id
ORDER BY FullName;

SELECT au.lastname, MAX(ar.id)
FROM author au
LEFT OUTER JOIN article ar ON ar.author_id = au.id
GROUP BY au.id
ORDER BY au.lastname DESC, au.firstname;
