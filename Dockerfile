FROM python:3-alpine
COPY . .
WORKDIR /app
RUN pip install -r requirements.txt
#EXPOSE 8777
CMD ["python", "MainGame.py", "MainScores.py"]