FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirments.txt

COPY . .
CMD ["streamlit", "run", "streamlit_app.py"]