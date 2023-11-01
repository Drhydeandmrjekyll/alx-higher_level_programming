/* global $ */

$(document).ready(function () {
  // Define URL to fetch translation
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Send GET request to API
  $.get(apiUrl, function (data) {
    // Select <div> with ID hello using jQuery and update its content
    $('#hello').text(data.hello);
  });
});
