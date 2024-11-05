# AWS recommends encrypting EBS volumes to protect data at rest. Creating an unencrypted volume is a misconfiguration that can lead to data exposure 
# if the volume is compromised. Here’s how to create an unencrypted volume.
# Setting Encrypted=False results in an unencrypted EBS volume, which may lead to unauthorized access to sensitive data if the volume is leaked or accessed.

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
