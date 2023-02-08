import boto3

# Create an S3 access object
s3 = boto3.client("s3")

s3.upload_file(
    Filename="/Users/bhanuprakash/projects/hello_flask/test.txt",
    Bucket="test1234567891234567",
    Key="uploaded by bhanu",
)

    