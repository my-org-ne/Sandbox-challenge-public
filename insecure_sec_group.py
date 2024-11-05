import boto3
from botocore.exceptions import ClientError

ec2_client = boto3.client('ec2')

# Create a security group with an overly permissive inbound rule
try:
    response = ec2_client.create_security_group(
        GroupName='InsecureSecurityGroup',
        Description='Security group with overly permissive ingress rule',
        VpcId='vpc-12345678'  # Replace with a valid VPC ID
    )
    security_group_id = response['GroupId']
    print(f"Security Group {security_group_id} created.")

    # Add a rule that allows ingress from any IP on all ports (dangerous)
    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': '-1',  # '-1' allows all protocols
                'FromPort': 0,
                'ToPort': 65535,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Open to the world
            }
        ]
    )
    print(f"Ingress rule added to {security_group_id}, open to all IPs.")
except ClientError as e:
    print(f"Error with security group: {e}")
