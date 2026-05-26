"""
Demo 2：AI 翻譯機（英文 → 中文）
==============================

這個程式做什麼？
    你給 AI 一句英文，AI 翻成中文還給你。

怎麼跑？
    打開終端機，輸入：
        python demos/02_translate.py

第一次跑會發生什麼？
    1. 電腦會下載一個「英翻中」專用模型（大概 300 MB，1～2 分鐘）
    2. 跑完你會看到原文跟譯文一行行對照

跟 Demo 1 差在哪？
    這次我們**指定**了用哪一個模型（model="..."），
    因為翻譯有方向（英→中、中→英、英→日…），不能讓 HuggingFace 自己亂猜。
"""

from transformers import pipeline

# 建立翻譯機器
# - "translation" 是任務名稱
# - model="Helsinki-NLP/opus-mt-en-zh" 指定要用的模型
#   這個模型由芬蘭赫爾辛基大學（Helsinki）的 NLP 團隊訓練，專門做「英文 → 中文」
#   HuggingFace 上有超過 1000 個 Helsinki-NLP 的翻譯模型，涵蓋幾百種語言對
translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-zh",
)

# 準備幾句英文
english_sentences = [
    "Hello, world!",
    "I am learning artificial intelligence.",
    "Taiwan is a beautiful island.",
    "Programming is easier than people think.",
]

# 一次翻譯整批（比一句一句翻快很多）
results = translator(english_sentences)

# 印出對照表
print("\n=== AI 英翻中結果 ===\n")
for english, result in zip(english_sentences, results):
    chinese = result["translation_text"]
    print(f"原文：{english}")
    print(f"譯文：{chinese}\n")

print("=== 完成！===")
print("試試看：把英文句子換成你自己想翻譯的內容。")
print("提示：AI 翻譯出來不一定完美，有時會怪怪的，這是正常的。")
