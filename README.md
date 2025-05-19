# Sweep Solver — A Structured Matrix Row Operation Tool

Sweep Solver は、行列の行基本変形・掃き出し法を対話的に実行できる Web ツールです。  
このリポジトリは、その構造的設計・実装・テスト・運用を一貫して記録・公開することを目的としています。

## 🧠 設計思想

- モジュールごとの責務分離（MVC的な思想）
- 状態管理の明示性とセッションベースの履歴復元
- 操作履歴の段階的出力（LaTeX形式など）
- 将来的なAPI連携・アプリ化を見据えた設計
- テスト駆動と可視化を意識した開発

## 📁 ファイル構成（初期）

```
sweep_solver/
├── app.py                     # Entry point / Blueprint registration
├── routes/interactive.py      # Flask route definitions
├── models/                    # 状態・操作の内部表現
│   ├── query.py
│   ├── matrix_state.py
│   └── session_manager.py
├── services/                  # 実処理ロジック（掃き出し法など）
│   ├── row_operations.py
│   └── auto_solver.py
├── views/                     # 表示形式変換（Latex・履歴構造）
│   ├── formatter.py
│   └── history_view_model.py
├── utils/                     # 汎用ユーティリティ（SymPy⇔JSONなど）
│   └── sympy_codec.py
├── templates/interactive.html # UIテンプレート
├── tests/                     # 各層の単体テスト
│   └── test_*.py
```

## 🚧 実装状況

現在は設計と構成構築のみ完了しています。  
今後は以下の順に実装・テストを進めていきます：

1. models/query.py
2. utils/sympy_codec.py
3. services/row_operations.py
4. models/matrix_state.py
5. models/session_manager.py
6. views/formatter.py
7. views/history_view_model.py
8. services/auto_solver.py
9. routes/interactive.py
10. app.py
11. templates/interactive.html

## 🔭 今後の展望

- Render/VPS へのデプロイと公開運用
- スマホアプリ化

---

© 2025 asdfmz
