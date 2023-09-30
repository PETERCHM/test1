<script>
document.getElementById('turnitin-automation-button').addEventListener('click', function() {
    fetch('/home/peterse/Desktop/Eng/software1/myapp/turnitin_automation.py')
        .then(response => response.text())
        .then(code => {
            const blob = new Blob([code], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const script = document.createElement('script');
            script.src = url;
            document.body.appendChild(script);
        })
        .catch(error => console.error('Error loading the Python script:', error))
});

document.getElementById("access-button").addEventListener("click", function() {
    // Make an AJAX request to trigger the Cliffnote script via Django views
    fetch('/run_cliffnote/')  // Replace with the correct Django URL for Cliffnote
        .then(response => response.text())
        .then(data => {
            // Handle the response data if needed
            console.log(data);
        })
        .catch(error => console.error('Error triggering Cliffnote script:', error))
});

</script>
