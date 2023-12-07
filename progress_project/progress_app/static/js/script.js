const menu = document.querySelector(".menu");
const menuItems = document.querySelectorAll(".menuItem");
const hamburger= document.querySelector(".hamburger");
const closeIcon= document.querySelector(".closeIcon");
const menuIcon = document.querySelector(".menuIcon");

function toggleMenu() {
if (menu.classList.contains("showMenu")) {
    menu.classList.remove("showMenu");
    closeIcon.style.display = "none";
    menuIcon.style.display = "block";
} else {
    menu.classList.add("showMenu");
    closeIcon.style.display = "block";
    menuIcon.style.display = "none";
}
}

hamburger.addEventListener("click", toggleMenu);


// slider
$('.carousel').carousel()



// cartttt
jQuery(document).ready(function($) {
    // auto timer
    // setTimeout(function() {
    //     $('#lab-slide-bottom-popup').modal('show');
    // }, 5000); // optional - automatically opens in xxxx milliseconds

    $(document).ready(function() {
        $('.lab-slide-up').find('a').attr('data-toggle', 'modal');
        $('.lab-slide-up').find('a').attr('data-target', '#lab-slide-bottom-popup');
    });
});