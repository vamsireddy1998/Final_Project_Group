import os
import json
import boto3

# Get table name from environment variable (NO HARDCODED SECRETS)
TABLE_NAME = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    """AWS Lambda handler for redirecting short URLs"""
    
    try:
        # Get short code from path parameter
        short_code = event.get('pathParameters', {}).get('code', '')
        
        if not short_code:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing short code'})
            }
        
        # Look up in DynamoDB
        response = table.get_item(Key={'short_code': short_code})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Short URL not found'})
            }
        
        item = response['Item']
        original_url = item['original_url']
        
        # Increment click count (optimistic update)
        table.update_item(
            Key={'short_code': short_code},
            UpdateExpression='ADD click_count :inc',
            ExpressionAttributeValues={':inc': 1}
        )
        
        # Return 302 redirect
        return {
            'statusCode': 302,
            'headers': {
                'Location': original_url,
                'Cache-Control': 'no-cache'
            },
            'body': ''
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Internal server error: {str(e)}'})
        }