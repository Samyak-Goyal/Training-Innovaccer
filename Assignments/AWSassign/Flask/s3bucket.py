import boto3

s3 = boto3.client('s3')


def createBucket():
    s3.create_bucket(Bucket='my-bucket')

def lsitBucket():
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)  
