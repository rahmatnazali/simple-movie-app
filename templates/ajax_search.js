const user_input = $("#user-input");
const search_icon = $('#search-icon');
const result_div = $('#replaceable-content');
const endpoint = '/api/movie/search';
const delay_by_in_ms = 500;
let scheduled_function = false;

let generate_search_result_html = function (response) {
    if (response.length) {
        let content_html = "";
        response.forEach(e => {
            content_html += `<li><img src="${e.thumbnail}" alt="${e.thumbnail}"/><a href="/${e.slug}">${e.name}</a></li>`;
        });
        return `<ul>${content_html}</ul>`
    } else {
        return "<p>No movies found.</p><br>";
    }
};

let ajax_call = function (endpoint, request_parameters) {
    /*this is a debounced function*/
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            let html = generate_search_result_html(response);

            // fade out the result_div, then:
            result_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                result_div.html(html);
                // fade-in the div with new contents
                result_div.fadeTo('slow', 1);
            })
        })
};

// simple throttle
user_input.on('keyup', function () {
    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    if ($(this).val().trim().length > 0) {
        const request_parameters = {
            search: $(this).val() // value of user_input: the HTML element with ID user-input
        };

        // start animating the search icon with the CSS class
        search_icon.addClass('blink');

        // setTimeout returns the ID of the function to be executed
        scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters);
    } else {
        result_div.html("");
    }
});