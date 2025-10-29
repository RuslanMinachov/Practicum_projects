# Sentiment Analysis API

API для классификации тональности русскоязычных отзывов с использованием модели `rubert-tiny-sentiment-balanced`.

## Эндпоинты

- `GET /` — проверка работоспособности
- `GET /status` — статус модели
- `POST /predict` — предсказание тональности

## Требования

- Python 3.8+
- FastAPI, Uvicorn, Transformers, Torch

## Установка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
