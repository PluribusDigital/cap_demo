# AWS Connect Python Script to Get Current On-Call list
# CClayton - 06282020
# For Pluribus Digital
#
# Lambda Function is invoked by AWS Connect incoming call
# Program gets a file from S3
# Parses File for Phone Number
# Passes Phone Number to AWS Connect
# This code needs to execute in under 8 seconds, size of DynamoDB Table and Lambda Warm Up time impact this
# Colocate the AWS region where your Connect and Lambda will exist.
import os
import json
import boto3

def lambda_handler(event, context):
    try:
        role = event['Parameters']['Parameters']['role']
        requestedRole = json.loads(role)
    except:
       requestedRole = 'VariableCaptureFailed'

## DynamoDB Code
## DynamoDB table has 3 'columns', Role, PhoneNumber and Name,
## Role holds a value that is passed as a Parameter from the Contact Flow
    client = boto3.client('dynamodb')

    agent_scan = client.scan(
        TableName="cap-agents",
        FilterExpression='IsOnCall = :S',
        ExpressionAttributeValues={
            'S' :{
                'S' : requestedRole
            }
        },
        ProjectionExpression="'PhoneNumber','Name'"
    )

    agent_call = []
    ## This ennumerates the scan from a json object into an accessible list
    ## This current version can only handle one assigned role ex: Primary   
    for agent_entry in agent_scan['Items']:
        agent_call.append(agent_entry['Name']['PhoneNumber'])
    
    if len(agent_entry) == 1:
        print("Debug: agent was successfully retrieved")
        print("Debug: " + agent_entry)
        agentName = agent_entry[0]
        agentPhoneNum = agent_entry[1]
    elif len(agent_entry) > 1:
        print("Debug: more than 1 agent was successfully retrieved")
        print("Debug: Calling only the first agent found")
        print("Debug: " + agent_entry)
        agentName = agent_entry[0]
        agentPhoneNum = agent_entry[1]
    else:
        print("Debug: No agent found")
        ## You can either set a default here for calling a contact or update testReturn as an error value
        ## agentName = "DefaultAgent"
        ## agentPhoneNum = "+1-555-555-5555"
        ## Phone Number return format requires dashes, when using the GUI it requires no dashes, bug as of 06/20/2020

    ## This can be used as a piece of helper code, add a debug var in the testReturn, and its output will be encoded into the CloudWatch logs.
    #try:
    #    debug = type(event)
    #except:
    #    debug = 'IssueWithTypeToString'
    
    #testReturn = {'Name': agentName, 'Address': agentPhoneNum,'Role': requestedRole, 'Debug': debug}
    testReturn = {'Name': agentName, 'Address': agentPhoneNum,'Role': requestedRole}
    return testReturn
