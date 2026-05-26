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
- Commit：`ad03575`
- 產出：`demos/03_image.py`、`demos/03_說明.md`
- 設計：跨模態（文字→圖片）但介面幾乎不變，凸顯 `pipeline()` 抽象化的價值
- 範例圖：用 COCO dataset 的公開圖片網址（不需要在 repo 內放圖檔，避免 repo 肥大）
- 教學重點：top_k 信心度長條圖、closed-set vs open-vocabulary 概念（埋點為「下一步學 CLIP」鋪路）

### M5 — 安裝指南 / 常見錯誤 / 下一步
- 產出：`docs/安裝指南.md`、`docs/常見錯誤.md`、`docs/下一步.md`
- 安裝指南：Win/Mac 兩平台、虛擬環境步驟、完整 troubleshooting
- 常見錯誤：8 個高頻錯誤的 root cause + 解法（包含中國/firewall 環境的鏡像設定）
- 下一步：學習地圖（高中生路線、大學生路線）、中期關鍵字（fine-tune、LoRA、RAG、Embedding）、心態建議
- 最後一個 demo 跑完到知道「之後該學什麼」之間，幫初學者銜接完整

---

## 第二輪：Notebook 版本（/safe-yolo 2026-05-26）

### 動機
原本 3 個 demo 是 `.py`，從終端機一次跑完。對「完全沒寫過程式」的目標受眾來說：
- 看不到中間每一步的狀態
- 想改參數要在編輯器跟終端機之間切換
- Demo 3 看不到要辨識的圖片本身

→ 新增對應的 `.ipynb` 版，每步驟一格、有 markdown 介紹、可即時改、可顯示圖片。

### N1 — Demo 1 Notebook（情感分析）
- Commit：`52afef3`
- 產出：`demos/01_sentiment.ipynb`
- 設計：6 個 markdown 介紹 + 6 個 code cell，含「動手玩玩看」可編輯區
- 回顧 cell：用 markdown 收尾講 3 個關鍵步驟 + DistilBERT 抽象層概念

### N2 — Demo 2 Notebook（翻譯）
- Commit：`36eab57`
- 產出：`demos/02_translate.ipynb`
- 設計：除了英翻中之外，新增中翻英 bonus cell 讓學生體驗反方向
- 故意保留 Programming→規劃 翻錯的 markdown 警示

### N3 — Demo 3 Notebook（圖片辨識）
- Commit：`435916e`
- 產出：`demos/03_image.ipynb`
- 設計：用 `IPython.display.Image` 直接在 notebook 內顯示要辨識的圖片（.py 版做不到）
- 三段動手玩玩看：picsum 隨機圖、本地圖片路徑、批次三張一起跑

### N4 — 文件更新串接
- 產出：`README.md`、`docs/安裝指南.md`、`requirements.txt`
- README：表格化「.py vs .ipynb 怎麼選」，建議完全新手用 .ipynb
- 安裝指南：Step 5 拆兩種方法（Jupyter / 終端機）
- requirements：加入 `notebook>=7.0`

---

## 第三輪：發佈到 GitHub（/safe-yolo 2026-05-26）

### P1 — 預檢 + 建立 remote repo
- 帳號：`gsinvest017-ai`（gh auth 既有）
- 預檢：working tree clean、無 .env / secret-named 檔案、tracked files 只有 markdown / py / ipynb
- 公開度：**public**（教學專案，內容適合分享；若要改私有：`gh repo edit --visibility private`）
- 指令：`gh repo create hf-tutorial-beginner --public --source=. --description "..."`
- Remote URL：https://github.com/gsinvest017-ai/hf-tutorial-beginner

### P2 — Push 全部 commits
- `git push -u origin main`
- 已 push commits：`0c9aa5e..ca5f091`（M1–M5 + N1–N4，共 9 個 commits）
- branch `main` 已 tracking `origin/main`

## Fallback 指引

若中途被接手或需要 rollback：
- `git log --oneline` 看 milestone commit
- `git reset --hard <M{n-1} commit>` 退回上一個 milestone
- 進度檔本身會記錄每個 milestone 完成的 commit hash
- 所有 demo 互相獨立，移除任一個 demo 不會影響其他 demo
- 想保留 .py 版、移除 .ipynb 版：`git rm demos/*.ipynb` 然後 revert README/安裝指南/requirements.txt 的對應段落（commit N4 之後）
- 想撤回 GitHub 發佈：
  - 改私有：`gh repo edit gsinvest017-ai/hf-tutorial-beginner --visibility private --accept-visibility-change-consequences`
  - 完全刪除（不可逆）：`gh repo delete gsinvest017-ai/hf-tutorial-beginner --yes`
