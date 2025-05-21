document.addEventListener("DOMContentLoaded", function () {
  const opSelect = document.getElementById("o");
  const factorGroup = document.getElementById("factor-group");
  const refRowGroup = document.getElementById("ref-row-group");
  const factorInput = document.getElementById("f");
  const rInput = document.getElementById("r");
  const tInput = document.getElementById("t");

  // Pythonテンプレートから注入される変数
  const offset = oneIndexed ? 1 : 0;
  const max = maxIndex + offset;

  // 操作の種類に応じて表示・必須属性を切り替える
  function updateVisibility() {
    const op = opSelect.value;

    // 係数フィールド
    factorGroup.style.display = (op === "m" || op === "a") ? "block" : "none";
    factorInput.required = (op === "m" || op === "a");
    if (!factorInput.required) factorInput.value = "";

    // 参照行フィールド
    refRowGroup.style.display = (op === "a" || op === "s") ? "block" : "none";
    rInput.required = (op === "a" || op === "s");
    if (!rInput.required) rInput.value = "";
  }

  // 入力フィールドの min/max を設定
  function updateMinMax(input) {
    input.min = offset;
    input.max = max;
  }

  // エラーメッセージのリアルタイム表示
  function attachValidation(input) {
    const msgId = `${input.id}-error`;

    // エラーメッセージ要素を追加（なければ）
    if (!document.getElementById(msgId)) {
      const span = document.createElement("span");
      span.id = msgId;
      span.style.color = "red";
      span.style.fontSize = "0.9em";
      span.style.display = "block";
      input.parentElement.appendChild(span);
    }

    input.addEventListener("input", () => {
      const val = parseInt(input.value, 10);
      const msgEl = document.getElementById(msgId);

      if (isNaN(val)) {
        msgEl.textContent = "数値を入力してください。";
      } else if (val < offset || val > max) {
        msgEl.textContent = `${offset} 以上 ${max} 以下の値を入力してください。`;
      } else {
        msgEl.textContent = "";
      }
    });
  }

  // 初期化処理
  opSelect.addEventListener("change", updateVisibility);
  updateVisibility();

  [tInput, rInput].forEach(updateMinMax);
  [tInput, rInput].forEach(attachValidation);
});
