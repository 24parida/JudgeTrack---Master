# judgeTrack-AWS
Runs on sagemaker notebook instance of type ml.t5.xlarge
final_model, and inference_py are uploaded into the notebook instance
endpoint code in a notebook instance is created with s3 bucket, that includes model.tar.gz and sagemaker endpoint

lambda function connects the API-Gateway to the sagemaker endpoint
