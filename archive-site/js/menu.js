document.addEventListener("DOMContentLoaded", function () {
  const btn = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".sidebar");

  if (btn && sidebar) {
    // ボタンで開閉
    btn.addEventListener("click", () => {
      sidebar.classList.toggle("open");
    });

    // サイドバーをクリックしたら閉じる
    sidebar.addEventListener("click", () => {
      sidebar.classList.remove("open");
    });
  }
});
