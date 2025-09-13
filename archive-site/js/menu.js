alert("menu.js が読み込まれました！");

document.addEventListener("DOMContentLoaded", function() {
  const btn = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".sidebar");

  if (btn && sidebar) {
    btn.addEventListener("click", () => {
      alert("ボタンが押されました！"); // ← 動作確認用
      sidebar.classList.toggle("active");
    });
  } else {
    alert("btn または sidebar が見つかりません");
  }
});
