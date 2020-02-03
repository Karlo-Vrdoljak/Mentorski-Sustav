
// Auto metoda za instantno disableanje 'none' za studenta
(()=> {
    document.getElementById('id_role').addEventListener("click", () => {
        formOptions();
    });
    formOptions();
    
})();

function formOptions() {
    let role = document.getElementById('id_role');
    let selected_role = Array.from(role.childNodes).filter(e => {
        if(e.selected == true) {
            return e;
        }
    })[0];
    if (selected_role.textContent == 'student') {
        let status = document.getElementById('id_status');
        Array.from(status.childNodes).map(e => {
            if(e.label == 'none' && e.selected == true) {
                e.selected = false;
                e.nextSibling.nextElementSibling.selected = true;
            }
        });
        Array.from(status.childNodes).filter(e => {
            if(e.label == 'none') {
                return e;
            } else {
                e.disabled = false;
            }
        })[0].disabled = true;
    } else if(selected_role.textContent == 'mentor') {
        let status = document.getElementById('id_status');
        Array.from(status.childNodes).filter(e => {
            if(e.label != 'none') {
                return e;
            } else {
                e.disabled = false;
                e.selected = true;
            }
        }).forEach(e => e.disabled = true);
    }
}