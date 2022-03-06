import json
import boto3
import base64

def lambda_handler(event, context):
    # TODO implement

    print("This lambda function is called -- lbs-app-rkp-test")
    print("Received event: " , event)
    runtime_client = boto3.client('sagemaker-runtime')
    content_type = "application/json"
    input = event
    request_body = input
    print("Request Body: " ,  request_body)
    data = json.loads(json.dumps(request_body))
    print("Data: ", data)
    payload = data['body']
    print("Payload: " , payload)
    payload = {"Input": payload}
    payload = json.dumps(payload)
    print("updated_payload: ", payload)
    
    endpoint_name = "sklearn-local-ep2022-03-06-17-57-22"
    
    response = runtime_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType=content_type,
        Body=payload)
    print("Response: ", response)
    response_body = json.loads(response['Body'].read().decode())['Output']
    print("Response Body: ", response_body)
    body_final = 'unkown'
    if(response_body == 1):
            body_final =  'lay'
    if(response_body == 2):
            body_final =  'flay'
    if(response_body == 2):
            body_final =  'tech'

    return {
        'statusCode': 200,
        'body': body_final
        
    }
