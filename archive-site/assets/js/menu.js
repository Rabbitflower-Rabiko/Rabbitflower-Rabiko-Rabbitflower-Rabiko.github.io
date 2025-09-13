document.addEventListener("DOMContentLoaded", function() {
  const btn = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".sidebar");

  if (btn && sidebar) {
    btn.addEventListener("click", () => {
      sidebar.classList.toggle("active");
    });
  }
});
