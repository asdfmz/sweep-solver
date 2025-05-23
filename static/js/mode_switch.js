  // モード切替（手動 / 自動）

document.addEventListener("DOMContentLoaded", () => {
  
  const modeButtons = document.querySelectorAll(".mode-btn");
  const manualSection = document.getElementById("manual-section");
  const autoSection = document.getElementById("auto-section");

  modeButtons.forEach(btn => {
    btn.addEventListener("click", () => {

      modeButtons.forEach(b => b.classList.remove("is-selected"));
      btn.classList.add("is-selected");

      const mode = btn.dataset.mode;
      manualSection.style.display = mode === "manual" ? "block" : "none";
      autoSection.style.display = mode === "auto" ? "block" : "none";
    });
  });
});
