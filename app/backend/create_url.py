import json 
import boto3 
import string 
import random 
import time 
 
dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('final-project-user-urls') 
 
def generate_short_code(): 
    chars = string.ascii_letters + string.digits 
    return ''.join(random.choice(chars) for _ in range(6)) 
 
def lambda_handler(event, context): 
    try: 
        body = json.loads(event['body']) 
        original_url = body['url'] 
        short_code = generate_short_code() 
        table.put_item(Item={'short_code': short_code, 'original_url': original_url, 'created_at': int(time.time()), 'click_count': 0}) 
        return {'statusCode': 200, 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}, 'body': json.dumps({'short_code': short_code, 'short_url': 'https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/' + short_code, 'original_url': original_url})} 
    except Exception as e: 
        return {'statusCode': 500, 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}, 'body': json.dumps({'error': str(e)})} 
