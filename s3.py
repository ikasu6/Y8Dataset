from PIL import Image  
from io import BytesIO,StringIO
from tqdm import tqdm  
from datetime import datetime 
from requests.exceptions import RequestException 
import boto3


def get_image_dimensions_from_s3_bucket(s3_bucket_name, image_key):  
    
    ''' 
    The function retrieves the dimensions (width and height)
    of an image stored in an Amazon S3 bucket.
    '''
    # Create an S3 client  
    s3_client = boto3.client('s3')  
  
    # Get the image object from S3  
    image_obj = s3_client.get_object(Bucket=s3_bucket_name, Key=image_key)  
  
    # Read the image into memory  
    image_data = BytesIO(image_obj['Body'].read())  
  
    # Open the image using PIL  
    with Image.open(image_data) as img:  
        # Get the image dimensions  
        width, height = img.size  
  
    return width, height 

