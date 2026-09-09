# cs-graduate-exam-skills

資工所（資訊工程）碩士班入學考試備考與出題的 **OpenCode Skills 集合**，供 AI Agent 參考使用。

整合了：台清交成中央考古題收集、模擬試題／解答卷生成、應試教材研究、Markdown→PDF 工具，並以台清交成中央 **114 學年度考古題實測格式**為規格依據。

## Skills

| Skill | 用途 | 位置 |
|-------|------|------|
| **cs-grad-exam-archiver** | 搜尋/下載台清交成中央與台聯大聯招資工所考古題，依科目歸檔 | `skills/cs-grad-exam-archiver/` |
| **mock-exam-generator** | 依考卷格式規格生成模擬試題卷＋解答卷（PDF，含計分） | `skills/mock-exam-generator/` |
| **exam-materials-research** | 研究各科應試教材/題庫（電子檔＋解答管道） | `skills/exam-materials-research/` |
| **md-to-pdf** | Markdown→PDF（MathJax 公式＋中文）與 PDF 文字抽取工具 | `skills/md-to-pdf/` |
| **exam-paper-format-ocr** | 掃描型考古題 PDF 之卷面格式視覺辨識（Groq Vision OCR） | `skills/exam-paper-format-ocr/` |

## 快速開始

1. **收集考古題**：載入 `cs-grad-exam-archiver`，依各校官方系統下載並歸檔。
2. **辨識考卷格式**：掃描型考古題 PDF 用 `exam-paper-format-ocr`（Groq Vision OCR）確認卷面格式。
3. **研究教材**：載入 `exam-materials-research`，取得各科題庫與教材來源。
4. **生成考卷**：載入 `mock-exam-generator`（先讀其內附 `EXAM_SPEC.md` 與 `EXAM_PROMPT.md`），生成試題卷＋解答卷。
5. **輸出 PDF**：用 `md-to-pdf` 把 Markdown 考卷轉為 A4 PDF。

## 目錄結構

```
cs-graduate-exam-skills/
├── README.md
├── docs/
│   ├── PROJECT_INDEX.md            # 專案檔案索引
│   └── materials-and-textbooks.md  # 各科教材/題庫/管道
└── skills/
    ├── cs-grad-exam-archiver/SKILL.md
    ├── mock-exam-generator/        # SKILL.md + EXAM_SPEC.md + EXAM_PROMPT.md
    ├── exam-materials-research/SKILL.md
    ├── exam-paper-format-ocr/      # SKILL.md + vision.py + requirements.txt
    └── md-to-pdf/                  # SKILL.md + md2pdf.py + pdf_extract.py
```

## 安裝為 OpenCode Skill

將 `skills/` 下任一資料夾複製到 OpenCode 技能目錄（如 `~/.config/opencode/skills/`），即可被 Agent 依 description 自動觸發。

## 授權與聲明

- 本專案僅彙整**各校官方公開考古題**與**正規出版教材**之資訊，不包含任何未授權之試題或書籍內容。
- 考古題版權屬各校，教材版權屬各出版社；本專案僅提供連結、格式規格與生成流程。