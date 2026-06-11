/* ============================================
   AIFORGE - Enhanced JavaScript Animations
   Premium Improvements v2.0
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // 1. CREATE PARTICLES BACKGROUND
    // ============================================
    function createParticles() {
        const container = document.createElement('div');
        container.className = 'particles-container';
        
        for (let i = 0; i < 9; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            container.appendChild(particle);
        }
        
        document.body.prepend(container);
    }
    
    createParticles();

    // ============================================
    // 2. SCROLL REVEAL ANIMATION
    // ============================================
    function initScrollReveal() {
        const revealElements = document.querySelectorAll('.service-card, .feature-card, .team-card, .blog-card, .portfolio-item, [class*="col-"]');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 100);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
        
        revealElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s cubic-bezier(0.5, 0, 0, 1)';
            observer.observe(el);
        });
    }
    
    initScrollReveal();

    // ============================================
    // 3. CURSOR GLOW EFFECT
    // ============================================
    function initCursorGlow() {
        const glow = document.createElement('div');
        glow.className = 'cursor-glow';
        document.body.appendChild(glow);
        
        let mouseX = 0, mouseY = 0;
        let glowX = 0, glowY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        function animateGlow() {
            glowX += (mouseX - glowX) * 0.1;
            glowY += (mouseY - glowY) * 0.1;
            glow.style.left = glowX + 'px';
            glow.style.top = glowY + 'px';
            requestAnimationFrame(animateGlow);
        }
        
        animateGlow();
    }
    
    // Only on desktop
    if (window.innerWidth > 768) {
        initCursorGlow();
    }

    // ============================================
    // 4. NAVBAR SCROLL EFFECT
    // ============================================
    function initNavbarScroll() {
        const navbar = document.querySelector('.navbar, header, nav');
        if (!navbar) return;
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
    
    initNavbarScroll();

    // ============================================
    // 5. COUNTER ANIMATION
    // ============================================
    function initCounters() {
        const counters = document.querySelectorAll('[data-count], .counter, .stat-number');
        
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.getAttribute('data-count') || counter.textContent.replace(/\D/g, ''));
                    const suffix = counter.textContent.replace(/[\d,]/g, '');
                    
                    if (isNaN(target)) return;
                    
                    let current = 0;
                    const duration = 2000;
                    const step = target / (duration / 16);
                    
                    const updateCounter = () => {
                        current += step;
                        if (current < target) {
                            counter.textContent = Math.floor(current).toLocaleString() + suffix;
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target.toLocaleString() + suffix;
                        }
                    };
                    
                    updateCounter();
                    counterObserver.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(counter => counterObserver.observe(counter));
    }
    
    initCounters();

    // ============================================
    // 6. CARD 3D TILT EFFECT
    // ============================================
    function initTiltEffect() {
        const cards = document.querySelectorAll('.service-card, .feature-card, .team-card');
        
        cards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
            });
        });
    }
    
    if (window.innerWidth > 768) {
        initTiltEffect();
    }

    // ============================================
    // 7. SMOOTH SCROLL
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // ============================================
    // 8. BUTTON RIPPLE EFFECT
    // ============================================
    function initRippleEffect() {
        const buttons = document.querySelectorAll('.btn, .btn-primary, [class*="btn-"]');
        
        buttons.forEach(button => {
            button.addEventListener('click', function(e) {
                const rect = button.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const ripple = document.createElement('span');
                ripple.style.cssText = `
                    position: absolute;
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 50%;
                    transform: scale(0);
                    animation: ripple 0.6s linear;
                    left: ${x}px;
                    top: ${y}px;
                    width: 100px;
                    height: 100px;
                    margin-left: -50px;
                    margin-top: -50px;
                    pointer-events: none;
                `;
                
                button.style.position = 'relative';
                button.style.overflow = 'hidden';
                button.appendChild(ripple);
                
                setTimeout(() => ripple.remove(), 600);
            });
        });
        
        // Add ripple keyframes
        if (!document.querySelector('#ripple-style')) {
            const style = document.createElement('style');
            style.id = 'ripple-style';
            style.textContent = `
                @keyframes ripple {
                    to { transform: scale(4); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    initRippleEffect();

    // ============================================
    // 9. PARALLAX EFFECT
    // ============================================
    function initParallax() {
        const parallaxElements = document.querySelectorAll('[data-parallax]');
        
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            
            parallaxElements.forEach(el => {
                const speed = parseFloat(el.getAttribute('data-parallax')) || 0.5;
                el.style.transform = `translateY(${scrollY * speed}px)`;
            });
        });
    }
    
    initParallax();

    // ============================================
    // 10. LAZY LOAD IMAGES
    // ============================================
    function initLazyLoad() {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    initLazyLoad();

    // ============================================
    // 11. PAGE LOAD ANIMATION
    // ============================================
    document.body.classList.add('page-transition');

    console.log('AIForge Enhancements loaded successfully!');
});
