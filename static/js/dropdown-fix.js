document.addEventListener('DOMContentLoaded', function () {

  // Submenu toggle (Mobile)
  document.querySelectorAll('.dropdown-submenu > .dropdown-toggle').forEach(el => {
    el.addEventListener('click', function (e) {

      if (window.innerWidth < 992) {
        e.preventDefault();
        e.stopPropagation();

        const submenu = this.nextElementSibling;

        // close other open submenus
        const parentMenu = this.closest('.dropdown-menu');
        parentMenu.querySelectorAll('.dropdown-menu.show').forEach(open => {
          if (open !== submenu) open.classList.remove('show');
        });

        submenu.classList.toggle('show');
      }

    });
  });

  // Close all submenus when parent dropdown closes
  document.querySelectorAll('.dropdown').forEach(dd => {
    dd.addEventListener('hide.bs.dropdown', function () {
      this.querySelectorAll('.dropdown-menu.show').forEach(sm => {
        sm.classList.remove('show');
      });
    });
  });

});
