---
name: exam-paper-format-ocr
description: 考古題卷面格式視覺辨識。當掃描影像型 PDF（無文字層）無法直接讀取時，用 Groq Vision API 將 PDF/圖片轉成文字描述，確認考卷卷面格式（卷頭欄位、題號與配分格式、題型結構）。當使用者要「讀取掃描考卷」「確認考古題格式」「OCR 考古題 PDF」「辨識考卷版面」時使用。需要 GROQ_API_KEY。
---

# 考古題卷面格式視覺辨識（exam-paper-format-ocr）

## 用途
各校官方考古題 PDF 多為**掃描影像**（無文字層，`PyMuPDF` 抽取文字為空白）。本 Skill 用 **Groq 免費 Vision API** 把掃描 PDF 逐頁轉成 PNG 再轉為文字描述，據以確認考卷的卷面格式（卷頭、題號/配分格式、題型結構），作為生成模擬試題的格式依據。

## 何時用、何時不用

| 情況 | 做法 |
|------|------|
| PDF 有**文字層** | 直接用 `pdf_extract.py`（PyMuPDF）抽文字，更快更準，不需 API |
| PDF 為**掃描影像**（無文字層） | 用本 Skill 之 `vision.py` 走 Groq Vision |
| 主模型支援視覺輸入 | 直接把 PDF 餵給主模型，不需本 Skill |

> 判斷方式：先跑 `python pdf_extract.py <檔.pdf>`，若輸出空白即為掃描影像。

## 前置安裝

```bash
pip install -r requirements.txt   # groq, pymupdf, python-pptx, python-docx, pillow
```

### Groq API Key（免費）
1. 至 https://console.groq.com 註冊 → API Keys → Create API Key（`gsk_...`）。
2. 儲存：環境變數 `GROQ_API_KEY=<key>`，或存至 `~/.groq_api_key`。
3. ⚠️ 檔案內容會上傳至 Groq（美國伺服器）；處理未公開資料前先告知使用者並建議脫敏。

## 使用方式

```bash
# OCR：抽取卷面文字（確認題號/配分/題目文字，推薦）
python vision.py <檔案路徑> --mode ocr --output <輸出.md>

# describe：詳細描述版面（物件、顏色、文字、結構）
python vision.py <檔案路徑> --mode describe --output <輸出.md>
```

- 支援：PNG/JPG/WEBP/BMP/GIF（直接送圖）、PDF（每頁轉 150dpi PNG 逐頁描述）、PPTX、DOCX。
- 輸出預設在檔案同目錄 `<檔名>.vision.md`；可用 `--output` 指定。
- **頁數過多會觸發 Groq 免費額度限流**：可先用 `pdf2png` 方式只轉前 2 頁再辨識（格式多在首頁），或分批處理。

## 流程 SOP

1. 確認檔案存在：`Test-Path <路徑>`。
2. 先抽文字層：`python pdf_extract.py <檔.pdf>`；若有文字直接用，結束。
3. 若為掃描影像：`python vision.py <檔.pdf> --mode ocr --output <輸出.md>`。
4. 讀取輸出之 `<輸出.md>`，摘錄：卷頭欄位、題號與配分格式、題型結構、語言。
5. 將確認結果對照 `EXAM_SPEC.md` §1.5（114 年實測格式）回填或比對。

## 114 年實測格式參考（本流程產出）

| 學校 | 卷頭欄位 | 題號/配分格式 | 題型特色 |
|------|----------|--------------|----------|
| 台大（數學(A)） | 「國立臺灣大學 114 學年度碩士班招生考試試題」＋題號/科目/節次 | 「1. (5%)」逐小題標百分比 | 多選「Which ones…」＋填空＋計算；英文 |
| 成大（計算機數學） | 卷頭含編號/系所/科目/日期/節次/注意 | 大題「一、離散數學(50%)」＋小題「1. (10%)」 | 單選(a)-(d)、是非題(a)-(e)各(2%)；英文 |
| 中央（離散數學與線性代數） | 卷頭含系所/科目/禁用計算器 | 「第一部分：共20分…錯一題倒扣2分」 | 單選(a)-(e)含倒扣；英文 |

## 注意事項
- Groq 免費方案有速率限制，大量圖片可能觸發限流（錯誤訊息會提示重試）。
- 模型下架時，`vision.py` 會自動檢查現有 Vision 模型；可 `--model <其他模型>` 指定。
- 隱私：掃描卷若含非公開內容，上傳前需取得使用者同意。