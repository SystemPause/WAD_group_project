$(".custom-select").select2();

$("#{{ form.speaks.id_for_label }}").select2({
    maximumSelectionLength: 5
});
$("#{{ form.practices.id_for_label }}").select2({
    maximumSelectionLength: 5
});