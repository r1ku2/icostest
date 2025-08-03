from flask import Flask, request, redirect, render_template_string
import os


app = Flask(__name__)

STORAGE_PATH = "/mnt/storage"
TEXT_FILE_PATH = os.path.join(STORAGE_PATH, "user_input.txt")

@app.route("/", methods=["GET", "POST"])
def handle_text():
    message = ""
    if request.method == "POST":
        user_text = request.form.get("text_input", "")
        try:
            with open(TEXT_FILE_PATH, "w") as f:
                f.write(user_text)
            message = "✅ テキストが保存されました！"
        except Exception as e:
            message = f"❌ エラー: {str(e)}"

    # 入力フォームのHTML
    template = """
    <h1>Text Input Form</h1>
    <form method="POST">
        <textarea name="text_input" rows="10" cols="50" placeholder="ここにテキストを入力"></textarea><br>
        <button type="submit">保存</button>
    </form>
    <p>{{ message }}</p>
    {% if saved_text %}
    <h2>保存済みテキスト:</h2>
    <pre>{{ saved_text }}</pre>
    {% endif %}
    """

    # 保存済みのテキストを読み込む（あれば表示）
    saved_text = ""
    if os.path.exists(TEXT_FILE_PATH):
        with open(TEXT_FILE_PATH, "r") as f:
            saved_text = f.read()

    return render_template_string(template, message=message, saved_text=saved_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)