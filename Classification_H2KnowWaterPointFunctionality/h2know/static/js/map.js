var greenIcon = new L.Icon({
  iconUrl: '../static/leaflet/images/marker-icon-2x-green.png',
  shadowUrl: '../static/leaflet/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

var redIcon = new L.Icon({
  iconUrl: '../static/leaflet/images/marker-icon-2x-red.png',
  shadowUrl: '../static/leaflet/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

var grayIcon = new L.Icon({
  iconUrl: '../static/leaflet/images/marker-icon-2x-gray.png',
  shadowUrl: '../static/leaflet/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

var yellowIcon = new L.Icon({
  iconUrl: '../static/leaflet/images/marker-icon-2x-yellow.png',
  shadowUrl: '../static/leaflet/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

const country_coordinates_mapping = {
  "Nigeria": [9.058739529932314, 7.489347690247056],
  "Sierra Leone": [8.466562640190368, -13.23200798661045],
  "Uganda": [0.3471773440316678, 32.58262298914897],
};

// Get an array of country names (keys) from the object
const countryNames = Object.keys(country_coordinates_mapping);

// Randomly choose one country name from the array
const randomCountry = countryNames[Math.floor(Math.random() * countryNames.length)];

var map = L.map('map').setView(country_coordinates_mapping[randomCountry], 13);
var marker;
var userMarker;
var markers = {};
var oldClosestMarkers = {};
var isSendingLocation = false;

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);


map.dragging.enable();

function handleCountrySelection() {
  var selectedCountry = document.getElementById("country-selector").value;

}

var countryDropdown = document.getElementById('country-selector');
var findWaterPointsBtn = document.getElementById('h2know-button'); // Use getElementById for the ID
var manualInputBtn = document.getElementById('manualInput');
var manualInputBtn2 = document.getElementById('manualInput2');

// Add an event listener to the country dropdown
countryDropdown.addEventListener('change', () => {
  // Check if a country is selected (dropdown value is not empty)
  if (countryDropdown.value !== '') {
    // If a country is selected, display the button
    findWaterPointsBtn.style.display = 'block';
	manualInputBtn.style.display = 'block';
	manualInputBtn2.style.display = 'block';
	
	if (userMarker) {
	  map.removeLayer(userMarker);
	}
	removeExistingMarkers();
	centerOnCountry(countryDropdown.value);
  } 
});
	
function getUserLocation() {
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
		function (position) {
			var latitude = position.coords.latitude;
			var longitude = position.coords.longitude;
			
			// Make an AJAX request to the backend
			var selectedCountry = document.getElementById("country-selector").value;
			
			
			// For testing, NEED TO ERASE after testing
			if (selectedCountry === "Nigeria") {
				latitude = 6.7133819+(Math.floor(Math.random() * 21) - 10)*0.01;
				longitude = 3.3984965+(Math.floor(Math.random() * 21) - 10)*0.01;
			} else if (selectedCountry === "Uganda") {
				latitude = -1.11672037+(Math.floor(Math.random() * 21) - 10)*0.01;
				longitude = 30.20906804+(Math.floor(Math.random() * 21) - 10)*0.01;
			} else if (selectedCountry === "Sierra Leone") {
				latitude = 8.497953611+(Math.floor(Math.random() * 21) - 10)*0.01;
				longitude = -13.28677972+(Math.floor(Math.random() * 21) - 10)*0.01;
			}
			removeExistingMarkers();
			if (userMarker) {
			  map.removeLayer(userMarker);
			}

			userMarker = L.marker([latitude, longitude],  { icon: yellowIcon }).addTo(map);
			map.setView([latitude, longitude], 13);

			
	
			var data = {
				latitude: latitude,
				longitude: longitude,
				country: selectedCountry
			};
			isSendingLocation = true;
			sendLocationToBackend(data);
		},
		function (error) {
			console.log("Error getting user location:", error.message);
		}
    );
  } else {
		console.log("Geolocation is not supported by this browser.");
	}
}


// for manual lat, long user input 
function getManualLocation() {
	removeExistingMarkers();
	var inputText = document.getElementById('manualInput').value;
	var coordinates = inputText.split(',');
	var latitude = parseFloat(coordinates[0].trim());
	var longitude = parseFloat(coordinates[1].trim());

	var selectedCountry = document.getElementById("country-selector").value;
	

	if (userMarker) {
		map.removeLayer(userMarker);
	}

	userMarker = L.marker([latitude, longitude],  { icon: yellowIcon }).addTo(map);
	map.setView([latitude, longitude], 13);

	var data = {
		latitude: latitude,
		longitude: longitude,
		country: selectedCountry
	};
	isSendingLocation = true;
	sendLocationToBackend(data);
}


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function sendLocationToBackend(data){
	$.ajax({
          url: '/process-location/',
          type: 'POST',
		  headers: {
			'X-CSRFToken': getCookie('csrftoken')  // Retrieve the CSRF token from cookies
		  },
          data: data,
          success: function (response) {
            
			// Reset any green marker into blue
			// if (!(Object.keys(oldClosestMarkers).length === 0)){
				// for (let wpdxId in Object.keys(oldClosestMarkers)){
					// map.removeLayer(markers[wpdxId]);
					// oldClosestMarkers[wpdxId].addTo(map);
					// delete oldClosestMarkers[wpdxId];
				// }
				
				
			// }
			
			// Handle the response from the backend
			for (let i = 0; i < response["#wpdx_id"].length; i++) {
				let wpdxId = response["#wpdx_id"][i];
				let latitude = response["#lat_deg"][i];
				let longitude = response["#lon_deg"][i];
				let waterSource = response["#water_source_clean"][i];
				let waterTech = response["#water_tech_clean"][i];
				let distance = response["calculated_distances"][i];
				let waterQuality = response["#subjective_quality_clean"][i];

				let tooltip = `Water Point ID: ${wpdxId} <br>Location: (${latitude}, ${longitude}) <br>Water Source: ${waterSource} <br>Water Tech: ${waterTech} <br> Water Quality: ${waterQuality}<br>Distance: ${distance} KM`;

				// Remove existing marker with the same wpdxId from the map and the markers object
				// if (markers[wpdxId]) {
				// 	console.log("Marker existed, line 249, sendLocationToBackend")
				// 	map.removeLayer(markers[wpdxId]);
				// 	delete markers[wpdxId];
				// }
				
// Add a new marker to the map and the markers object
				if (i < 3){
					marker = L.marker([latitude, longitude], { icon: greenIcon })
					.bindPopup(tooltip)
					.addTo(map);
				}
				else {
					marker = L.marker([latitude, longitude])
					.bindPopup(tooltip)
					.addTo(map);
				}
				
				markers[wpdxId] = marker;

				// // Add a new marker to the map and the markers object
// 				if (let marker = L.marker([latitude, longitude], { icon: greenIcon })
// 				.bindPopup(tooltip)
// 				.addTo(map);

				
				
			}	
			isSendingLocation = false;
			console.log(markers);
          },
          error: function (xhr, status, error) {
            console.log('AJAX request failed:', error);
			isSendingLocation = false;
          }
        });
}

function sendCountryToBackend(data){
  $.ajax({
    url: '/process-country/',
    type: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    },
    data: data, // 'data' should contain the selected country
    success: function (response) {
      // Handle the response from the backend
      $('#country-info').html('Selected Country: ' + response.country + '<br>And just to ensure that we\'re passing it to the backend, this should be all caps: ' + response.country_plus_caps  + '<br>CSV Validation Message: ' +response.message);
    },
    error: function (xhr, status, error) {
      console.log('AJAX request failed:', error);
    }
  });
}


function setupEventListeners() {
  // Add event listener for the country selector
  document.getElementById("country-selector").addEventListener("change", () => {
    // Get the selected country from the dropdown
    var selectedCountry = this.value;
    
    // Check if a country is selected
    if (selectedCountry) {
      // Make an AJAX request to send the selected country to the backend
      var data = {
        country: selectedCountry
      };

      sendCountryToBackend(data);
    }
  });

  // Add click event listener to the map
  map.on('click', function(event) {
    selectedCountry = document.getElementById("country-selector").value;
    
    console.log("Line 113 - map.on('click', function(event)");
    let latitude = event.latlng.lat;
    let longitude = event.latlng.lng;
	removeExistingMarkers();
	if (selectedCountry === ''){
		return;
	}

    if (userMarker) {
      userMarker.setLatLng(event.latlng);
      console.log("if-click userMarker");
    } else {
      userMarker = L.marker(event.latlng, { icon: yellowIcon }).addTo(map); // add yellow color
      console.log("else-click userMarker");
    }

    let data = {
      latitude: latitude,
      longitude: longitude,
      country: selectedCountry
    };
    console.log(data);
	isSendingLocation = true;
    sendLocationToBackend(data);
  });
}

// Call the setupEventListeners function to set up the event listeners once
setupEventListeners();

// Add event listener for the country selector
// document.getElementById("country-selector").addEventListener("change", function () {
  // Get the selected country from the dropdown
  // var selectedCountry = this.value;
	// console.log("Line 295, country-selector");
  // Check if a country is selected
  // if (selectedCountry) {
    // Make an AJAX request to send the selected country to the backend
    // var data = {
      // country: selectedCountry
    // };

    // sendCountryToBackend(data);
  // }
// });

// function processMarkersData(markersData) {
  // for (var i = 0; i < markersData.length; i++) {
    // var markerData = markersData[i];

    // var marker = L.marker([markerData.lat, markerData.lon])
      // .bindPopup(markerData.tooltip);
    // marker.addTo(map);
	// console.log(marker);
    // markers[markerData.wpdxId] = marker; // Add the new marker to the markers object
  // }
// }

function removeExistingMarkers() {
	console.log(markers)
  for (let wpdxId in markers) {
	  console.log(wpdxId)
    map.removeLayer(markers[wpdxId]);
  }
  markers = {};
}

function centerOnCountry(selectedCountry){
	map.setView(country_coordinates_mapping[selectedCountry], 13);
}
