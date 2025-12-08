# AWS Serverless URL Shortener

## Team
- Final_project_User

## What It Does
- Shortens URLs via web interface or API
- Stores URL mappings in DynamoDB with click tracking
- Redirects short URLs to original destinations

## Architecture
- Frontend: S3 static website hosting
- API: API Gateway REST endpoints
- Compute: AWS Lambda functions (Python)
- Database: DynamoDB NoSQL table
- Security: IAM roles with least privilege access

## API Endpoints
- POST /shorten - Create short URL
- GET /{short_code} - Redirect to original URL

## How to Access
- Web Interface: http://final-project-vvs.s3-website-us-east-1.amazonaws.com
- API Base URL: https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod

## SLO & Monitoring Plan
- Latency: p95 API response time < 500ms
- Availability: 99.5% uptime for redirect functionality
- Error Rate: Alert if error rate > 2% over 5-minute window
- Monitoring: CloudWatch metrics for Lambda invocations, duration, errors

## AI Usage
- Lambda function code templates generated with AI assistance
- API Gateway setup commands provided by AI
- All code reviewed for security and AWS best practices