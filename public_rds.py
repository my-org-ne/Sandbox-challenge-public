"""
Setting a database instance to be publicly accessible increases the risk of data breaches. Here’s an example of creating a publicly accessible RDS instance.
Setting 'PubliclyAccessible=True' makes the database available over the internet, which can expose it to unauthorized access.
"""

rds_client = boto3.client('rds')

try:
    # Create an RDS instance with public accessibility
    db_instance = rds_client.create_db_instance(
        DBName='testdb',
        DBInstanceIdentifier='insecure-rds-instance',
        MasterUsername='admin',
        MasterUserPassword='password123',  # Avoid weak passwords in real setups
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        AllocatedStorage=20,
        PubliclyAccessible=True  # Publicly accessible
    )
    print(f"Public RDS instance {db_instance['DBInstanceIdentifier']} created.")
except ClientError as e:
    print(f"Error creating RDS instance: {e}")
