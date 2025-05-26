# Sweep Solver ― 行基本変形・掃き出し法ツール

![demo](docs/demo.gif) <!-- ← 後で追加予定のGIF -->

**Sweep Solver** は、行基本変形をステップごとに確認しながら実行できる、シンプルなWebツールです。連立一次方程式や逆行列の、掃き出し法による求解に活用できます。

🌐 リンク → [https://sweep-solver.com](https://sweep-solver.com)

---

## 🔧 主な機能

- 行列サイズを指定して値を入力
- 行基本変形（加算・定数倍・交換）をインタラクティブに実行
- 自動で掃き出し法を行う機能
- 履歴表示やステップのやり直し機能
- 分数・ルート・複素数にも対応
- スマホ表示にも対応

---

## ⚙️ 技術スタック

- Python 3
- Flask
- HTML / CSS / JavaScript
- Gunicorn
- Nginx

---

## 🧠 設計概要

行基本変形は内部的に `Query` インスタンスとして構造化され、Pythonの `SymPy` による行列操作が行われます。ステップの履歴は JSON シリアライズ可能な形式に変換され、Flaskのセッションに保存されています。

また、インタラクティブページでは PRG（Post/Redirect/Get）パターンを採用し、再投稿やセッションの不整合を回避する構成になっています。

---

## 📄 ライセンス

MIT License

---

## 🛠 導入方法（開発者向け）

以下の手順でローカル実行できます。

```bash
git clone https://github.com/asdfmz/sweep-solver.git
cd sweep-solver
python3 -m venv venv
source venv/bin/activate  # Windowsの場合は venv\Scripts\activate
pip install -r requirements.txt
flask run
```

---

© 2025 asdfmz
