django.jQuery(document).ready(function($) {

    $('select#id_addons').select2({
        multiple: true,
        placeholder: 'Select Addons or click + to add new',
        allowClear: true
    } );

});

