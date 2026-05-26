"""
Demo 1：你的第一個 AI（情感分析）
================================

這個程式做什麼？
    你給 AI 一句話，AI 告訴你這句話是「正面（開心）」還是「負面（難過）」。

怎麼跑？
    打開終端機，輸入：
        python demos/01_sentiment.py

第一次跑會發生什麼？
    1. 電腦會「下載」一個 AI 模型（大概 250 MB，要等 1～2 分鐘）
    2. 之後跑同一個程式就不用再下載了，會很快
    3. 跑完你會看到結果像：[{'label': 'POSITIVE', 'score': 0.99}]
       意思是「AI 99% 確定這句話是正面的」
"""

# 第 1 行：從 transformers 這個套件，借一個叫 pipeline 的工具
# pipeline 是 HuggingFace 最簡單的入口，就像「一鍵 AI」按鈕
from transformers import pipeline

# 第 2 行：建立一個「情感分析機器」
# "sentiment-analysis" 是告訴 HuggingFace：「我要的是情感分析這項功能」
# HuggingFace 會自動幫你下載一個適合的 AI 模型
classifier = pipeline("sentiment-analysis")

# 第 3 行：準備幾句要分析的話
sentences = [
    "I love this movie, it's amazing!",      # 「我超愛這部電影！」→ 應該是正面
    "This is the worst day of my life.",     # 「今天是我人生最爛的一天」→ 應該是負面
    "The food was okay, nothing special.",   # 「東西還好，沒什麼特別」→ 中性偏負面
]

# 第 4 行：把句子交給 AI，AI 會回傳一個結果清單
results = classifier(sentences)

# 第 5～7 行：把結果印出來給你看
# zip(...) 是 Python 的小技巧，可以「同時跑兩個清單」
print("\n=== AI 情感分析結果 ===\n")
for sentence, result in zip(sentences, results):
    label = result["label"]              # POSITIVE 或 NEGATIVE
    score = result["score"]              # AI 的信心度，0～1 之間
    emoji = "😊" if label == "POSITIVE" else "😢"
    print(f"{emoji} 句子：{sentence}")
    print(f"   AI 判斷：{label}（信心 {score:.1%}）\n")

print("=== 完成！===")
print("試試看：把上面 sentences 裡的句子改成你自己的，再跑一次。")
