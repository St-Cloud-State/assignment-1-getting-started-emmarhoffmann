// Array to store the application data
const applications = [];

// Function to submit the application and send it to the server
function submitApplication() {
    const name = document.getElementById('name').value;
    const zipcode = document.getElementById('zipcode').value;

    // Create a JSON object with the application data
    const applicationData = {
        name: name,
        zipcode: zipcode
    };

    // Send the application data to the server via POST request
    fetch('/api/submit-application', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(applicationData)
    })
        .then(response => response.json())
        .then(data => {
            // Display a success message or handle errors if needed
            console.log(data.message);

            // Add the new application data to the applications array
            applications.push(applicationData);
            console.log(applications)

            // Refresh the display
            displayApplications();
        })
        .catch(error => {
            console.error('Error submitting the application:', error);
        });


}

// Function to display applications in the list
function displayApplications() {
    const applicationList = document.getElementById('applicationList');
    applicationList.innerHTML = ''; // Clear existing list

    applications.forEach(application => { 
        const applicationElement = document.createElement('div');
        applicationElement.innerHTML = `
            <h2>Added Successfully</h2>
                <p>Name: {application.name} </p>
                <p>Zipcode: {application.zipcode} </p>
        `;
        applicationList.appendChild(applicationElement);
    });
}

