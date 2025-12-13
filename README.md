# AWS Serverless URL Shortener

## 1) What It Does (User Flow)
This is a URL shortener built on AWS. Users can shorten long URLs and use short links to redirect to originals.

**Write Path (Create Short URL):**
1. User submits URL → API Gateway → Lambda → DynamoDB → Returns short code

**Read Path (Redirect):**
1. User clicks short link → API Gateway → Lambda → Looks up in DynamoDB → 302 redirect

## 2) Architecture
![Architecture Diagram](architecture-diagram.png)

**Components:**
- Frontend: S3 static website
- API: API Gateway
- Compute: AWS Lambda (Python)
- Database: DynamoDB
- IaC: AWS SAM template

**Security:**
- Least-privilege IAM roles
- No hardcoded secrets (env variables only)

## 3) API Endpoints

**Shorten URL:**
```bash
curl -X POST https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/shorten \
  -H "Content-Type: application/json" \
  -d '{"long_url":"https://example.com"}'
Response:

json
{"short_code":"abc123","short_url":"https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/abc123"}
Redirect:

bash
curl -I https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod/abc123
4) SLO & Monitoring Plan
p95 latency < 300ms

Error rate < 1%

Availability > 99%

Monitor: Lambda errors, API Gateway 4xx/5xx, DynamoDB latency

5) How to Deploy
bash
git clone https://github.com/vamsireddy1998/Final_Project_Group
cd Final_Project_Group
sam build
sam deploy --guided
Access:

Web: http://final-project-vvs.s3-website-us-east-1.amazonaws.com

API: https://th1omwipo7.execute-api.us-east-1.amazonaws.com/prod

6) Team & Roles
3 Members:

Name1: AWS Infrastructure

Name2: Lambda & Database

Name3: Frontend & Docs

7) AI Usage
Tools: ChatGPT-4, GitHub Copilot

Prompt: "Generate Python Lambda for URL shortener with DynamoDB"

Human Changes: Added security, validation, monitoring, and error handling.

Features Implemented:

Infrastructure as Code (AWS SAM)

Monitoring plan

Security best practices
