function selectLetter(letter, element) {
    // Cambia la letra mostrada en grande
    document.getElementById("selected-letter").textContent = letter;

    // Elimina la clase active de todas las letras
    let items = document.querySelectorAll(".alphabet-menu ul li");
    items.forEach(item => {
        item.classList.remove("active");
    });

    // Agrega la clase active a la letra seleccionada
    element.classList.add("active");
}
