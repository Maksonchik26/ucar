# Отзывы пользователей — FastAPI mini-сервис

Сервис принимает текстовые отзывы, определяет их настроение (positive / negative / neutral) и сохраняет в базу данных.

## Установка и запуск

```bash
pip install -r requirements.txt
python3 main.py
```

## Эндпоинты
### POST /reviews
```bash
curl -X POST http://127.0.0.1:8000/reviews \
 -H "Content-Type: application/json" \
 -d '{"text": "Обожаю ваш сервис, хорошая работа!"}'
```

### GET /reviews?sentiment=(negative|positive|neutral)
```bash
curl "http://127.0.0.1:8000/reviews?sentiment=negative"
```

## Документация swager
http://127.0.0.1:8000/docs
