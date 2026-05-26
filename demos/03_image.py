"""
Demo 3：AI 看圖認物
==================

這個程式做什麼？
    你給 AI 一張圖片（網路上的或你電腦裡的），
    AI 告訴你「這張圖最有可能是什麼」。

怎麼跑？
    打開終端機，輸入：
        python demos/03_image.py

第一次跑會發生什麼？
    1. 電腦會下載一個叫 ViT（Vision Transformer）的圖像模型（約 350 MB）
    2. AI 會分析範例圖片（一隻貓），印出前 5 名最有可能的答案

跟前兩個 Demo 差在哪？
    這次處理的是「圖片」而不是「文字」，
    但你會發現 ── HuggingFace 的用法幾乎一模一樣。
    這就是 pipeline() 的厲害：不管什麼類型的 AI 任務，介面都長得很像。
"""

from transformers import pipeline

# 建立圖片分類機器
# - "image-classification" 是任務名稱（看圖辨識物體）
# - 模型 google/vit-base-patch16-224 是 Google 訓練的 Vision Transformer
#   可以辨識 1000 種常見物體（動物、車、食物、家具等等）
classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224",
)

# 來辨識一張網路上的貓咪圖
# 這是 HuggingFace 官方範例常用的測試圖（一隻坐在沙發上的貓）
image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"

print(f"\n=== 正在辨識圖片 ===")
print(f"圖片網址：{image_url}\n")

# AI 看圖，回傳「前 5 名」最可能的答案
# top_k=5 意思是「給我前 5 名」，可以改成 top_k=10 看更多
results = classifier(image_url, top_k=5)

# 印出排行榜
print("=== AI 的猜測（信心度從高到低）===\n")
for rank, result in enumerate(results, start=1):
    label = result["label"]              # 物體名稱（英文）
    score = result["score"]              # 信心度 0～1
    bar = "█" * int(score * 30)          # 用方塊畫一個信心度長條
    print(f"  第 {rank} 名：{label}")
    print(f"          {bar} {score:.1%}\n")

print("=== 完成！===")
print()
print("試試看：")
print("1. 換成你自己的圖片網址（任何 .jpg / .png 都行）")
print("2. 或者把 image_url 換成本地圖片路徑，例如：")
print('   image_url = r"C:\\Users\\你的名字\\Pictures\\cat.jpg"')
print()
print("AI 能認的物體有 1000 種，包含：")
print("- 各種動物（狗、貓、鳥、魚...）")
print("- 各種食物（披薩、漢堡、壽司...）")
print("- 各種交通工具（車、船、飛機...）")
print("- 各種家具與生活用品")
