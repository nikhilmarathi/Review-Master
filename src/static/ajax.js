$(function () {

    $('#search').keyup(function () {

        $.ajax({
            type: "POST",
            url: "/search/",
            data: {
                'search_product_text': $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });

    $(document).on('click', 'li', function () {
        $('#search_product_text').val($(this).text());
        $('#search-results').fadeOut();

    });

});

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data);
    $('#search-results').fadeIn();
}

