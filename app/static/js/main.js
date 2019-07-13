/*jshint jquery:true, esversion: 6 */
/**
 * Number.prototype.currencyFormat(n)
 *
 * @param integer n: length of decimal
 */
Number.prototype.currencyFormat = function(n) {
    'use strict';

    const x = 3;      // length of whole part
    const s = '.';    // sections delimiter
    const c = ',';    // decimal delimiter
    const re = `\\d(?=(\\d{${x || 3}})+${n > 0 ? '\\D' : '$'})`;
    const num = this.toFixed(Math.max(0, ~~n));

    return (c ? num.replace('.', c) : num).replace(new RegExp(re, 'g'), `$&${s || ','}`);
};

function getCookie(name) {
    'use strict';

    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    'use strict';

    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend(xhr, settings) {
        'use strict';

        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    }
});

$(() => {
    'use strict';
});
