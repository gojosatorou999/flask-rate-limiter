# Flask Rate Guard 🛡️

A lightweight Flask application demonstrating robust request rate limiting based on User IP addresses. It uses `Flask-Limiter` to protect API endpoints from brute force and abuse.

## 🚀 Features
- **Global Rate Limiting**: Defaults to 200 requests/day and 50 requests/hour.
- **Route-Specific Limits**: Custom thresholds for sensitive endpoints (e.g., `/ping`, `/slow`).
- **IP Identification**: Automatically identifies users via their remote address.
- **Custom Error Responses**: Returns clean JSON errors when limits are exceeded.

## 🛠️ Logic Overview

The application uses `Flask-Limiter` with the following configuration:
1. **Key Function**: `get_remote_address` is used as the unique identifier for rate limiting. This ensures that limits are tracked per individual IP address.
2. **Storage**: Currently configured with `memory://`. For production, this can be easily swapped to `redis://` or `mongodb://` for persistent tracking.
3. **Decorators**: Routes are protected using the `@limiter.limit()` decorator, allowing for granular control over different API sections.

## 📦 Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```

## 🧪 Testing

- Access `http://127.0.0.1:5000/ping` more than 5 times in a minute to trigger the rate limit.
- You will receive a `429 Too Many Requests` response with a JSON body.

## 📜 License
MIT
