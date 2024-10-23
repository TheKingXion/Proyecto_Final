function selectLetter(letter, element) {
    document.getElementById("selected-letter").textContent = letter;

    let items = document.querySelectorAll(".alphabet-menu ul li");
    items.forEach(item => {
        item.classList.remove("active");
    });

    element.classList.add("active");
}