/*
window.addEventListener('scroll', function() {
    const aboutSection = document.getElementById('about');
    const position = aboutSection.getBoundingClientRect();

    // Show the "about" section when it reaches a certain point on the page
    if (position.top < window.innerHeight * 0.75) {
        aboutSection.style.display = 'block';
    } else {
        aboutSection.style.display = 'none'; // Hide the section if it's not within the visible range
    }
});
*/

// script.js

// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});