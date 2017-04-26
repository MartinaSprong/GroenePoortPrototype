(function(){
    var vectorSource = new ol.source.Vector({
      //create empty vector
    });
    
    //create single marker and add to source vector
    var iconFeatureSingleOne = new ol.Feature({
      geometry: new ol.geom.Point(ol.proj.transform([4.209137, 51.914997], 'EPSG:4326',     
      'EPSG:3857')),
      name: 'Null Island',
      population: 4000,
      rainfall: 500
    });
    vectorSource.addFeature(iconFeatureSingleOne);

    //create single marker and add to source vector
    var iconFeatureSingleTwo = new ol.Feature({
      geometry: new ol.geom.Point(ol.proj.transform([4.178667, 51.944870], 'EPSG:4326',     
      'EPSG:3857')),
      name: 'Null Island',
      population: 4000,
      rainfall: 500
    });
    vectorSource.addFeature(iconFeatureSingleTwo);

    //create a bunch of icons and add to source vector
    for (var i=0;i<50;i++){
 
        var iconFeature = new ol.Feature({
          geometry: new  
            ol.geom.Point(ol.proj.transform([Math.random()*360-180, Math.random()*180-90], 'EPSG:4326',   'EPSG:3857')),
        name: 'Null Island ' + i,
        population: 4000,
        rainfall: 500
        });
        vectorSource.addFeature(iconFeature);
    }

    //create the style
    var iconStyle = new ol.style.Style({
      image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
        anchor: [0.5, 46],
        anchorXUnits: 'fraction',
        anchorYUnits: 'pixels',
        opacity: 0.75,
        src: 'http://openlayers.org/en/v3.9.0/examples/data/icon.png'
      }))
    });

    //add the feature vector to the layer vector, and apply a style to whole layer
    var vectorLayer = new ol.layer.Vector({
      source: vectorSource,
      style: iconStyle
    });

    var map = new ol.Map({
      layers: [new ol.layer.Tile({ source: new ol.source.OSM() }), vectorLayer],
      target: document.getElementById('map'),
      view: new ol.View({
        center: ol.proj.fromLonLat([4.209137, 51.914997]),
        zoom: 12
      })
    });
    vectorSource.events.register('mousedown', vectorSource, function(evt){
      this.pop.show();
      OpenLayers.Event.stop(evt); 
      });                                                              
})();

