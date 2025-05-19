import subprocess
import json
import sys
import os

def extract_main_error(message: str, max_lines: int = 3) -> str:
    """
    エラーメッセージの中から、AssertionErrorなどを含む代表的なエラーブロックを抽出
    """
    lines = message.strip().splitlines()
    for i, line in enumerate(lines):
        if "Error" in line or "Exception" in line:
            block = lines[i:i+max_lines]
            return "\n   ".join(block)
    return lines[-1] if lines else "（エラー詳細取得失敗）"

def main():
    if len(sys.argv) < 2:
        print("使用法: python summarize_tests.py <テスト対象> [--full]")
        sys.exit(1)

    # フラグとテスト対象を分けて解釈
    args = sys.argv[1:]
    is_full = "--full" in args
    test_targets = [arg for arg in args if not arg.startswith("--")]

    if not test_targets:
        print("テスト対象を指定してください。例: tests/test_hogehoge.py")
        sys.exit(1)

    report_file = "report.json"

    subprocess.run(
        ["pytest", "--json-report", f"--json-report-file={report_file}"] + test_targets,
        check=False
    )

    if not os.path.exists(report_file):
        print("エラーレポートファイルが見つかりません。pytestが失敗した可能性があります。")
        sys.exit(1)

    with open(report_file, encoding="utf-8") as f:
        data = json.load(f)

    print("\n【失敗したテスト一覧】\n")

    failures = [t for t in data["tests"] if t["outcome"] == "failed"]

    if not failures:
        print("🎉 すべてのテストが成功しました！")
    else:
        for i, test in enumerate(failures, 1):
            name = test["nodeid"]
            msg = test.get("call", {}).get("crash", {}).get("message", "")
            if not msg:
                error_summary = "（エラー詳細取得失敗）"
            elif is_full:
                error_summary = msg.strip()
            else:
                error_summary = extract_main_error(msg)
            print(f"{i}. {name}\n   → {error_summary}\n")

if __name__ == "__main__":
    main()
