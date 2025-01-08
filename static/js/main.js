// Announcements Swiper initialization
const announcementSwiper = new Swiper('.swiper-container', {
    slidesPerView: 3,          // Show 3 slides at once
    spaceBetween: 30,
    loop: true,                // Enable continuous loop
    centeredSlides: false,
    autoplay: {                // Add autoplay
        delay: 3000,           // Delay between transitions (in ms)
        disableOnInteraction: false,  // Continue autoplay after user interaction
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        }
    }
}); 