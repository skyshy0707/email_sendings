
$("#sendings").on("submit", (event) => {
    event.preventDefault()
    data = new FormData(event.target)
    $.ajax({
        type: 'POST',
        data: data,
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        url: `${BASE_URL}`,
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRF-Token', data.get('csrfmiddlewaretoken'))
        },
        success: function(response, status, jqxhr){
            location.reload();
        },
        error: function(jqxhr, status, exception){
            console.log(arguments)
        }
    })
})