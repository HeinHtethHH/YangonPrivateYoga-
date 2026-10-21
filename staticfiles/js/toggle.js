document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll('.toggleBtn').forEach(btn => {
    btn.addEventListener('click', function() {
      const targetId = this.getAttribute('data-target');
      const desc = document.getElementById(targetId);

      if (desc.classList.contains('truncate')) {
        desc.classList.remove('truncate');
        this.innerText = "see less";
      } else {
        desc.classList.add('truncate');
        this.innerText = "see more";
      }
    });
  });
});
