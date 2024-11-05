ec2_client = boto3.client('ec2')

try:
    # Create an unencrypted EBS volume
    volume = ec2_client.create_volume(
        Size=10,  # Size in GiB
        AvailabilityZone='us-west-2a',  # Replace with a valid zone
        Encrypted=False  # Unencrypted volume
    )
    print(f"Unencrypted EBS volume {volume['VolumeId']} created.")
except ClientError as e:
    print(f"Error creating volume: {e}")
