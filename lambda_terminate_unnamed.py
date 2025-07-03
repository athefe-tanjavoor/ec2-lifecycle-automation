import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # Get all instances that are not yet terminated
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['pending', 'running', 'stopping', 'stopped']
            }
        ]
    )

    # Extract instance IDs that do NOT have a 'Name' tag
    instance_ids_to_terminate = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            tags = instance.get('Tags', [])
            has_name_tag = any(tag['Key'] == 'Name' for tag in tags)
            if not has_name_tag:
                instance_ids_to_terminate.append(instance['InstanceId'])

    # Terminate the instances without Name tag
    if instance_ids_to_terminate:
        ec2.terminate_instances(InstanceIds=instance_ids_to_terminate)
        print("Terminating instances without Name tag:", instance_ids_to_terminate)
        return {
            'statusCode': 200,
            'body': f'Terminated instances without Name tag: {instance_ids_to_terminate}'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No unnamed instances found to terminate.'
        }


