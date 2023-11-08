$(document).ready(function() {
    $('input#btn_translate').click(function() {
        const langCode = $('input#language_code').val();
        const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=';
        $.get(apiUrl + langCode, function(data) {
            $('div#hello').text(data.hello);
        });
    });
});
