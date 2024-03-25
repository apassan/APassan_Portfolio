export function createColoredIcon(color) {
  return new L.Icon({
    iconUrl: `../static/leaflet/images/marker-icon-2x-${color}.png`,
    shadowUrl: '../static/leaflet/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });
}


// Example usage:
// var greenIcon = createColoredIcon('green');
// var redIcon = createColoredIcon('red');
// var grayIcon = createColoredIcon('gray');
// var yellowIcon = createColoredIcon('yellow');