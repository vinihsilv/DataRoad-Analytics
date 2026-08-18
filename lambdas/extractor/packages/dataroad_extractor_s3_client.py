import boto3


class DataroadExtractorS3Client:
    def __init__(self, s3_client: boto3.client("s3")):
        self.s3_client = s3_client

    def get_object(self, bucket_name, object_key):
        response = self.s3_client.get_object(Bucket=bucket_name, Key=object_key)
        return response["Body"].read()

    def put_object(self, bucket_name, object_key, data):
        self.s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=data)

    def list_objects(self, bucket_name, prefix=""):
        response = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        return [obj["Key"] for obj in response.get("Contents", [])]
