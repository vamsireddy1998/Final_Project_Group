import json 
import boto3 
 
dynamodb = boto3.resource('dynamodb') 
table = dynamodb.Table('final-project-user-urls') 
 
def lambda_handler(event, context): 
    print('Event:', event) 
    try: 
        short_code = event['pathParameters']['short_code'] 
        print('Looking for:', short_code) 
        response = table.get_item(Key={'short_code': short_code}) 
        print('DynamoDB response:', response) 
 
        if 'Item' not in response: 
            return {'statusCode': 404, 'body': 'Not found'} 
 
        item = response['Item'] 
        print('Found item:', item) 
 
        # Update click count 
        table.update_item( 
            Key={'short_code': short_code}, 
            UpdateExpression='SET click_count = click_count + :val', 
            ExpressionAttributeValues={':val': 1} 
        ) 
 
        return {'statusCode': 302, 'headers': {'Location': item['original_url']}} 
 
    except Exception as e: 
        print('Error:', str(e)) 
        return {'statusCode': 500, 'body': 'Internal server error'} 
