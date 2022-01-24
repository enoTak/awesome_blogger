# Setting of sertverless-gas-client-secret.json
* generate secret key on GCP and copy to this directory as tha file name = ```serverless-gas-client-secret.json```

# Setting of zappa_settings.json
* the setting is as follows. ```SERVERLESS_AWS_ACCESS_KEY_ID``` and ```SERVERLESS_AWS_SECRET_KEY``` are same as ```application```
```
{
    "dev": {
        "apigateway_enabled": false,
        "app_function": "bot.app",
        "aws_region": "ap-northeast-1",
        "profile_name": "serverless-blog",
        "project_name": "serverless-bot",
        "runtime": "python3.8",
        "s3_bucket": "zappa-xxxxxxx",
        "environment_variables": {
            "SERVERLESS_AWS_ACCESS_KEY_ID": "xxxxxxxx",
            "SERVERLESS_AWS_SECRET_KEY": "xxxxxxxx",
            "GSPREAD_DOC_ID": "xxxxxxxx"
        },
        "events": [
            {
                "function": "bot.run_bot",
                "expression": "cron(59 14 * * ? *)"
            }
        ]
    }
}
```