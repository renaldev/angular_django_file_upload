'use strict';

$('input[id=id_file]').change(function() {
    $('#fileLabel').attr("data-text", $(this).val().replace("C:\\fakepath\\", "") || "Select");
    $('button[type="submit"]').prop('disabled', !($(this).val()));
});