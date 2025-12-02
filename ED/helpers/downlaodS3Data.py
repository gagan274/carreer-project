import boto3
import re
def GetDataFromS3(deviceId, from_epoch, to_epoch):


    # Initialize a session using Amazon S3
    s3 = boto3.client(
    's3',
    aws_access_key_id='AKIASG73VL5RGT7QI7OC',
    aws_secret_access_key='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',
    region_name='ap-south-1'
)

    # Define the bucket name and the prefix for the files
    bucket_name = 'dbchangetesting'
    prefix = "HBL_RAWDATA/"+deviceId+"/"


    # List all objects in the specified bucket and prefix
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    # Filter objects based on the epoch time range
    filtered_files = []
    for obj in response.get('Contents', []):
        match = re.search(r'(\d+)\.json$', obj['Key'])
        if match:
            epoch_time = int(match.group(1))
            if from_epoch <= epoch_time <= to_epoch:
                filtered_files.append(obj['Key'])
    requiredData = []
    # Print the data of the filtered files
    for file_key in filtered_files:
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        data = obj['Body'].read().decode('utf-8')
        requiredData.append(data)

    responceData = {"data":requiredData}
    print(responceData)
    return responceData
GetDataFromS3("GHWC000001",1722408890,1722409016)