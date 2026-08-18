import os


class DataroadExtractorS3Environment:
    bucket_name = os.environ.get("DATRAROAD_EXTRACTOR_S3_BUCKET_NAME")
    bucket_prefix = os.environ.get("DATRAROAD_EXTRACTOR_S3_BUCKET_PREFIX")
