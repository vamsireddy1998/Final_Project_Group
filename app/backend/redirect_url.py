import json
import boto3
import os

TABLE_NAME = os.environ.get('TABLE_NAME', 'final-project-user-urls')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type'
}

def lambda_handler(event, context):

    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': HEADERS, 'body': ''}

    short_code = event.get('pathParameters', {}).get('code', '')

    if not short_code:
        return {
            'statusCode': 400,
            'headers': HEADERS,
            'body': json.dumps({'error': 'Missing short code'})
        }

    try:
        response = table.get_item(Key={'short_code': short_code})

        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': HEADERS,
                'body': json.dumps({'error': 'Not found'})
            }

        original_url = response['Item']['original_url']

        return {
            'statusCode': 302,
            'headers': {
                **HEADERS,
                'Location': original_url
            },
            'body': ''
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': HEADERS,
            'body': json.dumps({'error': str(e)})
        }
