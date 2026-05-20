FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY school_calendar ./school_calendar
COPY exam_creator ./exam_creator
COPY whiteboard ./whiteboard
COPY static ./static
COPY lessons ./lessons

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
