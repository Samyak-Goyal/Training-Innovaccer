import boto.ec2

conn = boto.ec2.connect_to_region("us-east-1",
    aws_access_key_id='AKIAR6SBPFMCNJIK4DFT',
   aws_secret_access_key='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')

conn = boto.ec2.connect_to_region("us-west-2")

def runInst():
    # conn.run_instances('04505e74c0741db8d')

    conn.run_instances(
            '04505e74c0741db8d',
            # key_name='myKey',
            instance_type='t2.micro',
            # security_groups=['your-security-group-here']
            )

def getAllInst():
    reservations = conn.get_all_reservations()
    instances = reservations[0].instances
    # print(instances)
    inst = instances[0]
    print(inst.instance_type)
    print(inst.placement)


def stopInst(instId):
    conn.stop_instances(instance_ids=[instId])

def termInst(instId):    
    conn.terminate_instances(instance_ids=[instId])

def checkStatus():
    statuses = conn.get_all_instance_status()
    print(statuses)

def createVol():
    vol = conn.create_volume(50, "us-west-2")
    return vol



