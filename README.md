# AI-Powered Dynamic Task Scheduling System

This project implements a dynamic task scheduling system that leverages AI to recommend the optimal scheduling algorithm (FCFS, SJF, or Round Robin) for a set of tasks in real time. The system supports interactive task addition, automatic scheduling refresh, and custom stop conditions.

## Features
- **AI-Based Algorithm Recommendation:** Uses a trained Random Forest model to select the best scheduling algorithm based on task features.
- **Dynamic Scheduling:** Scheduler refreshes every 5 seconds and adapts to new tasks as they arrive.
- **Multiple Algorithms:** Supports First-Come-First-Serve (FCFS), Shortest Job First (SJF), and Round Robin (RR).
- **Interactive Task Addition:** Add tasks manually or configure for automatic addition.
- **Custom Stop Condition:** Type `stop` at the prompt to exit the scheduler gracefully.

## Files
- `dynamic_scheduler.py`: Main script for dynamic scheduling with AI recommendations.
- `ai_scheduling.py`: Contains traditional scheduling algorithms and AI model training logic.
- `generate_dataset.py`: Script to generate synthetic datasets for model retraining.
- `scheduling_dataset.csv`: Dataset used to train the AI model.
- `traditional_scheduling.py`: Additional scheduling algorithm implementations.

## Getting Started
1. **Install dependencies:**
   ```bash
   pip install numpy pandas scikit-learn
