django.jQuery(document).ready(function($) {

    $('select#id_addons').select2({
        multiple: true,
        placeholder: 'Select Addons or click + to add new',
        allowClear: true
    } );

    $('select#id_addons').on('select2:open', function () {
    // get values of selected option
    var values = $(this).val();
    // get the pop up selection
    var pop_up_selection = $('.select2-results__options');

    if (values != null ) {
      // hide the selected values
       pop_up_selection.find("li[aria-selected=true]").hide();

    } else {
      // show all the selection values
      pop_up_selection.find("li[aria-selected=true]").show();
    }

  });

});

