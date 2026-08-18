import boto3


from packages.dataroad_extractor_s3_client import DataroadExtractorS3Client
from packages.dataroad_extractor_s3_enviroment import DataroadExtractorS3Environment
from packages.dataroad_extractor_s3_parser import DataroadExtractorS3Parser


def lambda_handler(event=None, context=None):
    print("Starting extractor lambda function...")
    client_s3 = DataroadExtractorS3Client(s3_client=boto3.client("s3"))

    print("Getting csv file from S3 bucket...")
    client_s3.get_object(bucket_name="my-bucket", object_key="data.csv")


if __name__ == "__main__":
    print(lambda_handler({"source": "local"}, None))
