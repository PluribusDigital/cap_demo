# AWS Connect Python Script to Get Current On-Call list
# CClayton - 06282020
# For Pluribus Digital
#
# Lambda Function is invoked by AWS Connect incoming call
# Program gets a file from S3
# Parses File for Phone Number
# Passes Phone Number to AWS Connect

import boto3
import json
import os

def lambda_handler(event, context):
    try:
        role = event['Parameters']['Parameters']['role']
        requestedRole = json.loads(role)
    except:
       requestedRole = 'VariableCaptureFailed'


    try:
        debug = type(event)
    except:
        debug = 'IssueWithTypeToString'
    
    ## dashes are needed in the below phone number but not in the 
    testReturn = {'Name':'Agent On Call','Address':'+1555-555-5555','Role': requestedRole, 'Debug': debug}
    return testReturn
