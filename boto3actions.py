import boto3

# Initialize interfaces
s3Client = boto3.client('s3')
s3Resource = boto3.resource('s3')

# Create byte string to send to our bucket
putMessage = b'Hi! I came from Boto3!'

# put_object
response = s3Client.put_object(
    Body = putMessage,
    Bucket = 'my-bucket',
    Key = 'my-file'
)

print(response)

# copy
toCopy = {
    'Bucket': 'my-bucket',
    'Key': 'my-file'
}

s3Resource.meta.client.copy(toCopy, 'my-bucket', 'boto3copy.txt')

# copy_object
response = s3Client.copy_object(
    Bucket = 'my-bucket',
    CopySource = '/my-bucket/my-file',
    Key = 'boto3copyobject.txt'
)

print(response)

# upload_file
boto3Upload = 'boto3upload.txt'

s3Resource.meta.client.upload_file(boto3Upload, 'my-bucket', boto3Upload)

# upload_fileobj
with open(boto3Upload, 'rb') as fileObj:
    response = s3Client.upload_fileobj(fileObj, 'my-bucket', 'boto3uploadobj.txt')
    print(response)

'''
response = s3Client.put_bucket_accelerate_configuration(
    Bucket='my-bucket',
    AccelerateConfiguration={
        'Status': 'Enabled'
    }
)
print(response)
'''
