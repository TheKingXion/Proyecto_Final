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
    particle.style.left = `${Math.random() * 100}vw`;
    particle.style.top = `${Math.random() * 100}vh`;
    particle.textContent = words[currentLanguage][Math.floor(Math.random() * words[currentLanguage].length)];
    document.getElementById('particles').appendChild(particle);

    const duration = 5000 + Math.random() * 5000;
    const animation = particle.animate([
        { transform: 'translate(0, 0)', opacity: 0 },
        { transform: `translate(${Math.random() * 200 - 100}px, ${Math.random() * 200 - 100}px)`, opacity: 1 },
        { transform: `translate(${Math.random() * 200 - 100}px, ${Math.random() * 200 - 100}px)`, opacity: 0 }
    ], {
        duration: duration,
        easing: 'ease-out'
    });

    animation.onfinish = () => {
        particle.remove();
        createParticle();
    };
}

function changeLanguage() {
    currentLanguage = languages[(languages.indexOf(currentLanguage) + 1) % languages.length];
    document.querySelectorAll('.particle').forEach(p => p.remove());
    for (let i = 0; i < 20; i++) {
        createParticle();
    }
}

function initParticles() {
    for (let i = 0; i < 20; i++) {
        createParticle();
    }
    setInterval(changeLanguage, 5000);
}

// Call initParticles when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initParticles);