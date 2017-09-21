var map;
// Inicializando o mapa do openstreetmap no index
function initmap()
{
  map = new L.Map('map');

  // create the tile layer with correct attribution
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12});
  map.setView(new L.LatLng(-20.297618, -40.295777),10);
  map.addLayer(osm);
}