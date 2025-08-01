# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# 依存関係のコピーとインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリコードをコピー
COPY app.py .

# ポートを指定（Code Engine が使用）
ENV PORT=8080
EXPOSE 8080

# 起動コマンド
CMD ["python", "app.py"]