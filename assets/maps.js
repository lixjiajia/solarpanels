// Declare initMap globally
console.log("maps.js loaded!");
let map;
let autocomplete;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 51.0447, lng: -114.0719},
    zoom: 8,
  });
  initAutocomplete();
}

function initAutocomplete() {
  const input = document.getElementById("address");
  autocomplete = new google.maps.places.Autocomplete(input);
  autocomplete.bindTo("bounds", map);

  autocomplete.addListener("place_changed", onPlaceChanged);
}

function onPlaceChanged() {
  const place = autocomplete.getPlace();
  if (!place.geometry) {
    return;
  }


  map.setCenter(place.geometry.location);
  map.setZoom(15);


  new google.maps.Marker({
    position: place.geometry.location,
    map: map,
  });


  alert("Address selected: " + place.formatted_address);
}
// Initialize map when the window loads
window.onload = initMap;