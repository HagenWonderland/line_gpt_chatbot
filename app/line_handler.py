import os
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from .gpt import chat_with_gpt
from .memory import get_user_history, add_user_message

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(os.getenv("LINE_CHANNEL_SECRET"))

async def handle_line_event(body, signature):
    events = parser.parse(body, signature)
    tasks = []
    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
            user_id = event.source.user_id
            user_message = event.message.text

            # 記錄用戶訊息
            add_user_message(user_id, "user", user_message)
            # 取得記憶(多輪)
            history = get_user_history(user_id)
            gpt_messages = [{"role": h["role"], "content": h["content"]} for h in history]

            # call GPT API
            gpt_reply = await chat_with_gpt(gpt_messages)
            # 記錄機器人回應
            add_user_message(user_id, "assistant", gpt_reply)

            # 回LINE
            tasks.append(line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=gpt_reply)
            ))
    # 等所有回覆執行完
    return tasks
