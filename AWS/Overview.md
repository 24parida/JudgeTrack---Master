# judgeTrack-AWS
create sagemaker notebook instance of type ml.t5.xlarge ($0.42 per hour)
upload final_model, and inference_py into the notebook instance
run the endpoint code in a notebook instance to create s3 bucket with model.tar.gz and sagemaker endpoint

create lambda function with sagemaker permissions, and add lambda code
