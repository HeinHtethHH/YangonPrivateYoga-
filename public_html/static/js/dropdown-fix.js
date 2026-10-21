// document.addEventListener('DOMContentLoaded', function() {
//     // Mobile မှာ Submenu link တွေကို နှိပ်ရင် ပွင့်စေဖို့
//     var submenus = document.querySelectorAll('.dropdown-submenu > .dropdown-item');
    
//     submenus.forEach(function(element) {
//         element.addEventListener('click', function (e) {
//             // Screen size က mobile ဖြစ်နေရင် (992px အောက်)
//             if (window.innerWidth < 992) {
//                 e.preventDefault();
//                 e.stopPropagation();
                
//                 let nextEl = this.nextElementSibling;
//                 if (nextEl && nextEl.classList.contains('dropdown-menu')) {
//                     // တခြားပွင့်နေတဲ့ sibling submenu တွေကို ပိတ်ပါ
//                     let parent = this.parentElement.parentElement;
//                     parent.querySelectorAll('.dropdown-menu.show').forEach(function(openMenu) {
//                         if (openMenu !== nextEl) openMenu.classList.remove('show');
//                     });
                    
//                     // လက်ရှိ submenu ကို toggle လုပ်ပါ
//                     nextEl.classList.toggle('show');
//                 }
//             }
//         });
//     });
// });

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
