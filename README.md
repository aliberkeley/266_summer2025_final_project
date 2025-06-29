# 266_summer2025_final_project
Cutting Through the Noise: Detecting Fallacies in Online Discourse with NLP
Allen Li, Arthur Kang, Skylar Wang

## Milestone (try to submit by July 20th)

__If you want more formal feedback on an intermediate stage of your project, feel free to send us an milestone/interim copy of your report a week ahead of our office hour.  We are happy to take a look and prepare some feedback for you either over email or in the office hour.__

You’ll submit a partial report (3-5 pages) and implementation of your project. This should include:
- Evidence that you’ve been able to obtain, load, and play around a bit with your data.  (For example,  some simple exploratory data analysis.)
- Results from a baseline model. This can be very simple, such as random predictor, most-common-class, or a bag-of-words model.

Your report should be the working/rough draft of your final project report (see below), although it’s expected that you won’t have fleshed-out results or conclusion sections. It’s also okay if your report changes substantially between here and the final, especially if you have exciting results in the interim!

For the milestone, your writeup should have sections similar to the following, in the vein of a proper research paper:
- **Abstract**
- **Introduction** (motivation for your work)
- **Background** (literature review, or related work)
- **Methods** (include a description of any proposed work here, even if you haven’t done it yet)
- **Results and discussion** (for your baseline model, though feel free to include material for anything else you’ve done)
- **Next Steps** section for work you plan to do before submitting the final version (you’ll remove this section and replace it with your conclusions, final results and analysis in your final report)

The easiest way to write your report is LaTeX; the standard ACL template is available [here](http://2023.aclweb.org/downloads/acl2023.zip) (or, on Overleaf [here](https://www.overleaf.com/latex/templates/acl-2023-proceedings-template/qjdgcrdwcnwp) or in Word [here](http://2023.aclweb.org/downloads/acl2023.docx)). However, you’re welcome to typeset in Microsoft Word, Google Docs, or the editor of your choice as long as you can export to PDF.

You should also share your code with us via GitHub.  Just include a link to your GitHub repository.

Please send your write-up in PDF format to mids-nlp-instructors@googlegroups.com or follow the specific instructions from your section instructor.

## Proposal:
https://docs.google.com/document/d/18rKL6RrghY9bW_u3ZXbtcEFmwcZmKiWhLEFo3oWfLyI

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
