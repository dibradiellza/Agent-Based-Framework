# Agent-Based-Framework

This repository contains the implementation of an autonomous agent-based framework for cryptocurrency trading strategy development using Large Language Models (LLMs). The project was developed as part of my Master's thesis at the University of Basel.

Inspired by Karpathy's AutoResearch paradigm, the framework enables LLM agents to iteratively generate, evaluate, and refine Python-based trading strategies through interaction with a fixed backtesting environment. Candidate strategies are assessed using predefined performance metrics, and only modifications that improve performance are retained, creating a fully autonomous optimization loop without human intervention.

To investigate the impact of agent architecture, two optimization frameworks were implemented:

Single-Agent Framework – one LLM agent is responsible for the complete optimization process, including strategy generation, evaluation, and refinement.
Dual-Agent Framework – responsibilities are divided between two specialized agents: an Explorer Agent, which proposes strategy improvements, and a Risk Manager Agent, which focuses on risk controls and robustness.

Both frameworks start from the same baseline trading strategy and operate under identical evaluation conditions, enabling a controlled comparison of their optimization behavior and out-of-sample performance.

The objective of this project is not to develop a production-ready trading system, but to demonstrate how Large Language Models can operate as autonomous agents within an iterative optimization framework for quantitative finance. The repository serves as a proof of concept and a foundation for future research on autonomous financial agents
