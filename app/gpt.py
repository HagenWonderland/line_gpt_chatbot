import os
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

DEFAULT_SYSTEM_PROMPT = """你是一位專業的智能數據分析助手。請注意：
1. 使用繁體中文回答所有問題
2. 提供專業、準確且易於理解的數據分析建議
3. 回答要簡潔明瞭，並適時使用重點列表
4. 需要時主動詢問更多資訊以提供更精確的答案
"""

async def chat_with_gpt(messages, model="gpt-3.5-turbo"):
    # 加入系統提示訊息
    if not any(msg.get("role") == "system" for msg in messages):
        messages.insert(0, {"role": "system", "content": DEFAULT_SYSTEM_PROMPT})
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "max_tokens": 1024,
        "temperature": 0.1,
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(OPENAI_API_URL, headers=headers, json=data, timeout=30)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
