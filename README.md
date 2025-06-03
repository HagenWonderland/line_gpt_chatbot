# LINE GPT Chatbot (FastAPI)

A professional LINE chatbot powered by OpenAI GPT, built with FastAPI. This bot acts as an intelligent data assistant, responding in Traditional Chinese and supporting multi-turn conversations.

## Features

- **LINE Integration**: Seamlessly connects with LINE Messaging API.
- **OpenAI GPT Support**: Utilizes GPT-3.5/4 for intelligent, context-aware responses.
- **Multi-turn Memory**: Remembers recent user interactions for more natural conversations.
- **Professional Data Assistant**: Answers in Traditional Chinese with a focus on data analysis and user-friendly explanations.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

- Copy `.env.example` to `.env` and fill in your API keys.
- **MacOS users:**  
  Add your API keys to your `~/.zshrc` for security and convenience. For example:
  ```bash
  export OPENAI_API_KEY=your_openai_api_key
  export LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
  export LINE_CHANNEL_SECRET=your_line_channel_secret
  ```
  After editing, reload your shell:
  ```bash
  source ~/.zshrc
  ```

### 3. Run the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Configure LINE Webhook

Set your webhook URL in the LINE Developers Console to:
```
https://your-domain/webhook
```

## Project Structure

- `app/main.py` — FastAPI entry point and webhook endpoint
- `app/gpt.py` — Handles OpenAI GPT API integration
- `app/memory.py` — Manages user conversation history (in-memory, replace with DB for production)
- `app/line_handler.py` — Processes LINE events and message routing

## Notes

- This project uses in-memory storage for user history. For production, consider integrating Redis or another database.
- The bot is designed to answer in Traditional Chinese and provide professional data analysis support.

## License

MIT

