document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('predictBtn').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = {
            pregnancies: document.getElementById('pregnancies').value,
            glucose: document.getElementById('glucose').value,
            blood_pressure: document.getElementById('blood_pressure').value,
            skin_thickness: document.getElementById('skin_thickness').value,
            insulin: document.getElementById('insulin').value,
            bmi: document.getElementById('bmi').value,
            diabetes_pedigree_function: document.getElementById('diabetes_pedigree_function').value,
            age: document.getElementById('age').value
        };

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Prediction request failed');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                document.getElementById('result').innerText = 'Error: ' + data.error;
            } else {
                document.getElementById('result').innerText = data.prediction;
            }
        })
        .catch(error => {
            document.getElementById('result').innerText = 'An error occurred. Please try again.';
            console.error('Error:', error);
        });
    });
});
