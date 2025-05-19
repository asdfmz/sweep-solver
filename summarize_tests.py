import subprocess
import json
import sys
import os

def main():
    # テスト対象が指定されていなければエラー
    if len(sys.argv) < 2:
        print("使用法: python summarize_tests.py <テスト対象>")
        print("例: python summarize_tests.py tests/test_sympy_codec.py")
        sys.exit(1)

    # コマンドライン引数からテスト対象を取得
    test_target = sys.argv[1:]

    # JSON出力用ファイル名（重複防止のため明示的に指定）
    report_file = "report.json"

    # pytestをサブプロセスで実行
    subprocess.run(
        ["pytest", "--json-report", f"--json-report-file={report_file}"] + test_target,
        check=False
    )

    # 結果ファイルが存在するかチェック
    if not os.path.exists(report_file):
        print("エラーレポートファイルが見つかりません。pytestが失敗した可能性があります。")
        sys.exit(1)

    # JSONを読み込む
    with open(report_file, encoding="utf-8") as f:
        data = json.load(f)

    # 失敗テストの要約を表示
    print("\n【失敗したテスト一覧】\n")

    failures = [t for t in data["tests"] if t["outcome"] == "failed"]

    if not failures:
        print("🎉 すべてのテストが成功しました！")
    else:
        for i, test in enumerate(failures, 1):
            name = test["nodeid"]
            msg = test.get("call", {}).get("crash", {}).get("message", "")
            last_line = msg.strip().splitlines()[-1] if msg else "（エラー詳細取得失敗）"
            print(f"{i}. {name}\n   → {last_line}\n")

if __name__ == "__main__":
    main()
