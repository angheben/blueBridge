document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', function() {
        const aboutSection = document.getElementById('about');
        const position = aboutSection.getBoundingClientRect();

        // Show the "about" section when it reaches a certain point on the page
        if (position.top < window.innerHeight * 0.75) {
            aboutSection.style.opacity = 1; // Make the section visible
            aboutSection.style.transform = 'translateY(0)'; // Animate the section
        } else {
            aboutSection.style.opacity = 0; // Hide the section if it's not within the visible range
            aboutSection.style.transform = 'translateY(20px)'; // Animate the section
        }
    });
});