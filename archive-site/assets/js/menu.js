// menu.js

// 読み込み確認用
alert("✅ menu.js が読み込まれました！");

document.addEventListener("DOMContentLoaded", function () {
  const btn = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".sidebar");

  if (btn && sidebar) {
    btn.addEventListener("click", () => {
      alert("👉 ハンバーガーボタンが押されました！");
      sidebar.classList.toggle("open");
    });
  } else {
    alert("⚠️ menu.js: ボタンまたはサイドバーが見つかりません");
  }
});

.sidebar.open {
  right: 0 !important;
}
