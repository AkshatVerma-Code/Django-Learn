const searchInput = document.getElementById('searchInput');
const chaiCards = document.querySelectorAll('.chai-card');
const noResults = document.getElementById('noResults');
const chaiGrid = document.getElementById('chaiGrid');

searchInput.addEventListener('input', function() {
const searchTerm = this.value.toLowerCase();
let visibleCount = 0;

chaiCards.forEach(card => {
    const chaiName = card.getAttribute('data-name').toLowerCase();
    
    if (chaiName.includes(searchTerm)) {
        card.classList.remove('hidden');
        visibleCount++;
    } else {
        card.classList.add('hidden');
    }
});

if (visibleCount === 0) {
    noResults.classList.remove('hidden');
    chaiGrid.style.display = 'none';
} else {
    noResults.classList.add('hidden');
    chaiGrid.style.display = 'grid';
}
});

function orderChai(chaiName) {
alert(`Thank you for ordering ${chaiName}! 🍵\n\nYour order has been placed successfully.\nEnjoy your chai with some code! 💻`);
}