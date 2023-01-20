

const url = "http://127.0.0.1:8000/v1/spot/process";
const options = {
    method: "POST",
    headers: {
        Accept: "application/json",
    },
};
const api = "http://127.0.0.1:8000/v1/spot/process/get-sample-data";
const output = document.querySelector(".output");
const results = document.querySelector(".result-container");
results.style.display = "none";
const form = document.querySelector(".form-data");
const input = document.querySelector(".input");
const searchForCountry = async inputtext => {
    try {
        await fetch('http://127.0.0.1:8000/v1/spot/process?text=' + inputtext, {
            method: 'POST',
            headers: {
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded'
            }
        })
            .then(response => response.json())
            .then(data => { console.log(data); 
                output.textContent = data;
                results.style.display = "block";
            })
    } catch (error) {
        results.style.display = "none";
    }
};
// declare a function to handle form submission
const handleSubmit = async e => {
    e.preventDefault();
    searchForCountry(input.value);
    console.log(input.value);
};
form.addEventListener("submit", e => handleSubmit(e));