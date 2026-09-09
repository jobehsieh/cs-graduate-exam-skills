---
name: cs-grad-exam-archiver
description: 資工所（資訊工程）碩士班入學考試考古題收集與歸檔。搜尋並下載台大、清大、交大(陽明交大)、成大、中央及台聯大聯招之資工所考古題，依科目類別（資料結構與演算法／線性代數／離散數學／作業系統／計算機組織）歸檔。當使用者要「收集考古題」「下載歷屆試題」「整理資工所考題」時使用。
---

# 資工所考古題收集與歸檔（cs-grad-exam-archiver）

## 用途
協助收集台清交成中央五校資工所碩士班入學考試考古題（近5年為原則），並依科目類別歸檔，作為模擬試題題庫來源。

## 各校官方考古題系統

| 學校 | 考古題入口 | 說明 |
|------|-----------|------|
| 台大 | https://exam.lib.ntu.edu.tw/graduate | 電機資訊學院→資訊工程學研究所，可線上下載 PDF |
| 清大 | https://www.lib.nthu.edu.tw/library/department/lrs/exam/ | 資工系數學考科近5年多標示「試題不公開」 |
| 陽明交大 | https://www.lib.nycu.edu.tw/custom?menu=120&cid=451 | 不提供線上下載，僅目次索引＋圖書館紙本 |
| 成大 | https://exam.lib.ncku.edu.tw | 電機資訊學院-資訊聯招（department_code=EC24），可下載 |
| 中央 | https://rapid.lib.ncu.edu.tw/cexamn/ | 資工系 EC02.html，可下載 |
| 台聯大聯招 | https://rapid.lib.ncu.edu.tw/cexamn/tai.html | 清交成央系統共同出題之電機類試題 |

## 科目類別與歸檔規則

建立「資工所考古題」資料夾，依科目建子資料夾，再依學校建次子資料夾：

```
資工所考古題/
├── 數學(綜合)/{學校}/    ← 綜合數學卷（含線代+離散，如台大「數學(A)」、成大「計算機數學」、中央「離散數學與線性代數」）
├── 資料結構與演算法/{學校}/
├── 線性代數/{學校}/
├── 離散數學/{學校}/
├── 作業系統/{學校}/
└── 計算機組織/{學校}/
```

## 下載流程（PowerShell / Invoke-WebRequest）

```powershell
$url = "<PDF 網址>"
$out = "<目標路徑>.pdf"
Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing
```

- 檔案命名：`{學校}_{年度}_{科目}.pdf`（如 `台大_114_數學(A).pdf`）。
- 台大數學卷網址格式：`https://exam.lib.ntu.edu.tw/sites/default/files/exam/graduate/{年}/{檔}.pdf`
- 成大計算機數學：`https://exam.lib.ncku.edu.tw/exam/EC24_{年}_3.pdf`
- 中央離散數學與線性代數：`https://rapid.lib.ncu.edu.tw/cexamn/exam/EC02_{年}_03.pdf`
- 台聯大聯招：資料結構 `tai/ec{年}4.pdf`、離散數學 `tai/ec{年}10.pdf`、計算機系統 `tai/ecc{年}.pdf`、工程數學 `tai/ecw{年}{abc}.pdf`

## 注意事項
- 清大、交大資工系多為獨立招生，官方數學考題常標示「試題不公開」；可改取台聯大聯招電機類試題作為系統出題之參考。
- 官方考古題僅提供試題、無解答。
- 完整連結彙整範例可參考專案文件 `docs/PROJECT_INDEX.md` 第 3 節。