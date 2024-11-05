import boto3
from botocore.exceptions import ClientError

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

# Define the bucket name
bucket_name = "my-public-bucket-example"

# Create the S3 bucket
try:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} created successfully.")
except ClientError as e:
    print(f"Error creating bucket: {e}")

# Define a policy that allows public access (Insecure configuration)
public_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadWrite",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject", "s3:PutObject"],
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

# Apply the public access policy
try:
    s3_client.put_bucket_policy(
        Bucket=bucket_name,
        Policy=json.dumps(public_policy)
    )
    print(f"Public access policy applied to {bucket_name}.")
except ClientError as e:
    print(f"Error applying policy: {e}")
