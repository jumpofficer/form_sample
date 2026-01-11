from flask import Flask, render_template, request

app = Flask(__name__)

# 1. 入力画面 (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# 2. 確認画面 (index_confirm.html)
@app.route('/index_confirm')
def confirm():
    # フォームから送られてきたデータ(GET)をすべて辞書として取得
    # HTMLの name="○○" という名前でデータが入ってきます
    form_data = request.args.to_dict()
    
    # 取得したデータを、確認画面へ渡す
    return render_template('index_confirm.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)