# Simple Multi-Agent Chat System
Knowledge Representation and Reasoning – Group Assignment 03

## Overview
This project implements a minimal multi-agent chat system designed to demonstrate
core concepts of Knowledge Representation and Reasoning (KR&R). The system consists
of a Coordinator (Manager) agent that orchestrates multiple specialized agents to
answer user queries intelligently.

The system supports task decomposition, agent collaboration, structured memory,
context-aware retrieval, and adaptive decision-making.
## System Architecture

The system follows a Manager–Worker multi-agent architecture.

### Coordinator (Manager)
The Coordinator acts as the central controller of the system. It:
- Receives user queries
- Determines query complexity (simple vs complex)
- Plans and sequences agent execution
- Coordinates dependencies between agents
- Synthesizes final responses
- Avoids redundant computation by querying memory first

### ResearchAgent
The ResearchAgent simulates information retrieval using a pre-loaded mock
knowledge base. It returns structured facts with metadata such as topic,
source, timestamp, and confidence score.

### AnalysisAgent
The AnalysisAgent performs reasoning and analysis on retrieved data. It
summarizes information, compares concepts, identifies trade-offs, and
produces structured analytical outputs with confidence scores.

### MemoryAgent
The MemoryAgent manages long-term structured memory. It:
- Stores knowledge with metadata (topic, agent, timestamp, confidence)
- Supports keyword-based retrieval
- Supports vector similarity–based retrieval to avoid redundant work
- Influences future decision-making by reusing past knowledge
## Memory Design and Retrieval

The system implements an enhanced memory layer to support context-aware
knowledge storage and retrieval.

### Memory Types
1. **Conversation Memory**
   - Maintains a history of user queries handled by the Coordinator.
   - Enables context tracking across interactions.

2. **Knowledge Base Memory**
   - Stores structured knowledge records produced by Research and Analysis agents.
   - Each record includes:
     - Topic
     - Content
     - Source agent
     - Timestamp
     - Confidence score

3. **Agent State Memory**
   - Tracks what information each agent has contributed during task execution.
   - Helps the Coordinator decide whether to reuse previous results.

### Vector-Based Retrieval
To avoid redundant computation, the MemoryAgent supports vector similarity search.
A lightweight in-memory vector store is implemented using cosine similarity.

- Text is converted into deterministic numeric embeddings.
- Queries are embedded using the same method.
- Memory records are retrieved based on semantic similarity and keyword matching.

This approach provides functionality equivalent to FAISS or Chroma while ensuring
platform compatibility and minimal dependencies.
## How to Run the System

### Prerequisites
- Python 3.10+
- Git
- VS Code or any Python-supported IDE

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/noorali104/krr-multiagent.git
   cd krr-multiagent
Install dependencies (if required):

pip install -r requirements.txt


(Note: The system primarily uses standard Python libraries.)

Run the system:

python src/main.py
Test Scenarios

The following sample scenarios are implemented and demonstrated in the
outputs/ directory:

Simple Query — simple_query.txt

Complex Query — complex_query.txt

Memory Recall — memory_test.txt

Multi-step Reasoning — multi_step.txt

Collaborative Comparison — collaborative.txt

Each output file shows agent collaboration, coordinator decisions, and
memory usage.

Containerization (Docker)

Docker support can be added using a simple Dockerfile and docker-compose
configuration. This enables consistent execution across environments.
The system is designed to be container-ready with minimal changes.

Notes

LLMs are optional and not required for system functionality.

Rule-based planning and reasoning are used as a fallback strategy.

The architecture is modular and easily extensible.
