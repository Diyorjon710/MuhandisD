
document.addEventListener("DOMContentLoaded", function() {
// Tilni tanlash uchun elementlarni tanlash
var languageSwitchers = document.querySelectorAll('.dropdown-item.liu');

languageSwitchers.forEach(function(elem) {
    elem.addEventListener('click', function(event) {
    event.preventDefault(); // Sahifa o'tishini oldini olish
    var selectedLanguage = this.getAttribute('data-lang'); // data-lang attributidan tilni olish
    localStorage.setItem('selectedLanguage', selectedLanguage); // localStorage'da saqlaymiz

    // Tanlangan tilga mos rasm va matnni yangilaymiz
    var navLink = document.querySelector('.nav-link.dropdown-toggle');
    navLink.innerHTML = `<img src="img/${selectedLanguage.toLowerCase()}_flag.jpg" class="img m-1" alt="${selectedLanguage}">${selectedLanguage} <span class="caret"></span>`;

    console.log("Tanlangan til: ", selectedLanguage);
    // location.reload(); // Agar kerak bo'lsa, sahifani qayta yuklash
    // Bu yerda tanlangan tilga mos kontentni yuklash uchun kod qo'shishingiz kerak
    });
});

// Sayt yuklanganda, localStorage'dan tanlangan tilni qo'llash
var selectedLanguage = localStorage.getItem('selectedLanguage');
if (selectedLanguage) {
    var navLink = document.querySelector('.nav-link.dropdown-toggle');
    navLink.innerHTML = `<img src="img/${selectedLanguage.toLowerCase()}_flag.jpg" class="img m-1" alt="${selectedLanguage}">${selectedLanguage} <span class="caret"></span>`;
}
});

