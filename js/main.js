// Initialize AOS (Animate On Scroll)
document.addEventListener('DOMContentLoaded', function() {
    // Performance optimizations for mobile
    const isMobile = window.innerWidth < 768 || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

    // Adjust AOS settings based on device
    AOS.init({
        duration: isMobile ? 600 : 800,
        once: true,
        offset: isMobile ? 50 : 100,
        disable: window.innerWidth < 480
    });

    // Initialize Particles.js
    // Particle configuration
    const particleConfig = {
        "particles": {
            "number": {
                "value": isMobile ? 40 : 80,
                "density": {
                    "enable": true,
                    "value_area": 800
                }
            },
            "color": {
                "value": "#64FFDA"
            },
            "shape": {
                "type": "circle",
                "stroke": {
                    "width": 0,
                    "color": "#000000"
                },
                "polygon": {
                    "nb_sides": 5
                }
            },
            "opacity": {
                "value": 0.5,
                "random": false,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 3,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 40,
                    "size_min": 0.1,
                    "sync": false
                }
            },
            "line_linked": {
                "enable": true,
                "distance": 150,
                "color": "#64FFDA",
                "opacity": 0.4,
                "width": 1
            },
            "move": {
                "enable": true,
                "speed": 2,
                "direction": "none",
                "random": false,
                "straight": false,
                "out_mode": "out",
                "bounce": false,
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": {
                "onhover": {
                    "enable": true,
                    "mode": "grab"
                },
                "onclick": {
                    "enable": true,
                    "mode": "push"
                },
                "resize": true
            },
            "modes": {
                "grab": {
                    "distance": 140,
                    "line_linked": {
                        "opacity": 1
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 3
                },
                "repulse": {
                    "distance": 200,
                    "duration": 0.4
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2
                }
            }
        },
        "retina_detect": true
    };

    // Initialize particles for each section
    const sections = ['home', 'about', 'projects', 'resume', 'contact'];
    
    // Only initialize particles if device can handle it
    if (!isMobile || window.innerWidth > 480) {
        sections.forEach(section => {
            const elementId = `particles-js-${section}`;
            if (document.getElementById(elementId)) {
                // Create a slightly modified config for each section
                const sectionConfig = JSON.parse(JSON.stringify(particleConfig));
                
                // Modify config for different sections
                if (section !== 'home') {
                    // Make non-home sections have fewer particles
                    sectionConfig.particles.number.value = isMobile ? 30 : 50;
                    // Make the particles move slower in non-home sections
                    sectionConfig.particles.move.speed = 1.5;
                }
                
                // Initialize particles.js for this section
                particlesJS(elementId, sectionConfig);
            }
        });
    } else {
        // For very low-end devices, only initialize particles in home section with minimal config
        const elementId = 'particles-js-home';
        if (document.getElementById(elementId)) {
            const minimalConfig = JSON.parse(JSON.stringify(particleConfig));
            minimalConfig.particles.number.value = 20;
            minimalConfig.particles.move.speed = 1;
            minimalConfig.particles.line_linked.enable = false;
            
            particlesJS(elementId, minimalConfig);
        }
    }

    // Add resize handler to adjust particles count on window resize
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            // Only reload particles if width changed significantly
            const newIsMobile = window.innerWidth < 768;
            if ((isMobile && !newIsMobile) || (!isMobile && newIsMobile)) {
                location.reload();
            }
        }, 500);
    });

    // Ensure page starts at top on refresh
    window.scrollTo(0, 0);
    history.scrollRestoration = "manual";

    // Initialize Typing Animation with performance adjustments
    initTypingAnimation();
});

// Ensure page starts at top on refresh
window.onload = function() {
    window.scrollTo(0, 0);
    history.scrollRestoration = "manual";
};

// Typing Animation
function initTypingAnimation() {
    const typingText = document.querySelector('.typing-text');
    if (!typingText) return;
    
    const texts = ["I'm Tanmay Patel", "I'm Software Engineer"];
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100; // Base typing speed
    
    function typeWriter() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            // Deleting text
            typingText.innerHTML = currentText.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 50; // Faster when deleting
        } else {
            // Typing text
            typingText.innerHTML = currentText.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 100; // Normal speed when typing
        }
        
        // If we've finished typing the current text
        if (!isDeleting && charIndex === currentText.length) {
            // Pause at the end of typing
            isDeleting = true;
            typingSpeed = 1500; // Wait before starting to delete
        } 
        // If we've finished deleting the current text
        else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            // Move to next text
            textIndex = (textIndex + 1) % texts.length;
            // Pause before typing next text
            typingSpeed = 500;
        }
        
        setTimeout(typeWriter, typingSpeed);
    }
    
    // Start the typing animation with a slight delay
    setTimeout(typeWriter, 1000);
}

// Mobile Menu Toggle with improved performance
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');
let isMenuOpen = false;

if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', function() {
        isMenuOpen = !isMenuOpen;
        mobileMenu.classList.toggle('hidden');
        mobileMenu.classList.toggle('mobile-menu-active');
        
        // Update icon
        mobileMenuButton.innerHTML = isMenuOpen ? 
            '<i class="fas fa-times text-2xl"></i>' : 
            '<i class="fas fa-bars text-2xl"></i>';
    });
}

// Close mobile menu when clicking on a link
document.querySelectorAll('#mobile-menu a').forEach(link => {
    link.addEventListener('click', () => {
        if (mobileMenu) {
            mobileMenu.classList.add('hidden');
            mobileMenu.classList.remove('mobile-menu-active');
            
            if (mobileMenuButton) {
                mobileMenuButton.innerHTML = '<i class="fas fa-bars text-2xl"></i>';
                isMenuOpen = false;
            }
        }
    });
});

// Smooth Scroll with performance optimizations
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const navHeight = document.querySelector('nav').offsetHeight;
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;
            
            // Use native smooth scrolling if supported
            if ('scrollBehavior' in document.documentElement.style) {
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            } else {
                // Fallback for browsers that don't support smooth scrolling
                window.scrollTo(0, targetPosition);
            }
        }
    });
});

// Active Navigation Highlight with throttling for performance
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.hidden.md\\:flex a');

// Debounce function to limit how often a function can run
function debounce(func, wait) {
    let timeout;
    return function() {
        const context = this, args = arguments;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), wait);
    };
}

// Use debounced scroll event listener to improve performance
const debouncedScroll = debounce(() => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (pageYOffset >= sectionTop - 150) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('text-aqua');
        link.classList.add('text-light-blue');
        
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.remove('text-light-blue');
            link.classList.add('text-aqua');
        }
    });
}, 100);

window.addEventListener('scroll', debouncedScroll);

// Resume Button Animations
const resumeButtons = document.querySelectorAll('.resume-btn');

resumeButtons.forEach(button => {
    button.addEventListener('mouseenter', () => {
        button.style.transform = 'translateY(-5px)';
    });

    button.addEventListener('mouseleave', () => {
        button.style.transform = 'translateY(0)';
    });

    button.addEventListener('click', (event) => {
        // Add a ripple effect when clicked
        const ripple = document.createElement('div');
        ripple.classList.add('ripple');
        
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height) * 2;
        
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${event.clientX - rect.left - size / 2}px`;
        ripple.style.top = `${event.clientY - rect.top - size / 2}px`;
        
        button.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Form Submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData);
        
        // Here you would typically send the data to a server
        console.log('Form submitted:', data);
        
        // Clear form
        contactForm.reset();
        
        // Show success message (you can customize this)
        alert('Thank you for your message! I will get back to you soon.');
    });
}

// Add project card hover effect
document.querySelectorAll('.bg-navy-light').forEach(card => {
    card.classList.add('project-card');
});

// Add hover translate effect to social links
document.querySelectorAll('.fab, .fas').forEach(icon => {
    icon.parentElement.classList.add('hover-translate');
}); 