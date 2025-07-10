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
curl -X POST http://127.0.0.1:8000/reviews/ \
 -H "Content-Type: application/json" \
 -d '{"text": "Обожаю ваш сервис, хорошая работа!"}'
```
#### Пример ответа
```bash
{
  "id": 1,
  "text": "Обожаю ваш сервис, хорошая работа!",
  "sentiment": "positive",
  "created_at": "2025-07-09T12:34:56.789123"
}
```

### GET /reviews?sentiment=(negative|positive|neutral)
```bash
curl "http://127.0.0.1:8000/reviews/?sentiment=positive"
```
#### Пример ответа
```bash
[
  {
    "id": 2,
    "text": "Ненавижу интерфейс, очень плохо",
    "sentiment": "negative",
    "created_at": "2025-07-09T12:40:00.000000"
  }
]
```

## Документация swager
http://127.0.0.1:8000/docs
