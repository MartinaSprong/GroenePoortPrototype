// -- Display information on singleclick --

// Create a popup overlay which will be used to display feature info
var popup = new ol.Overlay.Popup();
map.addOverlay(popup);

// Add an event handler for the map "singleclick" event
map.on('singleclick', function(evt) {

    // Hide existing popup and reset it's offset
    popup.hide();
    popup.setOffset([0, 0]);

    // Attempt to find a feature in one of the visible vector layers
    var feature = map.forEachFeatureAtPixel(evt.pixel, function(feature, layer) {
        return feature;
    });

    if (feature) {
        var coord = feature.getGeometry().getCoordinates();
        // var props = feature.getProperties();
        var info = "<p>Lorem Ipsum</p>";
            // info += "<p>Status:</p>";
            // info += "<p><a href='" + props.caseurl + "'>To graph</a></p>";
            info += "<p><a href='graph'>To graph</a></p>";
        // Offset the popup so it points at the middle of the marker not the tip
        popup.setOffset([0, -22]);
        popup.show(coord, info);
    }
});