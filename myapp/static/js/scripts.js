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
</script>
