function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}

// Here is the event listener for the Contact Info html
function logSubmit(event) {
log.textContent = `Form Submitted! Timestamp: ${event.timeStamp}`;
event.preventDefault();
}

const form = document.getElementById("form");
const log = document.getElementById("log");
form.addEventListener("submit", logSubmit);

element.addEventListener("click", myFunction);
