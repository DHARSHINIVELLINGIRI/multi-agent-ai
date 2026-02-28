FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Running uvicorn from the root folder pointing to the app module
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]