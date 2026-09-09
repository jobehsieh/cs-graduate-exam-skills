---
name: md-to-pdf
description: Markdown 轉 PDF 工具（支援 LaTeX 數學公式與中文）。把含 $...$/$$...$$ 數學公式的 Markdown 文件轉成 A4 PDF（Markdown→HTML→MathJax 渲染→Playwright 列印）。另附 PDF 文字層抽取工具（PyMuPDF）。當使用者要「把 Markdown 轉成 PDF」「產生 PDF 文件」「抽取 PDF 文字」時使用。
---

# Markdown → PDF 轉換（md-to-pdf）

## 用途
將含 LaTeX 數學公式與中文的 Markdown 文件轉為 A4 PDF，適用於試卷、教材、報告等文件。

## 前置安裝

```bash
pip install markdown playwright PyMuPDF
playwright install chromium
```

## 使用方式

### 1. Markdown → PDF
```bash
python md2pdf.py <輸入.md> <輸出.pdf>
```

- 支援 `$...$`（行內）與 `$$...$$`（獨立行）LaTeX 公式，透過 MathJax 渲染。
- 中文字體自動使用 Microsoft JhengHei；A4、留邊。
- 公式先以佔位符保護，避免被 Markdown 語法破壞。

### 2. 抽取 PDF 文字層（掃描檔會回傳空字串）
```bash
python pdf_extract.py <輸入.pdf> [最大頁數，預設4]
```
- 使用 PyMuPDF 抽取文字層；掃描影像型 PDF 會得到空白，需改以 OCR 或視覺工具處理。

## 技術流程
1. 讀取 Markdown，將 `$$...$$`、`$...$` 公式替換為佔位符。
2. `markdown` 套件（extensions: tables, fenced_code, sane_lists）轉 HTML。
3. 還原公式，嵌入 MathJax 3（tex-svg）與 CSS。
4. Playwright Chromium 開啟 `file://` 頁面，等待 `MathJax.startup.promise` 完成後 `page.pdf()` 輸出 A4 PDF。

## 已知限制
- 需要網路連線（MathJax CDN）以渲染公式。
- 深層巢狀表格或特殊字元可能需人工檢查排版。
- 掃描影像 PDF 無文字層時，`pdf_extract.py` 無法抽出文字；如需讀圖請搭配視覺模型。