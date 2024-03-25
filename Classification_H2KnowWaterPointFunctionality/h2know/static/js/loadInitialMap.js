import { populateMapWithMarkers } from './countrySelection.js';

export async function initializeMap(country_coordinates_mapping, randomCountry) {
  var map = L.map('map').setView(country_coordinates_mapping[randomCountry], 13);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  // Create a marker cluster group
  var markersCluster = L.markerClusterGroup();

  try {
    // Fetch markers data
    var markersData = await populateMapWithMarkers(randomCountry, false, country_coordinates_mapping);
    processMarkersData(markersData, markersCluster);
  } catch (error) {
    console.error('Error fetching markers:', error);
  }

  // Add the cluster group to the map
  map.addLayer(markersCluster);

  return {map: map, markersCluster: markersCluster};
}

function processMarkersData(markersData, markersCluster) {
  for (var i = 0; i < markersData.length; i++) {
    var markerData = markersData[i];

    var marker = L.marker([markerData.lat, markerData.lon])
      .bindPopup(markerData.tooltip);
    markersCluster.addLayer(marker); // Add the new marker to the markersCluster group
  }
}