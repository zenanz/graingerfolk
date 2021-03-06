function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 5,
        minZoom: 3,
        center: {lat: 51.5239, lng: -0.1586},
        panControl: false,
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        overviewMapControl: false,
        rotateControl: true,

        styles: [
            {
                "featureType": "administrative",
                "elementType": "geometry.stroke",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#0096aa"
                    },
                    {
                        "weight": "0.30"
                    },
                    {
                        "saturation": "-75"
                    },
                    {
                        "lightness": "5"
                    },
                    {
                        "gamma": "1"
                    }
                ]
            },
            {
                "featureType": "administrative",
                "elementType": "labels.text.fill",
                "stylers": [
                    {
                        "color": "#0096aa"
                    },
                    {
                        "saturation": "-75"
                    },
                    {
                        "lightness": "5"
                    }
                ]
            },
            {
                "featureType": "administrative",
                "elementType": "labels.text.stroke",
                "stylers": [
                    {
                        "color": "#ffe146"
                    },
                    {
                        "visibility": "on"
                    },
                    {
                        "weight": "6"
                    },
                    {
                        "saturation": "-28"
                    },
                    {
                        "lightness": "0"
                    }
                ]
            },
            {
                "featureType": "administrative",
                "elementType": "labels.icon",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#e6007e"
                    },
                    {
                        "weight": "1"
                    }
                ]
            },
            {
                "featureType": "landscape",
                "elementType": "all",
                "stylers": [
                    {
                        "color": "#ffe146"
                    },
                    {
                        "saturation": "-28"
                    },
                    {
                        "lightness": "0"
                    }
                ]
            },
            {
                "featureType": "poi",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "road",
                "elementType": "all",
                "stylers": [
                    {
                        "color": "#0096aa"
                    },
                    {
                        "visibility": "off"
                    },
                    {
                        "saturation": "-75"
                    },
                    {
                        "lightness": "5"
                    },
                    {
                        "gamma": "1"
                    }
                ]
            },
            {
                "featureType": "road",
                "elementType": "labels.text",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#ffe146"
                    },
                    {
                        "weight": 8
                    },
                    {
                        "saturation": "-28"
                    },
                    {
                        "lightness": "0"
                    }
                ]
            },
            {
                "featureType": "road",
                "elementType": "labels.text.fill",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#0096aa"
                    },
                    {
                        "weight": 8
                    },
                    {
                        "lightness": "5"
                    },
                    {
                        "gamma": "1"
                    },
                    {
                        "saturation": "-75"
                    }
                ]
            },
            {
                "featureType": "road",
                "elementType": "labels.icon",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "transit",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "simplified"
                    },
                    {
                        "color": "#0096aa"
                    },
                    {
                        "saturation": "-75"
                    },
                    {
                        "lightness": "5"
                    },
                    {
                        "gamma": "1"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "geometry.fill",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#0096aa"
                    },
                    {
                        "saturation": "-75"
                    },
                    {
                        "lightness": "5"
                    },
                    {
                        "gamma": "1"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "labels.text",
                "stylers": [
                    {
                        "visibility": "simplified"
                    },
                    {
                        "color": "#ffe146"
                    },
                    {
                        "saturation": "-28"
                    },
                    {
                        "lightness": "0"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "labels.icon",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            }
        ],

        /*[
              {
                "featureType": "administrative.land_parcel",
                "stylers": [
                  {
                    "visibility": "off"
                  }
                ]
              },
              {
                "featureType": "administrative.neighborhood",
                "stylers": [
                  {
                    "visibility": "off"
                  }
                ]
              },
              {
                "featureType": "poi",
                "elementType": "labels.text",
                "stylers": [
                  {
                    "visibility": "off"
                  }
                ]
              },
              {
                "featureType": "road",
                "stylers": [
                  {
                    "visibility": "off"
                  }
                ]
              },
              {
                "featureType": "road",
                "elementType": "labels",
                "stylers": [
                  {
                    "visibility": "off"
                  }
                ]
              },
              {
                "featureType": "water",
                "elementType": "labels.text",
                "stylers": [
                  {
                    "visibility": "off"
                  }
                ]
              }
            ],*/


    });


    // Create an array of alphabetical characters used to label the markers.
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    // Add some markers to the map.
    // Note: The code uses the JavaScript Array.prototype.map() method to
    // create an array of markers based on a given "locations" array.
    // The map() method here has nothing to do with the Google Maps API.
    var markers = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            /*                     label: labels[i % labels.length],
             */                    icon: '/static/image/icons8-music-40-2.png'
        });
    });

    for (var i = 0, len = markers.length; i < len; i++) {
        markers[i].addListener('mouseover', toggleBounce)
    }

    var contentString = '<div id="content">' +
        '<div id="siteNotice">' +
        '</div>' +
        '<h1 id="firstHeading" class="firstHeading">BYE BYE MY DARLING</h1>' +
        '<div id="bodyContent">' +
        '<p><b>BYE BYE MY DARLING</b>, recorded at <b>London, United Kingdom</b>, is a large ' +
        'sandstone rock formation in the southern part of the ' +
        'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) ' +
        'south west of the nearest large town, Alice Springs; 450&#160;km ' +
        '(280&#160;mi) by road. Kata Tjuta and Uluru are the two major ' +
        'features of the Uluru - Kata Tjuta National Park. Uluru is ' +
        'sacred to the Pitjantjatjara and Yankunytjatjara, the ' +
        'Aboriginal people of the area. It has many springs, waterholes, ' +
        'rock caves and ancient paintings. Uluru is listed as a World ' +
        'Heritage Site.</p>' +
        '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
        'https://en.wikipedia.org/w/index.php?title=Uluru</a> ' +
        '(last visited June 22, 2009).</p>' +
        '</div>' +
        '</div>';
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    // test marker
    var byebyemydarling = {lat: 51.420868, lng: -0.130445};
    var marker = new google.maps.Marker({
        position: byebyemydarling,
        map: map,
        title: 'BYE BYE MY DARLING',
        icon: '/static/image/icons8-music-50.png'
    });

    marker.addListener('click', function () {
        infowindow.open(map, marker);
    });
    marker.addListener('mouseover', toggleBounce);
    markers.push(marker)
    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}

/* have to be different location */
var locations = [
    {lat: 51.520868, lng: -0.130445},
    {lat: 53.554242, lng: -0.484769},
    {lat: 53.564242, lng: -0.484769},
    {lat: 51.427235, lng: -0.226082},
    {lat: 51.437235, lng: -0.226082},
    {lat: 57.985996, lng: -3.947143},
    {lat: 57.995996, lng: -3.947143},
    {lat: 54.205632, lng: -2.602048},
    {lat: 54.215632, lng: -2.602048}

];

function toggleBounce() {
    if (this.getAnimation() !== null) {
        this.setAnimation(null);
    } else {
        //marker will bounce one time.
        this.setAnimation(4);
    }
}