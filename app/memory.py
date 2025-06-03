import time

# 用戶訊息歷史記憶，實際部署請用 Redis 之類外部DB
user_memories = {}

def get_user_history(user_id, limit=5):
    # 取出使用者最近N輪對話，預設5輪
    if user_id not in user_memories:
        return []
    return user_memories[user_id][-limit:]

def add_user_message(user_id, role, content):
    if user_id not in user_memories:
        user_memories[user_id] = []
    user_memories[user_id].append({
        "role": role,
        "content": content,
        "ts": int(time.time())
    })
    # 控制最多留20輪，避免記憶體爆炸
    if len(user_memories[user_id]) > 20:
        user_memories[user_id] = user_memories[user_id][-20:]
