console.log("menu.js が読み込まれました！");

document.addEventListener("DOMContentLoaded", function() {
  const btn = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".sidebar");

  if (btn && sidebar) {
    btn.addEventListener("click", () => {
      console.log("ボタンが押されました！");
      sidebar.classList.toggle("open");
    });
  } else {
    console.log("btn または sidebar が見つかりません");
  }
});
