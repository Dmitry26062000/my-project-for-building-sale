

function valld() {
    let f=1;
    let frst = document.getElementById("password").value;
    let scnd = document.getElementById("confirm_pas").value;
    if(frst.length>=8) {

        if (frst.value === scnd.value) {
            f = 1;
            // frm.reset();
        } else {
            f = 0;
            alert('error')

        }
    }
    else{
        alert('Пароль должен состоять минимум из 8 символов!')
    }
}
function submitForm() {
   // Get the first form with the name
   // Usually the form name is not repeated
   // but duplicate names are possible in HTML
   // Therefore to work around the issue, enforce the correct index
   var frm = document.getElementsByName('form_reg')[0];
   frm.submit(); // Submit the form
   frm.reset();  // Reset all form data
   return false; // Prevent page refresh
}