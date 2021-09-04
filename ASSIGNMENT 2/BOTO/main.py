import boto3,boto.ec2

def create_instance():

    script  = '''
        #!/bin/sh
        yum -y install httpd
        systemctl enable httpd
        systemctl start httpd.service

        mkdir dist
        cd dist
        wget https://lapy113.s3.amazonaws.com/dist.zip
        unzip dist.zip
        cd dist

        cp -r * /var/www/html        
    '''

    try:
        resource_ec2 = boto3.resource('ec2')
        response = resource_ec2.create_instances(
            ImageId='ami-0c2b8ca1dad447f8a',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='CS351-SG1',
            SecurityGroups=['launch-wizard-1'],
            UserData=script
        )
        print(response)
        instance = response[0]
        print('Instance created.. waiting to be in running state')
        instance.wait_until_running()
        print('Instance in running.')
        
        print('public dns address: ', get_public_ip(instance))
        
    except Exception as e:
        print(e)

def start_ec2_instance() :
    try:
        resource_ec2 = boto3.client('ec2')
        instance_id = resource_ec2.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
        # instance_id = 'i-0cc89f742692b78c8'
        resource_ec2.start_instances(InstanceIds=[instance_id])
    except Exception as e:
        print(e)

def get_public_ip(inst):
    client = boto3.client('ec2')
    response = client.describe_instances(InstanceIds=[inst.instance_id])
    public_ipvp4 = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return public_ipvp4

# start_ec2_instance()
create_instance()