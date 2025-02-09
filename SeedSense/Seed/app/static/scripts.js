// JavaScript for additional validation
function validateForm() {
    const numberFields = document.querySelectorAll('input[type="number"]');
    for (let field of numberFields) {
        if (field.value === "" || isNaN(field.value)) {
            alert('Please enter a valid number for ' + field.name);
            field.focus();
            return false;
        }
    }
    return true;
}

// Block non-numeric input
function allowOnlyNumbers(event) {
    const charCode = event.charCode || event.keyCode;
    if ((charCode < 48 || charCode > 57) && charCode !== 46) {
        event.preventDefault(); // Prevent any non-numeric keypress
    }
}
