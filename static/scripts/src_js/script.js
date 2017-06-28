// refresh with parameters
function refresh(name, value) {
    var url = window.location.href;
    if (name === undefined || name === null) {
        window.location.href = url;
        window.location.reload(true);
    } else {
        if (url.indexOf('?') > -1) {
            url += '&' + name + '=' + value;
        } else {
            url += '?' + name + '=' + value;
        }
        window.location.href = url;
        window.location.reload(true);
    }
}

gapi.load('auth2', function() {
    auth2 = gapi.auth2.init({
        client_id: '199953711880-pqekr1lmjvu6gb5qg2d99qgn8rs56h1a.apps.googleusercontent.com',
    });
});

function signInCallback(json) {
    authResult = json;
    if (authResult['code']) {
        // Send the code to the server
        jQuery.ajax({
            type: 'POST',
            url: '/login/',
            processData: false,
            data: authResult['code'],
            contentType: 'application/octet-stream; charset=utf-8',
            success: function(result) {
                // Handle or verify the server response if necessary.
                if (result) {
                    refresh()
                } else if (authResult['error']) {
                    alert('There was an error: ' + authResult['error']);
                } else {
                    alert('An error Happened. Please refresh the page and try again.');
                }
            }
        });
    }
}

jQuery(function($) {
    $(document).ready(function() {
        $('#loginButton').click(function() {
            auth2.grantOfflineAccess({
                'redirect_uri': 'postmessage'
            }).then(signInCallback);
        });
    });
});
