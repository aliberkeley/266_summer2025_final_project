import os
import json
import time
import pandas as pd
import openai

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= "API_KEY"
)

df = pd.read_csv("climate_test_with_lst.csv")

def assess_fallacy(text: str, lst: str) -> dict:
    prompt = (
        "You are an expert in argumentation and logic. "
        "Identify which logical fallacy is present in the following sentence, "
        "using also the provided Logical Structure Tree (LST) to inform your reasoning.  "
        "Choose from: ad hominem, ad populum, appeal to emotion, circular reasoning, "
        "deductive fallacy, fallacy of credibility, fallacy of extension, fallacy of relevance, "
        "false causality, false dilemma, faulty generalization, intentional fallacy.\n\n"
        "Think step by step, then respond *only* in JSON with this format:\n\n"
        "{\n"
        '  "Reasoning": "Brief chain‑of‑thought explaining your decision.",\n'
        '  "Predicted Fallacy": "One of the listed labels"\n'
        "}\n\n"
        f"Sentence: \"{text.strip()}\"\n"
        f"LST: {lst.strip()}"
    )

    res = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = res.choices[0].message.content.strip()

    if raw.startswith("```"):
        raw = raw.split("```")[-2].strip()

    block = raw[raw.find("{"): raw.rfind("}")+1]
    return json.loads(block)

reasonings, fallacies = [], []

for sentence, lst in zip(df["source_article"], df["lst"]):
    try:
        out = assess_fallacy(sentence, lst)
        reasonings.append(out["Reasoning"])
        fallacies.append(out["Predicted Fallacy"])
    except Exception as e:
        reasonings.append(f"ERROR: {e}")
        fallacies.append(None)
    time.sleep(1)

df["Reasoning"] = reasonings
df["Predicted Fallacy"] = fallacies
df.to_csv("climate_test_with_lst_assessed.csv", index=False)

print("Done — see climate_test_with_lst_assessed.csv")
