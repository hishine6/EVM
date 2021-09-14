var map;
const map_center = {lat: 37.54989794096065, lng: 126.94100229832952};

function initMap(){
    var container = document.getElementById('map');
    var options = {
        center: new kakao.maps.LatLng(map_center.lat,map_center.lng),
        level: 2

    };
    map = new kakao.maps.Map(container, options);
}