import boto3
import json
from botocore.exceptions import ClientError

iam_client = boto3.client('iam')

try:
    # Create IAM user
    user_name = "insecure_user"
    iam_client.create_user(UserName=user_name)
    print(f"IAM user {user_name} created.")

    # Define overly permissive policy
    full_access_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    # Create the policy
    policy_response = iam_client.create_policy(
        PolicyName='FullAdminAccessPolicy',
        PolicyDocument=json.dumps(full_access_policy)
    )
    policy_arn = policy_response['Policy']['Arn']

    # Attach the policy to the user
    iam_client.attach_user_policy(
        UserName=user_name,
        PolicyArn=policy_arn
    )
    print(f"Full admin access policy attached to {user_name}.")
except ClientError as e:
    print(f"Error creating user or policy: {e}")
