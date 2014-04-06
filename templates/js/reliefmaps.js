var left, right;

function initialize() {

  // VILLAMOR
  var left = {
    zoom: 14,
    center: new google.maps.LatLng(14.518023, 121.021934),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  // ABSCBN
  var right = {
    zoom: 14,
    center: new google.maps.LatLng(14.639493, 121.034722),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  left = new google.maps.Map(document.getElementById("relief-left-map"),
                                left);
  right = new google.maps.Map(document.getElementById("relief-right-map"),
                                right);
}

google.maps.event.addDomListener(window, 'load', initialize);

