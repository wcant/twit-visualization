var $ = require('jquery');
var http = require('http');

var dataURL = "http://45.55.151.93:8080/custom_range.json"

$.getJSON(dataURL, function(json) {
    var data = json.results;
    console.log( "success" );
})

  .done(function() {
    console.log( "second success" );
  })
  .fail(function() {
    console.log( "error" );
  })
  .always(function() {
    console.log( "complete" );
  });
 
