/**
 * AIForge v2.5 - Main JavaScript
 * Handles Navigation, Mobile Menu, Dropdowns, and UI Effects
 */

document.addEventListener('DOMContentLoaded', function () {
    initNavigation();
    initStickyHeader();
    // initSmoothScroll(); // Desativado para evitar rolagem automática
});

/* ============================================
   NAVIGATION & DROPDOWNS
   ============================================ */
function initNavigation() {
    const mobileToggle = document.querySelector('.navbar-toggler');
    const navMenu = document.getElementById('af-nav-menu');
    const dropdowns = document.querySelectorAll('.af-dropdown');

    // Mobile Toggle
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', function (e) {
            e.stopPropagation();
            navMenu.classList.toggle('active');

            // Icon transition (optional enhancement)
            const icon = this.querySelector('i');
            if (icon) {
                if (navMenu.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-xmark');
                } else {
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            }
        });

        // Close when clicking outside
        document.addEventListener('click', function (e) {
            if (navMenu.classList.contains('active') &&
                !navMenu.contains(e.target) &&
                !mobileToggle.contains(e.target)) {
                navMenu.classList.remove('active');

                const icon = mobileToggle.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-xmark');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // Dropdowns (Mobile & Desktop)
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('.af-link');

        if (link) {
            link.addEventListener('click', function (e) {
                // Determine if we are in mobile view (check CSS breakpoint or width)
                if (window.innerWidth <= 992) {
                    e.preventDefault();
                    e.stopPropagation();

                    // Close other dropdowns
                    dropdowns.forEach(other => {
                        if (other !== dropdown) other.classList.remove('active');
                    });

                    dropdown.classList.toggle('active');
                }
            });
        }
    });
}

/* ============================================
   STICKY HEADER EFFECT
   ============================================ */
function initStickyHeader() {
    const navbar = document.querySelector('.af-navbar');

    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
}

/* ============================================
   SMOOTH SCROLL CHECK
   ============================================ */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (!href || href === '#' || href.length <= 1) return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Close mobile menu if open
                const navMenu = document.getElementById('af-nav-menu');
                if (navMenu && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            }
        });
    });
}
