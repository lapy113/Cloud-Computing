import boto3

#base64 encoded script
my_script = 'IyEvYmluL3NoCnl1bSAteSBpbnN0YWxsIGh0dHBkCnN5c3RlbWN0bCBlbmFibGUgaHR0cGQKc3lzdGVtY3RsIHN0YXJ0IGh0dHBkLnNlcnZpY2UKCm1rZGlyIGRpc3QKY2QgZGlzdAp3Z2V0IGh0dHBzOi8vbGFweTExMy5zMy5hbWF6b25hd3MuY29tL2Rpc3QuemlwCnVuemlwIGRpc3QuemlwCmNkIGRpc3QKCmNwIC1yICogL3Zhci93d3cvaHRtbA=='

def create_launch_template() :
    print('Creating Launch template')
    template_name = 'my-t2micro-template'
    ec2_client = boto3.client('ec2')
    try :
        response = ec2_client.create_launch_template(
            LaunchTemplateName=template_name,
            LaunchTemplateData={
                'ImageId' : 'ami-0c2b8ca1dad447f8a',
                'InstanceType':'t2.micro',
                'KeyName' : 'CS351-SG1',
                'UserData': my_script,
                'SecurityGroupIds':['sg-07920ae5008337d63']
            }
        )
        template_id = response['LaunchTemplate']['LaunchTemplateId']
        print('Template id = ',template_id," template name = ",template_name)
        return template_id, template_name

    except Exception as e:
        print('There is already launch template with the name ',template_name)
        response = ec2_client.describe_launch_templates(
            LaunchTemplateNames = [template_name]
        )
        template_id = response['LaunchTemplates'][0]['LaunchTemplateId']
        return template_id,template_name

def create_autoscaling_group():
    print('creating autoscaling group')
    launch_id , launch_name = create_launch_template()
    client = boto3.client('autoscaling')

    response = client.create_auto_scaling_group(
        AutoScalingGroupName = 'my-autoscaling-group',
        LaunchTemplate = {
            'LaunchTemplateId':launch_id
        },
        MinSize = 1,
        MaxSize = 3,
        DesiredCapacity = 2,
        AvailabilityZones = ['us-east-1c']
    )

    if str(response['ResponseMetadata']['HTTPStatusCode']) =='200':
        print('Succesfully created autoscaling group')
        return True
    else :
        print('Failed')
        return False

def scaleup_policy() :
    print('creating scale up policy')
    client = boto3.client('autoscaling')

    response = client.put_scaling_policy(
        AutoScalingGroupName = 'my-autoscaling-group',
        PolicyName = 'Scale-up-policy',
        AdjustmentType = 'ChangeInCapacity',
        ScalingAdjustment = 1,
        Cooldown = 60,
        
    )
    if str(response['ResponseMetadata']['HTTPStatusCode']) =='200':
        print('Succesfully created scaleup policy')
        return True
    else :
        print('Failed')
        return False

def scaledown_policy() :
    print('creating scale down policy')
    client = boto3.client('autoscaling')

    response = client.put_scaling_policy(
        AutoScalingGroupName = 'my-autoscaling-group',
        PolicyName = 'Scale-down-policy',
        AdjustmentType = 'ChangeInCapacity',
        ScalingAdjustment = -1,
        Cooldown = 60,
        
    )
    if str(response['ResponseMetadata']['HTTPStatusCode']) =='200':
        print('Succesfully created scaledown policy')
        return True
    else :
        print('Failed')
        return False

def create_scale_up_alarm() :
    scaleup_policy()
    autoscaling_client = boto3.client('autoscaling')
    action = autoscaling_client.describe_policies()['ScalingPolicies'][1]['PolicyARN']

    client = boto3.client('cloudwatch')
    response = client.put_metric_alarm(
        AlarmName = 'Scale-up-alarm-HighCpu',
        ActionsEnabled = True,
        AlarmActions = [action],
        MetricName = 'CPUUtilization',
        Namespace = 'AWS/EC2',
        EvaluationPeriods = 1,
        Period = 60,
        Statistic='Average',
        Threshold = 70.0,
        ComparisonOperator = 'GreaterThanOrEqualToThreshold',
        Dimensions=[
            {
            'Name': 'AutoScalingGroupName',
            'Value': 'my-autoscaling-group'
            },
        ],
        Unit='Percent'
    )
    if str(response['ResponseMetadata']['HTTPStatusCode']) =='200':
        print('Succesfully created Alarm')
        return True
    else :
        print('Failed')
        return False

def create_scale_down_alarm() :
    scaledown_policy()
    autoscaling_client = boto3.client('autoscaling')
    action = autoscaling_client.describe_policies()['ScalingPolicies'][0]['PolicyARN']

    client = boto3.client('cloudwatch')
    response = client.put_metric_alarm(
        AlarmName = 'Scale-down-alarm-LowCpu',
        ActionsEnabled = True,
        AlarmActions = [action],
        MetricName = 'CPUUtilization',
        Namespace = 'AWS/EC2',
        EvaluationPeriods = 1,
        Period = 60,
        Statistic='Average',
        Threshold = 20.0,
        ComparisonOperator = 'LessThanOrEqualToThreshold',
        Dimensions=[
            {
            'Name': 'AutoScalingGroupName',
            'Value': 'my-autoscaling-group'
            },
        ],
        Unit='Percent'
    )
    if str(response['ResponseMetadata']['HTTPStatusCode']) =='200':
        print('Succesfully created Alarm')
        return True
    else :
        print('Failed')
        return False

# create_autoscaling_group()
 
create_scale_up_alarm()
create_scale_down_alarm()


