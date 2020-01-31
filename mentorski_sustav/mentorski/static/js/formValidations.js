
// Auto metoda za instantno disableanje 'none' za studenta
(()=> {
    let role = document.getElementById('id_role');
    let selected_role = Array.from(role.childNodes).filter(e => {
        if(e.selected == true) {
            return e;
        }
    })[0];
    if (selected_role.textContent == 'student') {
        let status = document.getElementById('id_status');
        Array.from(status.childNodes).filter(e => {
            if(e.label == 'none') {
                return e;
            }
        })[0].disabled = true;
    }
    
})();