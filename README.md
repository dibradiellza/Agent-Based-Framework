# Agent-Based-Framework

This repository contains the implementation of an autonomous agent-based framework for cryptocurrency trading strategy development using Large Language Models (LLMs). The project was developed as part of my Master's thesis at the University of Basel.

Inspired by Karpathy's AutoResearch paradigm, the framework enables LLM agents to iteratively generate, evaluate, and refine Python-based trading strategies through interaction with a fixed backtesting environment. Candidate strategies are assessed using predefined performance metrics, and only modifications that improve performance are retained, creating an autonomous optimization loop without human intervention.

## Framework Architectures

Two optimization frameworks were implemented and evaluated:

### Single-Agent Framework
A single LLM agent is responsible for the complete optimization process, including strategy generation, evaluation, and refinement.

### Dual-Agent Framework
The optimization process is divided between two specialized agents:

- **Explorer Agent** – proposes and implements modifications to improve trading strategy performance.
- **Risk Manager Agent** – evaluates proposed strategies and introduces risk management mechanisms to improve robustness and generalization.

Both frameworks start from the same baseline trading strategy and operate under identical evaluation conditions, enabling a controlled comparison of their optimization behavior and out-of-sample performance.

## Project Objective

The objective of this project is **not** to develop a production-ready trading system, but to demonstrate how Large Language Models can operate as autonomous agents within an iterative optimization framework for quantitative finance. The repository serves as a proof of concept and provides a foundation for future research on autonomous financial agents.

