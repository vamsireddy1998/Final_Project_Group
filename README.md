AWS Serverless URL Shortener
1) What It Does (User Flow)

This project implements a URL shortener on AWS. Users can shorten long URLs and use the generated short links to redirect to the original URLs.

Write Path (Create Short URL):

User submits a URL → API Gateway → Lambda → DynamoDB → Returns short code

Read Path (Redirect):

User clicks a short link → API Gateway → Lambda → Looks up URL in DynamoDB → 302 Redirect

2) Architecture

Components:

Frontend: S3 static website

API: API Gateway

Compute: AWS Lambda (Python)

Database: DynamoDB

IaC: AWS SAM template

Security:

Least-privilege IAM roles

No hardcoded secrets; all configuration via environment variables

3) API Endpoints

Shorten URL (POST):

curl -X POST https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'


Response:

{
  "short_code": "abc123",
  "short_url": "https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/abc123",
  "original_url": "https://example.com"
}


Redirect (GET):

curl -I https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/abc123

4) SLO & Monitoring Plan

Latency: p95 < 300ms

Error Rate: < 1%

Availability: > 99%

Monitored Metrics:

Lambda errors

API Gateway 4xx/5xx errors

DynamoDB read/write latency

Request rates

Refer to the detailed monitoring plan in monitoring_plan.md.

5) How to Deploy
git clone https://github.com/vamsireddy1998/Final_Project_Group
cd Final_Project_Group
sam build
sam deploy --guided


Access URLs:

Web Frontend: http://final-project-vvs.s3-website-us-east-1.amazonaws.com

API: https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod

6) Team & Roles
Team Member	Role
Name1	AWS Infrastructure
Name2	Lambda & Database
Name3	Frontend & Documentation
7) AI Usage

Tools Used: ChatGPT-4, GitHub Copilot

Prompt Example: "Generate Python Lambda for URL shortener with DynamoDB"

Human Modifications:

Added security measures

Implemented input validation

Set up monitoring & alerting

Ensured production readiness

Features Implemented:

Serverless Infrastructure as Code (AWS SAM)

Lambda functions for URL creation and redirection

Static frontend hosted on S3

CloudWatch monitoring and alarms

IAM roles with least privilege
