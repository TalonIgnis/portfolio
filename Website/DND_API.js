// This is the darkmode
    function myFunction() {
        var element = document.body;
        element.classList.toggle("dark-mode");
    }

// Function to fetch data from the API based on category
function fetchData(category) {
    const apiUrl = `https://api.open5e.com/${category}/`;

    // Fetch data from the API
    fetch(apiUrl)
        .then(response => response.json())  // Parse the response as JSON
        .then(data => {
            const resultListDiv = document.getElementById('resultList');
            resultListDiv.innerHTML = '';  // Clear previous results

            // Check if results exist and display them
            if (data.results && data.results.length > 0) {
                data.results.forEach(item => {
                    const resultDiv = document.createElement('div');
                    resultDiv.classList.add('result-item');
                    resultDiv.textContent = item.name || item.index;  // Display the name or index for certain items
                    resultListDiv.appendChild(resultDiv);
                });
            } else {
                resultListDiv.innerHTML = '<p>No results found.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            document.getElementById('resultList').innerHTML = '<p>Error loading results.</p>';
        });
}

function Fclasses(){
document.getElementById('fetchClasses') 
    fetchData('classes');
}

function Fspells(){
document.getElementById('fetchSpells')
    fetchData('spells');
}

function Fraces(){
document.getElementById('fetchRaces')
    fetchData('races');
}

function FMonsters(){
document.getElementById('fetchMonsters')
    fetchData('monsters');
}