from neo4j import GraphDatabase

# Replace these with your Aura credentials
uri = "neo4j+ssc://a2998625.databases.neo4j.io"
user = "neo4j"
password = "FRrT9EmOjirmkCWlD3m6d1V7MViYYrbkZjCj0hrSWYs"
database = "neo4j"  # check Aura dashboard for exact name

driver = GraphDatabase.driver(uri, auth=(user, password))

try:
    with driver.session(database=database) as session:
        result = session.run("RETURN 1 AS test")
        print("Connection successful! Test query result:", result.single()["test"])
except Exception as e:
    print("Connection failed:", e)
finally:
    driver.close()
