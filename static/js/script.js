
document.addEventListener('DOMContentLoaded', () => {
    const wordInput = document.getElementById('wordInput');
    const generateBtn = document.getElementById('generateBtn');
    const resultsSection = document.getElementById('resultsSection');
    const resultsList = document.getElementById('resultsList');
    const resultCount = document.getElementById('resultCount');
    const totalPossible = document.getElementById('totalPossible');

    const toast = document.getElementById('toast');

    // Generate on Enter key
    wordInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            generateHomoglyphs();
        }
    });

    generateBtn.addEventListener('click', generateHomoglyphs);

    async function generateHomoglyphs() {
        const word = wordInput.value.trim();

        if (!word) return;

        // Reset UI
        resultsSection.classList.add('hidden');
        resultsList.innerHTML = '';

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ word })
            });

            const data = await response.json();

            if (response.ok) {
                renderResults(data);
            } else {
                console.error(data.error);
                // Simple error handling for now
                alert(data.error || "An error occurred");
            }
        } catch (error) {
            console.error('Error:', error);
            alert("Failed to reach server. Is it running?");
        }
    }

    function renderResults(data) {
        resultCount.textContent = `${data.count} variants shown`;
        if (data.total_possible > data.count) {
            totalPossible.textContent = `(Sampled from ${data.total_possible.toLocaleString()} possible)`;
        } else {
            totalPossible.textContent = '';
        }

        resultsList.innerHTML = '';

        data.variants.forEach(variant => {
            const card = document.createElement('div');
            card.className = 'result-card';

            // If punycode is different/available, show it
            const punyText = variant.puny ? `<span class="punycode">${variant.puny}</span>` : '';

            card.innerHTML = `
                <div>
                    <div class="result-text">${variant.text}</div>
                    ${punyText}
                </div>
                <svg class="copy-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            `;

            card.addEventListener('click', () => {
                copyToClipboard(variant.text);
            });

            resultsList.appendChild(card);
        });

        resultsSection.classList.remove('hidden');
    }

    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
            showToast();
        });
    }

    function showToast() {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2000);
    }
});
