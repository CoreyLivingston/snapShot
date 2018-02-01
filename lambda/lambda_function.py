import greengrasssdk
import time
import boto3
import cv2

s3 = boto3.client('s3')

client = greengrasssdk.client('iot-data')

def lambda_handler(event, context):
    ret, img = awscam.getLastFrame()
    #file_name = 'DeepLens/image-'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    #encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    #jpg_data = cv2.imencode('.jpg', img, encode_param)
    #response = s3.put_object(ACL='public-read', Body=jpg_data.tostring(),Bucket='shapshot1',Key=file_name)
    #image_url = 'https://s3.amazonaws.com/shapshot1/deep/'+file_name
    client.publish(topic='hello/world', payload='hey')
    time.sleep(2)
    return
