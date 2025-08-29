document.getElementById("emailForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;

    const response = await fetch("/validate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    });

    const data = await response.json();
    const resultElement = document.getElementById("result");

    resultElement.innerText = data.result;

    if (data.result === "Valid Email") {
        resultElement.className = "valid";
    } else {
        resultElement.className = "invalid";
    }
});
