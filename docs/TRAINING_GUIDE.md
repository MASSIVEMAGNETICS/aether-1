# Training Suite Guide

## One-Click Frontier Model Training

On first launch, AETHER-1 automatically:
1. Initializes neuromorphic + active inference core
2. Trains on synthetic frontier-scale data (active inference + world model objectives)
3. Exports production-ready model (ONNX + GGUF)
4. Creates desktop shortcut

## Advanced Training
```bash
aether train --frontier --export
```

Supports:
- Active Inference fine-tuning
- Neuromorphic weight adaptation
- Neuro-symbolic alignment training
- Self-evolution of architecture

All training is logged in `training_logs/` with full reproducibility.