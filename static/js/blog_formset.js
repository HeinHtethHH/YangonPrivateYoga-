document.addEventListener('DOMContentLoaded', function() {

    const addButton = document.getElementById('add-form');
    const totalFormsInput = document.querySelector('input[name$="-TOTAL_FORMS"]');
    const emptyForm = document.getElementById('empty-form');

    if (!addButton || !totalFormsInput || !emptyForm) {
        console.log("Formset elements missing");
        return;
    }

    addButton.addEventListener('click', function() {

        let currentCount = parseInt(totalFormsInput.value);

        let newFormHtml = emptyForm.innerHTML.replace(/__prefix__/g, currentCount);

        let div = document.createElement('div');
        div.classList.add('subform');
        div.innerHTML = newFormHtml;

        // ✅ Button မတိုင်ခင် ထည့်မယ်
        addButton.parentNode.insertBefore(div, addButton);

        totalFormsInput.value = currentCount + 1;
    });

});