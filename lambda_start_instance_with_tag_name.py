import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your region

    # Define the tag key and value
    tag_key = 'Name'
    tag_value = 'TagName'  # Replace with your actual tag value

    # Find stopped instances with the given tag
    response = ec2.describe_instances(
        Filters=[
            {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    # Extract instance IDs
    instance_ids = [
        instance['InstanceId']
        for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]

    if not instance_ids:
        print(f"No stopped instances found with tag {tag_key}={tag_value}")
        return {
            'statusCode': 200,
            'body': f'No stopped instances found with tag {tag_key}={tag_value}'
        }

    # Start instances
    ec2.start_instances(InstanceIds=instance_ids)
    print(f"Started instances: {instance_ids}")

    return {
        'statusCode': 200,
        'body': f'Started instances: {instance_ids}'
    }
