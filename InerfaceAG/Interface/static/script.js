document.getElementById("travel-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const numCities = document.getElementById("numCities").value;
    const distances = document.getElementById("distances").value;

    const response = await fetch("/solve", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ numCities, distances }),
    });

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = ""; // Limpar resultados anteriores

    const data = await response.json();
    if (data.error) {
        resultDiv.innerHTML = `<p style="color: red;">Erro: ${data.error}</p>`;
    } else {
        resultDiv.innerHTML = `<h3>Resultado:</h3><p>${JSON.stringify(data.result)}</p>`;
    }
});
