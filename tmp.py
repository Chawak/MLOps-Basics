import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('gmytestbucket')
for obj in bucket.objects.all():
    print(obj.key)