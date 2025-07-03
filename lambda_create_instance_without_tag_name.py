import boto3

def lambda_handler(event, context):
    # Initialize the Boto3 client for EC2
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    # Define EC2 instance parameters
    image_id = 'ami-05ffe3c48a9991133'  # Replace with your desired AMI ID
    instance_type = 't2.micro'
    key_name = 'linux-KeyPair'
    security_group_ids = ['sg-0a69b77ea418a9373']  # Replace with your security group IDs
    subnet_id = 'subnet-0ef367ce54a4b8a22'  # Replace with your subnet ID

    # Create EC2 instance
    response = ec2_client.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    print("EC2 instance created:", instance_id)
    
    return {
        'statusCode': 200,
        'body': 'EC2 instance creation successful'
    }