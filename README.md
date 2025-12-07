# AWS Serverless URL Shortener 
 
## Team: Final_project_User (Solo) 
 
## What It Does 
## What It Does 
- Stores in DynamoDB, tracks clicks 
- Redirects short URLs to originals 
 
## Architecture 
- Frontend: S3 static website 
- API: API Gateway 
- Compute: AWS Lambda 
- Database: DynamoDB 
- Security: IAM least privilege 
 
## API Endpoints 
- POST /shorten - Create short URL 
- GET /{code} - Redirect to original 
 
## How to Access 
- Web: http://final-project-vvs.s3-website-us-east-1.amazonaws.com 
- API: https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod 
 
## SLO Plan 
## SLO Plan 
- Availability: 99.5% uptime 
- Error rate: Alert if 
- Monitor: Lambda, API Gateway, DynamoDB metrics 
 
## AI Usage 
- Lambda code templates 
- API Gateway setup help 
- All code reviewed for security 
