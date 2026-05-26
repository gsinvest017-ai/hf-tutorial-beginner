# 我的第一個 AI ─ HuggingFace 三分鐘入門

> 給完全沒寫過程式的高中 / 大學新生

## 這是什麼？

這是一個讓你「**第一次跑出 AI**」的小教學。
你會在 15 分鐘內，**親手讓 AI**：

1. 看一句話，告訴你這句話是開心還是難過
2. 把英文翻譯成中文
3. 看一張圖片，告訴你裡面是什麼動物 / 物品

全部加起來，**你只需要寫 10 行左右的程式**。

## 什麼是 HuggingFace？

想像一下：
- **App Store** 裡面有幾百萬個 app，你不用自己寫，下載就能用
- **HuggingFace** 裡面有幾十萬個「**AI 模型**」，你不用自己訓練，下載就能用

差別在哪？
- App Store 的 app 是給人用的（點按鈕、滑來滑去）
- HuggingFace 的 AI 模型是給「**程式**」用的（你寫幾行 Python，就能呼叫 AI 幫你做事）

而且 **絕大多數模型完全免費**。

## 為什麼學這個？

- 你會發現「跑 AI」其實**比想像中簡單一萬倍**
- 你會知道 ChatGPT 這類東西「**背後在做什麼**」
- 履歷可以寫「我會用 HuggingFace 呼叫 AI 模型」（這是真的，不是吹牛）
- 之後想做專題、想做小 side project，AI 是現成的零件

## 開始之前你只需要

1. 一台**可以連網的電腦**（Windows / Mac 都行）
2. **15 分鐘**
3. 看得懂中文（程式碼註解全是中文）

完全不用懂：
- ❌ 機器學習
- ❌ 線性代數
- ❌ 神經網路
- ❌ 英文

## 開始

依照順序看：

1. **先讀** [`docs/安裝指南.md`](docs/安裝指南.md) ─ 教你裝 Python 跟 HuggingFace（一次就好）
2. **再跑** Demo 1：[`demos/01_sentiment.py`](demos/01_sentiment.py) 或 [`demos/01_sentiment.ipynb`](demos/01_sentiment.ipynb) ─ 你的第一個 AI（5 行）
3. **接著** Demo 2：[`demos/02_translate.py`](demos/02_translate.py) 或 [`demos/02_translate.ipynb`](demos/02_translate.ipynb) ─ AI 翻譯機
4. **最後** Demo 3：[`demos/03_image.py`](demos/03_image.py) 或 [`demos/03_image.ipynb`](demos/03_image.ipynb) ─ AI 看圖認物
5. **卡關時** 查 [`docs/常見錯誤.md`](docs/常見錯誤.md)
6. **想繼續學** 看 [`docs/下一步.md`](docs/下一步.md)

### 兩種版本怎麼選？

每個 demo 都有 **`.py`** 跟 **`.ipynb`** 兩個版本，挑一個喜歡的就好：

| 版本 | 適合誰 | 怎麼跑 |
|---|---|---|
| **`.py`**（純 Python 檔） | 想看完整程式、從終端機一鍵跑完 | `python demos/01_sentiment.py` |
| **`.ipynb`**（Jupyter Notebook） | 想**一格一格慢慢跑**、邊看輸出邊學 | `jupyter notebook`（會打開瀏覽器） |

**完全沒寫過程式強烈推薦 `.ipynb` 版**：每一步都有 markdown 說明、可以即時改參數重跑、Demo 3 還能直接在 notebook 內看到要辨識的圖片。

## 一句話總結

> 過去要博士才能做的事，現在你寫 3 行 Python 就能做。歡迎來到 2026 年。
