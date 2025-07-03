document.addEventListener('click', function(event) {
    var target = event.target;
    var navbarCollapse = document.querySelector('.navbar-collapse');

    if (!navbarCollapse.contains(target)) {
        navbarCollapse.classList.remove('show');
    }
});
