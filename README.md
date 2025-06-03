# LINE GPT Chatbot (FastAPI)

## Quick Start

1. 安裝套件 `pip install -r requirements.txt`
2. 複製 `.env.example` -> `.env` 並填入金鑰
3. 啟動: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
4. 將 https://你的domain/webhook 設為 LINE Webhook URL

## Folders

- app/main.py: FastAPI 主程式
- app/gpt.py: GPT-4/gpt-4o 調用
- app/memory.py: 使用者多輪記憶
- app/line_handler.py: LINE 訊息處理
