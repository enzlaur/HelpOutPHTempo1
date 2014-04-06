        var map;
        function initialize() {
            var mapOptions = {
                zoom: 8
            };
            map = new google.maps.Map(document.getElementById('map-canvas'),
                mapOptions);

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    var pos = new google.maps.LatLng(position.coords.latitude,
                                                     position.coords.longitude);

                    var infowindow = new google.maps.InfoWindow({
                        content: '<div id="infoWindowLabel">Location found using HTML5.Location found using HTML5.Location found using HTML5.Location found using HTML5.Location found using HTML5.Location found using HTML5.Location found using HTML5.</div>'
                    });

                    var marker = new google.maps.Circle({
                        center: pos,
                        position: pos,
                        map: map,
                        radius: 5000,
                        strokeWeight: 0,
                        fillColor: '#FF0000',
                        fillOpacity: 0.35
                    });
                    var toClose = true;
                    google.maps.event.addListener(marker, 'mouseover', function () {
                        infowindow.open(map, marker);
                        toClose = true;
                    });

                    google.maps.event.addListener(marker, 'mouseout', function () {
                        if(toClose)
                            infowindow.close();
                    });

                    google.maps.event.addListener(marker, 'click', function () {
                        toClose = false;
                    });


                    map.setCenter(pos);
                }, function () {
                    handleNoGeolocation(true);
                });
            } else {
                // Browser doesn't support Geolocation
                handleNoGeolocation(false);
            }
        }

        function handleNoGeolocation(errorFlag) {
            if (errorFlag) {
                var content = 'Error: The Geolocation service failed.';
            } else {
                var content = 'Error: Your browser doesn\'t support geolocation.';
            }

            var options = {
                map: map,
                position: new google.maps.LatLng(60, 105),
                content: content
            };

            var infowindow = new google.maps.InfoWindow(options);
            map.setCenter(options.position);
        }

        google.maps.event.addDomListener(window, 'load', initialize);