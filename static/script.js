document.getElementById('patientForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const data = {
        name: document.getElementById('name').value,
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value
    };
    fetch('/patients', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadPatients();
    });
});

function loadPatients() {
    fetch('/patients')
        .then(response => response.json())
        .then(data => {
            const patientList = document.getElementById('patientList');
            patientList.innerHTML = '';
            data.forEach(patient => {
                const div = document.createElement('div');
                div.textContent = `${patient[1]} (${patient[2]} years old, ${patient[3]})`;
                patientList.appendChild(div);
            });
        });
}

loadPatients();
