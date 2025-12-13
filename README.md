# Log Intelligence & Anomaly Detection System

## Problem Statement
Modern distributed systems generate millions of logs every day. Manually analyzing these logs to detect errors, failures, or abnormal patterns is inefficient and error-prone. This project aims to build a centralized log ingestion and analysis system with machine learning-based anomaly detection.

## Objective
- Centralize logs from multiple services
- Enable efficient querying and filtering of logs
- Detect anomalous log patterns using machine learning
- Help engineers identify system issues early

## Tech Stack
- Backend: FastAPI (Python)
- Database: PostgreSQL
- Machine Learning: scikit-learn
- Deployment: Docker, Render/AWS (later)

## High-Level Architecture
1. Services send logs to a centralized backend via REST APIs
2. Logs are stored in a structured database
3. Engineers query logs through APIs
4. ML models analyze log patterns and flag anomalies
