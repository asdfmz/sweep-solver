// 行基本変形の種類切替（定数倍 / 加算 / 交換）

document.addEventListener("DOMContentLoaded", () => {
  
  const opTypeButtons = document.querySelectorAll(".op-type-btn");
  const opInput = document.getElementById("operationInput");
  const factorGroup = document.getElementById("factor-group");
  const refRowGroup = document.getElementById("ref-row-group");

  function updateVisibility(op) {
    factorGroup.style.display = (op === "m" || op === "a") ? "block" : "none";
    factorInput.required = (op === "m" || op === "a");
    if (!factorInput.required) factorInput.value = "";

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

  updateVisibility(opInput.value);

});
