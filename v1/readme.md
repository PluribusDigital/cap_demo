# CAP   <a href="https://pluribusdigital.com" target="_blank"><img align="right" src="pb-logo-maintransparent.svg" width="120" alt="Pluribus Digital Logo" ></a>
### Call Alert at Pluribus
____
#### Key Files
* Amazon Connect Key Docs and Files
    * [Connect Setup](connect_setup.md)
    * [After Hours Call Escalation Flow JSON](AfterHours_IncomingWEscalation.json) (importable into a Connect instance)
* [Lambda Configuration](lambda.md)
    * [CAP Get Current Agent Function](CAP-GetCurrentAgent.py)
* DynamoDB Configuration
___
#### Design Goal: 
* This system is designed as a lightweight, and modular tool for connecting agnostic monitoring, alerting, and future frameworks to be able to contact engineers and reporting chains via SMS and Phone Call.

* **V1**: This version provided a generic phone number that connects requestor to primary and secondary on-call contacts if there is an emergency.
![CAP V1 System Design Diagram](/CAP-SysV1.png)

    * [Amazon Connect](https://aws.amazon.com/connect/)
        * This is AWS' Call Center in a box which allows for visual workflows using an IVR
    * [AWS Lambda (Python)](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
        * Triggered by API Gateway or Pinpoint to pull contact info, and initiate response logic.
    * [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
        * Provides lightweight holding and access of engineer information, and on-call state (primary, escalation, off).

