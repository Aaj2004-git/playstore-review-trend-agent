# Google Play Review Trend Analysis using Agentic AI

## Overview
This project builds an Agentic AI system that consumes daily Google Play Store reviews
for Swiggy and generates a rolling 30-day trend analysis of user issues, requests, and feedback.

## Architecture
- Ingestion Agent: Fetches daily reviews
- Preprocessing Agent: Cleans text
- Topic Extraction Agent: Uses LLM to extract issues
- Canonicalization Agent: Deduplicates similar topics using embeddings
- Trend Agent: Aggregates daily frequencies
- Report Agent: Generates trend table

## Why Agentic AI?
Each agent has a focused responsibility and collaborates to ensure:
- High recall topic detection
- Accurate deduplication
- Clean trend evolution

## Output
A CSV report where:
- Rows = Topics
- Columns = Dates (T-30 → T)
- Values = Frequency of topic occurrence

## How to Run
```bash
pip install -r requirements.txt
python main.py
