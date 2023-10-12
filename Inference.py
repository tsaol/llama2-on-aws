#You need to install boto3.
#pip install boto3

import io
import boto3
import json

# endpoint_name your endpoint name
endpoint_name ='ENDPOINT_NAME'
ACCESSKEY = 'YOUR_ACCESS_KEY'
SECRETKEY = 'YOUR_SECRET_KEY'
REGIONNAME = 'YOUR_ENDPOINT_REGION'



#Create SageMaker runtime client
sagemaker_runtime_client = boto3.client('sagemaker-runtime',
                        region_name=REGIONNAME,
                        aws_access_key_id=ACCESSKEY,
                        aws_secret_access_key=SECRETKEY)

#prepar data
prompt='hello who are you'
body = json.dumps({"inputs": prompt})

#invoke inference endpoint
response = sagemaker_runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    Body=body,
    ContentType='application/json' 
)

#response
result = response['Body'].read()
print(result)
