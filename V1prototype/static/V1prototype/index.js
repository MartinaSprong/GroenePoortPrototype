// (function(){
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

    //create different style
    var image = new ol.style.Circle({
      radius: 6,
      fill: null,
      stroke: new ol.style.Stroke({color: '#D50000', width: 20})
    });

    var styles = {
      'Point': new ol.style.Style({
        image: image
      }),
      'LineString': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'green',
          width: 1
        })
      }),
      'MultiLineString': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'green',
          width: 1
        })
      }),
      'MultiPoint': new ol.style.Style({
        image: image
      }),
      'MultiPolygon': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'yellow',
          width: 1
        }),
        fill: new ol.style.Fill({
          color: 'rgba(255, 255, 0, 0.1)'
        })
      }),
      'Polygon': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'blue',
          lineDash: [4],
          width: 3
        }),
        fill: new ol.style.Fill({
          color: 'rgba(0, 0, 255, 0.1)'
        })
      }),
      'GeometryCollection': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'magenta',
          width: 2
        }),
        fill: new ol.style.Fill({
          color: 'magenta'
        }),
        image: new ol.style.Circle({
          radius: 10,
          fill: null,
          stroke: new ol.style.Stroke({
            color: 'magenta'
          })
        })
      }),
      'Circle': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'red',
          width: 2
        }),
        fill: new ol.style.Fill({
          color: 'rgba(255,0,0,0.2)'
        })
      })
    };

    var styleFunction = function(feature) {
      return styles[feature.getGeometry().getType()];
    };

    //add the feature vector to the layer vector, and apply a style to whole layer
    var vectorLayer = new ol.layer.Vector({
      source: vectorSource,
      // style: iconStyle
      style: styleFunction
    });

    var map = new ol.Map({
      layers: [new ol.layer.Tile({ source: new ol.source.OSM() }), vectorLayer],
      target: document.getElementById('map'),
      view: new ol.View({
        center: ol.proj.fromLonLat([4.209137, 51.914997]),
        // center: [4.209137, 51.914997],
        zoom: 12
      })
    });                                                        
// })();

