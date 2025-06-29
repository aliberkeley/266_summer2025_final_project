# 266_summer2025_final_project
Cutting Through the Noise: Detecting Fallacies in Online Discourse with NLP
Allen Li, Arthur Kang, Skylar Wang

## Datasets:
[LFUD (for fine-tuning)](https://github.com/YandaGo/LFUD/blob/main/LFUD.csv)
[Logic](https://github.com/causalNLP/logical-fallacy/blob/main/data/edu_all.csv)
[LogicClimate](https://github.com/causalNLP/logical-fallacy/blob/main/data/climate_all.csv)


## Hypothesis
Prompt-based approaches (including Active Prompting and Logical Structure Trees) can match the performance of fine-tuned models like LLaMA 3.3 with LoRA in identifying the type of logical fallacy from a sentence—despite having no task-specific training.

## Tasks
__Allen__
- Test [pre-trained roberta model](https://huggingface.co/MidhunKanadan/roberta-large-fallacy-classification) on logic and logicClimate dataset (baseline model, higher priority)
  - Imbalanced class distribution in Logic and LogicClimate datasets and different classes. Drop minority classes or oversample?
- Fine-tune Llama-3.3 on LFUD, train on Logic and LogicClimate datasets
- Generating more Logical Fallacy data based on LFUD Paper. This will give us enough data to fine-tune the larger models like DeepSeek R1 and GPT

__Skylar__
- Active prompting with DeepSeek R1 and GPT
  - [Active Prompting Paper](https://aclanthology.org/2024.acl-long.73.pdf)
  
__Arthur__
- Logical Structure Tree prompt treatment on GPT and DeepSeek R1
  - [LST Paper](https://aclanthology.org/2024.emnlp-main.730.pdf)
