# Clothing Order Service

Order management microservice for the online clothing platform.

## Responsibilities
- Cart management
- Order creation
- Order lifecycle tracking
- Coordination with inventory and payment services

## Tech Stack
- Node.js / Java (TBD)
- Docker
- Kubernetes (EKS)
- AWS

## Branching Strategy
GitFlow with protected main and develop branches.

## CI/CD
CI via GitHub Actions. Images pushed to Amazon ECR.


## Platform completion notes

This service is part of the AWS clothing-platform starter. Keep order creation idempotent, validate inventory before confirming orders, and use an outbox/saga pattern for payment and shipping integration. The current starter persistence is not production durable; configure a managed database and migrations before deployment.
