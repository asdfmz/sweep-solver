// 手動操作フォームに関する処理（操作種別選択と入力欄の制御）

document.addEventListener("DOMContentLoaded", () => {

  const opTypeButtons = document.querySelectorAll(".op-type-btn");
  const opInput = document.getElementById("operationInput");
  const factorGroup = document.getElementById("factor-group");
  const refRowGroup = document.getElementById("ref-row-group");
  const tInput = document.getElementById("t");
  const fInput = document.getElementById("f");
  const rInput = document.getElementById("r");  

  const config = document.getElementById("validation-config");
  const oneIndexed = config.dataset.oneIndexed === "true";
  const maxIndex = parseInt(config.dataset.maxIndex, 10);

  const offset = typeof oneIndexed !== "undefined" && oneIndexed ? 1 : 0;
  const max = typeof maxIndex !== "undefined" ? maxIndex + offset : 10;
  console.log(offset, max);
  function updateMinMax(input) {
    input.min = offset;
    input.max = max;
  }

  function updateVisibility(op) {
    factorGroup.style.display = (op === "m" || op === "a") ? "block" : "none";
    fInput.required = (op === "m" || op === "a");
    if (!fInput.required) fInput.value = "";

    refRowGroup.style.display = (op === "a" || op === "s") ? "block" : "none";
    rInput.required = (op === "a" || op === "s");
    if (!rInput.required) rInput.value = "";
  }

  opTypeButtons.forEach(btn => {
    btn.addEventListener("click", () => {

      opTypeButtons.forEach(b => b.classList.remove("is-selected"));
      btn.classList.add("is-selected");

      const selectedOp = btn.dataset.op;
      opInput.value = selectedOp;
      console.log(selectedOp);
      updateVisibility(selectedOp);
    });
  });

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

  updateVisibility(opInput.value);
  [tInput, rInput].forEach(updateMinMax);
  [tInput, rInput].forEach(attachValidation);

});
