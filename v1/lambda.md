# CAP Connect Setup  <a href="https://pluribusdigital.com" target="_blank"><img align="right" src="pb-logo-maintransparent.svg" width="120" alt="Pluribus Digital Logo" ></a>
### Call Alert at Pluribus
____
### Lambda Setup
1. Download the [Get Current Agent script](CAP-GetCurrentAgent.py)
    - Right click the above link and save as
2. Navigate to [AWS Console and choose the Lambda service page](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions)
3. Choose Create Function
    1. Author from scratch
    2. Provide a Function Name (ex CAP-GetCurrentAgent)
    3. Runtime should be set to Python 3.x
    4. Architecture is x86_64 (this has not been tested, but should work on arm64)
4. Open the script in your preferred text editor
5. Copy the script into your clipboard
6. Paste the script into the lambda_function.py in the Lambda Code Editor
7. From the actions drop down choose Publish New Version
8. After publishing the Lambda function is ready to be integrated, we now need to [setup DynamoDB which can be found here.](dynamodb.md)