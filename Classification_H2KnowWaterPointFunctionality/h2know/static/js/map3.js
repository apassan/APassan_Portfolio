import { createColoredIcon } from './icons.js';
import { initializeMap } from './loadInitialMap.js';
import { getCookie } from './getCookie.js';
import { handleCountrySelection } from './countrySelection.js';

const country_coordinates_mapping = {
  "Nigeria": [9.058739529932314, 7.489347690247056],
  "Sierra Leone": [8.466562640190368, -13.23200798661045],
  "Uganda": [0.3471773440316678, 32.58262298914897]
};

const countryNames = Object.keys(country_coordinates_mapping);

var randomCountry = countryNames[Math.floor(Math.random() * countryNames.length)];

var mapAndClusters = initializeMap(country_coordinates_mapping, randomCountry);

var map = mapAndClusters.map;
var markersCluster = mapAndClusters.markersCluster;


// Get the country dropdown and button elements
const countryDropdown = document.getElementById('country-selector');
const findWaterPointsBtn = document.getElementById('h2know-button');

// Add an event listener to the dropdown change event
countryDropdown.addEventListener('change', () => {
  // Call the handleCountrySelection function and pass the countryDropdown and findWaterPointsBtn elements
  handleCountrySelection(countryDropdown, findWaterPointsBtn, true, country_coordinates_mapping, map);
});

// Call the handleCountrySelection function initially to set the button state based on the initial selection
handleCountrySelection(countryDropdown, findWaterPointsBtn, false, country_coordinates_mapping, map);