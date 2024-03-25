import { getCookie } from './getCookie.js';

export function handleCountrySelection(countryDropdown, findWaterPointsBtn, setView, country_coordinates_mapping, map) {
  countryDropdownEventListener(countryDropdown, findWaterPointsBtn, map);
  
  var selectedCountry = countryDropdown.value;
  populateMapWithMarkers(selectedCountry, setView, country_coordinates_mapping, map);
  
  
}

export function populateMapWithMarkers(selectedCountry, setView, country_coordinates_mapping, map) {
  if (setView) {
    map.setView(country_coordinates_mapping[selectedCountry], 13);
  }

  return new Promise((resolve, reject) => {
    $.ajax({
      url: '/populate-water-points/',
      type: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
      data: {
        country: selectedCountry,
      },
      dataType: 'json',
      success: function(response) {
        var markersData = response.markers;
        resolve(markersData);
      },
      error: function(xhr, status, error) {
        console.log('AJAX request failed:', error);
        reject(error);
      },
    });
  });
}

function countryDropdownEventListener(countryDropdown, findWaterPointsBtn){
	// Add an event listener to the country dropdown
	findWaterPointsBtn = document.getElementById('h2know-button');
	
	countryDropdown.addEventListener('change', () => {
		// When the country dropdown changes, show the location button.
		findWaterPointsBtn.style.display = 'block';
	});
	
	
}

function removeExistingMarkers() {
  for (let wpdxId in markers) {
    map.removeLayer(markers[wpdxId]);
  }
  markers = {};
}