FROM python:3.8-slim
 
WORKDIR /app
 
COPY . /app
 
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
 
EXPOSE 8000
 
ENV NAME sample
 
# Run gunicorn when the container launches and bind port 8000 from app.py
CMD ["gunicorn", "-b", ":8000", "app:app"]