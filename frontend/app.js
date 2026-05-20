async function detectDisease() {
    let file = document.getElementById("imageUpload").files[0];

    let formData = new FormData();
    formData.append("file", file);

    let res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    document.getElementById("result").innerText =
        `Disease: ${data.disease}\nTreatment: ${data.treatment}`;
}