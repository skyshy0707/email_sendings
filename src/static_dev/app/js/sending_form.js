//import { BASE_URL } from '../../common_js/base.js'

console.log("BASE_URL", BASE_URL)
$("#sendings").on("submit", (event) => {
    event.preventDefault()
    //data = $(this).seriallize()
    data = new FormData(event.target)
    console.log("data", data)
    $.ajax({
        type: 'POST',
        data: data,
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        url: `${BASE_URL}`,
        beforeSend: function(xhr){
            //xhr.setRequestHeader('Authorization', 'Token ' + getCookie('access_token'))
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