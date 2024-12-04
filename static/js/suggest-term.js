document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('suggestTermForm');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const suggestion = Object.fromEntries(formData);
        
        fetch('/api/suggest-term', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(suggestion),
        })
        .then(response => response.json())
        .then(data => {
            alert('¡Sugerencia enviada con éxito!');
            form.reset();
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Error al enviar la sugerencia. Por favor, inténtalo de nuevo.');
        });
    });
});

