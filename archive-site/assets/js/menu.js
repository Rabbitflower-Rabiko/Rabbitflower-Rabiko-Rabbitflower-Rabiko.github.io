document.addEventListener("DOMContentLoaded", function() {
  const btn = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".sidebar");

  btn.addEventListener("click", () => {
    sidebar.classList.toggle("active");
  });
});
