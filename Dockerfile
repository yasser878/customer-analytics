FROM python:3.11-slim

WORKDIR /app/pipeline

COPY . .

RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

CMD ["bash"]