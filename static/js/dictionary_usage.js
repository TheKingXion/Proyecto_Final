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

function updateTextContent(language) {
    const textContent = {
        es: {
            'title': 'Forma de Utilizar el Diccionario - Diccionario del 3MF',
            'header1': '¿Como se usa el Diccionario?',
            'header2': 'Tan simple como dar click en la letra de la cual quieres ver los terminos y te dejara ver los terminos traducidos',
            'header3': '¿Como se usa el "Buscar"?',
            'header4': 'Vas a la letra y cuando estes en la letra que tiene el termino, preciona el boton de buscar y busca ejemplo "If" y das ENTER',
        },
        en: {
            'title': 'How to Use the Dictionary - 3MF Dictionary',
            'header1': 'How to use the Dictionary?',
            'header2': 'Just click on the letter from which you want to see the terms, and you will see the translated terms',
            'header3': 'How to use the "Search"?',
            'header4': 'Go to the letter, and when you are at the letter with the term, click the search button and search for "If" and press ENTER',
        },
        it: {
            'title': 'Come usare il dizionario - Dizionario 3MF',
            'header1': 'Come usare il dizionario?',
            'header2': 'Basta cliccare sulla lettera da cui vuoi vedere i termini e vedrai i termini tradotti',
            'header3': 'Come usare la "Ricerca"?',
            'header4': 'Vai alla lettera, e quando sei sulla lettera con il termine, premi il pulsante di ricerca e cerca "If" e premi INVIO',
        },
        pt: {
            'title': 'Como usar o dicionário - Dicionário 3MF',
            'header1': 'Como usar o dicionário?',
            'header2': 'Basta clicar na letra da qual você quer ver os termos e verá os termos traduzidos',
            'header3': 'Como usar a "Busca"?',
            'header4': 'Vá para a letra e, quando estiver na letra com o termo, clique no botão de busca e pesquise por "If" e pressione ENTER',
        }
    };

    // Actualizar los textos de la página
    document.title = textContent[language].title;
    document.getElementById('header1').textContent = textContent[language].header1;
    document.getElementById('header2').textContent = textContent[language].header2;
    document.getElementById('header3').textContent = textContent[language].header3;
    document.getElementById('header4').textContent = textContent[language].header4;
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            performSearch();
        }
    });
});

document.getElementById('homeButton').addEventListener('click', function() {
    window.location.href = '/dictionary-usage';
});