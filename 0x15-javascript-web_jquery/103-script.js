$(document).ready(function() {
    $('#btn_translate').click(function() {
        const langCode = $('#language_code').val();
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function(data) {
            $('#hello').html(data.hello);
        });
    });

    $('#language_code').keypress(function(e) {
        if (e.which === 13) {
            $('#btn_translate').click();
        }
    });
});

