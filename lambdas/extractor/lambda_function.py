

def lambda_handler(event=None, context=None):
    print("Lambda invoked")
    return {
        "statusCode": 200,
        "body": "Hello from local lambda"
    }


if __name__ == "__main__":
    print(lambda_handler({"source": "local"}, None))