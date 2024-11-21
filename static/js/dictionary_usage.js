function selectLetter(letter, element) {
    document.querySelectorAll('#alphabet-list li').forEach(li => li.classList.remove('active'));
    element.classList.add('active');
    document.getElementById('selected-letter').textContent = letter;
    
    fetch(`/terms/${letter}?idioma=${getCurrentLanguage()}`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('terms-container').innerHTML = html;
        });
}

function changeLanguage() {
    var selectedLanguage = document.getElementById('input-language').value;
    window.location.href = '/dictionary-usage?idioma=' + selectedLanguage;
}

function toggleSearch() {
    var searchInput = document.getElementById('searchInput');
    searchInput.classList.toggle('active');
    if (searchInput.classList.contains('active')) {
        searchInput.focus();
    }
}

function performSearch() {
    var searchTerm = document.getElementById('searchInput').value.toLowerCase();
    var terms = document.querySelectorAll('.term');
    terms.forEach(function(term) {
        var termName = term.querySelector('h3').textContent.toLowerCase();
        if (termName.includes(searchTerm)) {
            term.style.display = 'block';
        } else {
            term.style.display = 'none';
        }
    });
}

function getCurrentLanguage() {
    return document.getElementById('input-language').value;
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            performSearch();
        }
    });
});

document.getElementById('homeButton').addEventListener('click', function() {
    window.location.href = '/dictionary-usage?idioma={{ idioma }}';
});