# 1. Pythonの環境を使う
FROM python:3.9-slim

# 2. コンテナ内の作業ディレクトリを決める
WORKDIR /app

# 3. 必要なライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. プログラムをコンテナにコピー
COPY . .

# 5. Flaskを起動 (host=0.0.0.0で外からのアクセスを許可)
CMD ["python", "app.py"]