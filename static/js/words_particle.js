const words = {
    es: ['Programación', 'Código', 'Desarrollo', 'Web', 'Aplicación', 'Software', 'Tecnología', 'Innovación'],
    en: ['Programming', 'Code', 'Development', 'Web', 'Application', 'Software', 'Technology', 'Innovation'],
    it: ['Programmazione', 'Codice', 'Sviluppo', 'Web', 'Applicazione', 'Software', 'Tecnologia', 'Innovazione'],
    pt: ['Programação', 'Código', 'Desenvolvimento', 'Web', 'Aplicação', 'Software', 'Tecnologia', 'Inovação']
};

const languages = ['es', 'en', 'it', 'pt'];
let currentLanguage = 'es';

function createParticle() {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    const startX = Math.random() * 100;
    const startY = Math.random() * 100;
    particle.style.left = `${startX}vw`;
    particle.style.top = `${startY}vh`;
    particle.textContent = words[currentLanguage][Math.floor(Math.random() * words[currentLanguage].length)];
    document.getElementById('particles').appendChild(particle);
    animateParticle(particle, startX, startY);
}

function animateParticle(particle, startX, startY) {
    const endX = Math.random() * 100;
    const endY = Math.random() * 100;
    particle.animate([
        { transform: `translate(0, 0)`, opacity: 0.5 },
        { transform: `translate(${endX - startX}vw, ${endY - startY}vh)`, opacity: 1 },
        { transform: `translate(0, 0)`, opacity: 0.5 }
    ], {
        duration: 10000 + Math.random() * 5000,
        iterations: Infinity,
        direction: 'alternate',
        easing: 'ease-in-out'
    });
}

function changeLanguage() {
    currentLanguage = languages[(languages.indexOf(currentLanguage) + 1) % languages.length];
    document.querySelectorAll('.particle').forEach(particle => {
        particle.textContent = words[currentLanguage][Math.floor(Math.random() * words[currentLanguage].length)];
    });
}

function initParticles() {
    for (let i = 0; i < 20; i++) {
        createParticle();
    }
    setInterval(changeLanguage, 50000);
}

// Call initParticles immediately
initParticles();