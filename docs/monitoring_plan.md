# Monitoring Plan for AWS URL Shortener

## 1. Key Metrics to Monitor

### Application Metrics:
- **Request Rate**: Number of shorten/redirect requests per minute
- **Latency**: 
  - p95 latency for `/shorten` endpoint (< 500ms SLO)
  - p95 latency for redirects (< 200ms SLO)
- **Error Rate**: 
  - 4xx errors (client errors) 
  - 5xx errors (server errors) - Alert if > 2% over 5 minutes
- **Success Rate**: Percentage of successful requests

### AWS Service Metrics:
- **Lambda**:
  - Invocations per minute
  - Duration (average, p95, p99)
  - Error count and rate
  - Throttles
- **API Gateway**:
  - 4xxErrorRate, 5xxErrorRate
  - Latency, IntegrationLatency
  - Count (number of requests)
- **DynamoDB**:
  - Read/Write capacity utilization
  - Throttled requests
  - Success/error rates

## 2. CloudWatch Alarms

### Critical Alarms (P1 - Page Team):
1. **High Error Rate**:
   - Metric: 5xxErrorRate
   - Threshold: > 2% for 5 minutes
   - Action: SNS notification → Email/SMS

2. **Service Unavailable**:
   - Metric: Request count
   - Threshold: 0 requests for 5 minutes (if expecting traffic)
   - Action: Immediate notification

### Warning Alarms (P2 - Business Hours):
1. **High Latency**:
   - Metric: p95 latency
   - Threshold: > 500ms for 10 minutes
   - Action: SNS notification

2. **Capacity Warning**:
   - Metric: DynamoDB ReadCapacityUnits
   - Threshold: > 70% utilization for 15 minutes
   - Action: SNS notification

## 3. Dashboards

### Operations Dashboard:
1. **High-Level Overview**:
   - Total requests (24h)
   - Error rate gauge
   - Average latency
   - Current active users

2. **Service-Specific Panels**:
   - Lambda function performance
   - API Gateway metrics
   - DynamoDB performance
   - S3 request rates (for frontend)

## 4. SLO Definitions

### Service Level Indicators (SLIs):
1. **Availability**:
   - SLI: Successful requests / Total requests
   - Target: 99.5% over 28-day rolling window

2. **Latency**:
   - SLI: p95 request latency
   - Target: < 500ms for shorten, < 200ms for redirect

3. **Freshness**:
   - SLI: Time from URL creation to availability
   - Target: < 100ms

### Error Budget: 0.5% (14.4 hours/month downtime allowed)

## 5. Incident Response

### Alert Routing:
- P1 (Critical): SMS + Email + PagerDuty
- P2 (High): Email within 15 minutes
- P3 (Medium): Daily digest
- P4 (Low): Weekly review

### Runbooks:
1. **High Error Rate**:
   - Check Lambda function logs
   - Verify DynamoDB connectivity
   - Review recent deployments

2. **High Latency**:
   - Check DynamoDB capacity
   - Review Lambda memory allocation
   - Check network connectivity

## 6. Cost Monitoring
- Daily cost alerts if > $10/day
- Monthly budget: $50/month
- Cost allocation tags by service