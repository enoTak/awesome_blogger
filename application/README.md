# For development with localdb
1. install DynamoDB local from https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html.
1. copy "dynamodb_local_latest" in "application" directory.
1. execute launch_dynamodblocal.sh. For test execution, we need to keep launching DynamoDb in local env.

# Setting for deployment to AWS to zappa
1. create "application/zappa_setting.json" file.
1. sample setting in this file is as follows:
```
{
    "dev": {
        "app_function": "server.app",
        "aws_region": "ap-northeast-1",
        "profile_name": "serverless-blog",
        "project_name": "application",
        "runtime": "python3.8",
        "s3_bucket": "zappa-xxxxxxxxx",
        "environment_variables": {
            "SERVERLESS_BLOG_CONFIG": "production",
            "SERVERLESS_USER_PW": "XXXXXX",
            "SERVERLESS_SECRET_KEY": "XXXXXXX",
            "SERVERLESS_AWS_ACCESS_KEY_ID": "XXXX",
            "SERVERLESS_AWS_SECRET_KEY": "XXXX"
        }
    }
}
```