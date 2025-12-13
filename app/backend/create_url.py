 Directory of C:\Users\Admin\final-project-submission\app\backend

07-12-2025  20:48    <DIR>          .
06-12-2025  23:01    <DIR>          ..
12-12-2025  23:25             1,637 create_url.py
07-12-2025  20:48               742 create_url_cors.zip
06-12-2025  22:41             1,069 redirect_url.py
               3 File(s)          3,448 bytes
               2 Dir(s)  48,315,027,456 bytes free

C:\Users\Admin\final-project-submission\app\backend>cat create_url.py
'cat' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Admin\final-project-submission\app\backend>show create_url.py
'show' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Admin\final-project-submission\app\backend>type create_url.py
import os
TABLE_NAME = os.environ['TABLE_NAME']
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
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}

    try:
        body = json.loads(event['body'])
        original_url = body['url']
        short_code = generate_short_code()

        table.put_item(Item={
            'short_code': short_code,
            'original_url': original_url,
            'created_at': int(time.time()),
            'click_count': 0
        })

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'short_code': short_code,
                'short_url': 'https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/' + short_code,
                'original_url': original_url
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }

C:\Users\Admin\final-project-submission\app\backend>