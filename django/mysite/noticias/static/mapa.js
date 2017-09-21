var map;
// Inicializando o mapa do openstreetmap no index
function initmap()
{
  map = new L.Map('map');

  // create the tile layer with correct attribution
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 30});
  map.setView(new L.LatLng(-20.297618, -40.295777),12);
  map.addLayer(osm);
}
function add_point(latitude,longitude,msg)
{
L.marker([latitude,longitude]).addTo(map)
.bindPopup('Mensagem.<br>'+msg+' .')
.openPopup();
}