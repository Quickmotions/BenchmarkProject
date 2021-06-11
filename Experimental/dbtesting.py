import csv
import psycopg2 
conn = psycopg2.connect("host=ec2-54-216-17-9.eu-west-1.compute.amazonaws.com dbname=d6jfdmfbk8m22t user=ydngonadspindw password=132f2ff02391469a239e18f0ef884109a2dc7b5cea958ae82ae7851b6229f29d")
cur = conn.cursor()
insert_query = "INSERT INTO test VALUES {}".format("(10, 'hello@callumg.com', 'Some NamE', '123 Fake St.')")
select_query = "SELECT * FROM test"
with open('Experimental/user.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO test VALUES (%s, %s, %s, %s)",
        row
    )
conn.commit()