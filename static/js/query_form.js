document.addEventListener("DOMContentLoaded", function () {
  const opInput = document.getElementById("operationInput");
  const factorGroup = document.getElementById("factor-group");
  const refRowGroup = document.getElementById("ref-row-group");
  const factorInput = document.getElementById("f");
  const rInput = document.getElementById("r");
  const tInput = document.getElementById("t");

  const opButtons = document.querySelectorAll(".op-btn");

  const offset = oneIndexed ? 1 : 0;
  const max = maxIndex + offset;

  function updateVisibility(op) {
    factorGroup.style.display = (op === "m" || op === "a") ? "block" : "none";
    factorInput.required = (op === "m" || op === "a");
    if (!factorInput.required) factorInput.value = "";

    refRowGroup.style.display = (op === "a" || op === "s") ? "block" : "none";
    rInput.required = (op === "a" || op === "s");
    if (!rInput.required) rInput.value = "";
  }

  // 操作切り替えボタンのイベント
  opButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const selectedOp = btn.dataset.op;
      opInput.value = selectedOp;

      opButtons.forEach(b => b.classList.remove("selected"));
      btn.classList.add("selected");

      updateVisibility(selectedOp);
    });
  });

  // min/maxとバリデーション
  function updateMinMax(input) {
    input.min = offset;
    input.max = max;
  }

  function attachValidation(input) {
    const msgId = `${input.id}-error`;

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

  // 初期化（hiddenの値から）
  updateVisibility(opInput.value);
  [tInput, rInput].forEach(updateMinMax);
  [tInput, rInput].forEach(attachValidation);
});
