# 閩南語注音工具 v1.01 Beta

一個用於為繁體中文 `.txt` 文檔進行**臺灣閩南語文讀台羅拼音注音**的小工具。

預設使用臺灣教育部的《閩南語常用詞辭典》作為讀音字典，也可選擇使用《說文解字》中**唐韻反切音**進行注音。

> 📌 當使用預設的教育部字典時，會**優先使用文讀音**；若無文讀音，則會註解所有可查得的讀音。若該字在教育部字典與《說文解字》中皆無對應資料，則會留空不注音。  
> 📌 使用唐韻反切注音時，程式會嘗試將該字套入預設字典，再進行拼音拼接，查無結果時將直接註記原始反切音。

⚠️ 本工具僅供學術研究與學習使用。

---

## 📥 使用方式

1. 將欲注音的繁體文本內容貼入專案根目錄下的 `text.txt`。
2. 執行 `main.py`，依提示選擇：
   - 是否於教育部字典查無結果時查詢《說文解字》庫
   - 是否使用多執行緒加速查詢（視電腦配置與資料庫大小，不一定更快）
3. 輸入輸出檔案的名稱（例如 `output.txt`）

---

## ⚠️ 注意事項

- 目前仍有部分字在臺灣教育部字典與《說文解字》中皆查無結果，需後續手動補充至字典中。
- 注音結果為自動生成，可能與實際語音略有出入，請以母語者語音為準。

---

## 💡 支援資料來源

- 📘 教育部臺灣閩南語常用詞辭典：  
  [https://sutian.moe.edu.tw/zh-hant/siongkuantsuguan/](https://sutian.moe.edu.tw/zh-hant/siongkuantsuguan/)
  
- 📗 《說文解字》數據庫（shuowenjiezi/shuowen）：  
  [https://github.com/shuowenjiezi/shuowen/blob/master](https://github.com/shuowenjiezi/shuowen/blob/master)

---

## 📄 授權

本專案使用來自 `shuowenjiezi/shuowen` 的《說文解字》數據庫，其原始授權為 Apache License。  
本專案已在 `shuowen-master` 目錄中保留原始授權聲明。

---



