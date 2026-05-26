# 進度檔：HuggingFace 給完全新手的最簡教學

## 目標

寫一個給「完全不會程式」的高中一年級 / 大學一年級新生看的 HuggingFace 教學專案。
要求：
- 每個 demo ≤ 10 行程式碼
- 全程繁體中文註解
- 從 zero 到看到 AI 跑出結果不超過 15 分鐘
- 用 `pipeline()` 高階 API，不碰 tokenizer / model class
- 視覺化或有趣的輸出讓初學者有成就感

## 受眾假設

- 從沒寫過任何程式
- 不知道什麼是 Python / pip / 終端機
- 看到英文錯誤訊息會放棄
- 但對 AI 有好奇心，看過 ChatGPT

## 計畫 milestone

- **M1** — 專案骨架 + README + 進度檔
  - 預期產出：資料夾結構、`README.md`（含「這是什麼」「為什麼學」「怎麼開始」）、`requirements.txt`
- **M2** — Demo 1：情感分析（你的第一個 AI）
  - 預期產出：`demos/01_sentiment.py` + `demos/01_說明.md`
- **M3** — Demo 2：中英翻譯
  - 預期產出：`demos/02_translate.py` + `demos/02_說明.md`
- **M4** — Demo 3：圖片辨識（這張圖是什麼？）
  - 預期產出：`demos/03_image.py` + `demos/03_說明.md` + 範例圖片
- **M5** — 收尾：安裝指南、常見錯誤、下一步學什麼
  - 預期產出：`docs/安裝指南.md`、`docs/常見錯誤.md`、`docs/下一步.md`

## 進度日誌

### M1 — 專案骨架 + README + 進度檔
- Commit：`0c9aa5e`
- 產出：`README.md`、`requirements.txt`、`.gitignore`、`docs/progress-*.md`
- 決策：用 `pipeline()` 高階 API 不碰底層；全 demo 互相獨立可單獨跑

### M2 — Demo 1 情感分析
- Commit：`0195cd7`
- 產出：`demos/01_sentiment.py`、`demos/01_說明.md`
- 設計：5 行核心程式碼 + 完整中文逐行註解；3 句範例輸入示範 POSITIVE/NEGATIVE/邊界 case
- 對初學者的取捨：說明檔特別解釋「為什麼這麼短」（抽象層概念）以及背後 5 步驟，但不要求理解

### M3 — Demo 2 英翻中
- Commit：`d764bc7`
- 產出：`demos/02_translate.py`、`demos/02_說明.md`
- 設計：引入「指定模型」概念（`model="Helsinki-NLP/opus-mt-en-zh"`），解釋為何翻譯不能讓 HuggingFace 自選
- 教學重點：模型名格式 `發佈者/模型名` 類比 GitHub repo；故意保留一個翻譯錯誤的例子（Programming→規劃）來教「模型有缺點」這件事

### M4 — Demo 3 圖片辨識
- 產出：`demos/03_image.py`、`demos/03_說明.md`
- 設計：跨模態（文字→圖片）但介面幾乎不變，凸顯 `pipeline()` 抽象化的價值
- 範例圖：用 COCO dataset 的公開圖片網址（不需要在 repo 內放圖檔，避免 repo 肥大）
- 教學重點：top_k 信心度長條圖、closed-set vs open-vocabulary 概念（埋點為「下一步學 CLIP」鋪路）

## Fallback 指引

若中途被接手或需要 rollback：
- `git log --oneline` 看 milestone commit
- `git reset --hard <M{n-1} commit>` 退回上一個 milestone
- 進度檔本身會記錄每個 milestone 完成的 commit hash
- 所有 demo 互相獨立，移除任一個 demo 不會影響其他 demo
