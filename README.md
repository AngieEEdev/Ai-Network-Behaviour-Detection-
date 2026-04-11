# AI Network Behaviour Detection Dashboard

## Overview

This project presents a complete end-to-end machine learning pipeline for detecting anomalous network behaviour using structured traffic data. It integrates data preprocessing, feature engineering, model training, and a lightweight deployment interface to simulate real-time anomaly detection.

The system demonstrates how machine learning techniques can be applied to cybersecurity contexts, particularly in identifying irregular traffic patterns that may indicate malicious or abnormal activity.

## Key Features

- End-to-end ML pipeline: raw data → preprocessing → model → inference  
- Feature engineering tailored to network traffic characteristics  
- Interactive Streamlit dashboard for real-time analysis  
- Modular code structure supporting extensibility  
- Reproducible workflow for training and deployment  

## Methodology

### Data Processing
Raw CSV data is cleaned to ensure consistency. Missing values are removed and column names are standardised.

### Feature Engineering

Core features:
- `spkts` — number of packets  
- `dur` — duration of connection  
- `sbytes` — source bytes  

Derived feature:
- `bytes_per_packet = sbytes / (spkts + 1)`

This derived metric improves detection of disproportionate traffic behaviour.

### Model

A lightweight supervised learning model (e.g., Logistic Regression) is used as a baseline classifier.

The focus is on:
- pipeline correctness  
- feature consistency  
- deployable workflow  

### Deployment

A Streamlit interface enables:
- CSV upload  
- real-time predictions  
- anomaly classification  


## Usage

### 1. Train the Model

```bash
python src/train.py
