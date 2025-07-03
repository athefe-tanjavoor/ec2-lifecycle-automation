import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region if needed

    # Define tag key and value
    tag_key = 'Name'
    tag_value = 'TagName'  # Change to your actual tag value

    # Find running instances with the specific tag
    response = ec2.describe_instances(
        Filters=[
            {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    # Extract instance IDs
    instance_ids = [
        instance['InstanceId']
        for reservation in response['Reservations']
        for instance in reservation['Instances']
    ]

    if not instance_ids:
        print(f"No running instances found with tag {tag_key}={tag_value}")
        return {
            'statusCode': 200,
            'body': f'No running instances found with tag {tag_key}={tag_value}'
        }

    # Stop instances
    ec2.stop_instances(InstanceIds=instance_ids)
    print(f"Stopped instances: {instance_ids}")

    return {
        'statusCode': 200,
        'body': f'Stopped instances: {instance_ids}'
    }