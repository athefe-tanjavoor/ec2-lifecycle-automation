import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region if needed

    # Describe all stopped instances
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    # Filter out instances that do NOT have a Name tag
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            tags = instance.get('Tags', [])
            name_tag = next((tag for tag in tags if tag['Key'] == 'Name'), None)
            if not name_tag:
                instance_ids.append(instance['InstanceId'])

    if not instance_ids:
        print("No stopped instances found without Name tag.")
        return {
            'statusCode': 200,
            'body': 'No stopped instances found without Name tag.'
        }

    # Start instances
    ec2.start_instances(InstanceIds=instance_ids)
    print(f"Started instances without Name tag: {instance_ids}")

    return {
        'statusCode': 200,
        'body': f'Started instances without Name tag: {instance_ids}'
    }
