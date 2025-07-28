const map = new maplibregl.Map({
  container: 'map',
  style: 'https://api.maptiler.com/maps/01984d3e-b180-7b5c-95d8-d3358c517535/style.json?key=m0E6vRrf1tfFuz2sFKuW',
  center: [-73.97, 40.77],
  zoom: 2
});

map.on('load', () => {
  Promise.all([
    loadIcon('icon2.png'),  // NYC
    loadIcon('icon1.png'),  // Tokyo
    loadIcon('icon3.png'),  // Shanghai
    loadIcon('icon4.png'),  // LA
    loadIcon('icon.png')    // Hover icon
  ]).then(([nycIcon, tokyoIcon, shanghaiIcon, laIcon, hoverIcon]) => {
    map.addImage('nyc-icon', nycIcon);
    map.addImage('tokyo-icon', tokyoIcon);
    map.addImage('shanghai-icon', shanghaiIcon);
    map.addImage('la-icon', laIcon);
    map.addImage('hover-icon', hoverIcon);

    // Add all cities
    addLayerWithPopup('nyc', 'manhattan_toy_stores.geojson', 'nyc-icon', 'nyc-layer');
    addLayerWithPopup('tokyo', 'tokyo_toy_stores.geojson', 'tokyo-icon', 'tokyo-layer');
    addLayerWithPopup('shanghai', 'shanghai_toy_stores.geojson', 'shanghai-icon', 'shanghai-layer');
    addLayerWithPopup('la', 'losangeles_toy_stores.geojson', 'la-icon', 'la-layer');

    // Region navigation buttons
    addRegionButtons();
  });
});

function loadIcon(path) {
  return new Promise((resolve, reject) => {
    map.loadImage(path, (err, image) => {
      if (err) reject(err);
      else resolve(image);
    });
  });
}

function addLayerWithPopup(sourceId, geojsonFile, defaultIcon, layerId) {
  map.addSource(sourceId, {
    type: 'geojson',
    data: geojsonFile
  });

  map.addLayer({
    id: layerId,
    type: 'symbol',
    source: sourceId,
    layout: {
      'icon-image': defaultIcon,
      'icon-size': 0.15,
      'icon-allow-overlap': true
    }
  });

  // Hover effect
  map.on('mouseenter', layerId, () => {
    map.setLayoutProperty(layerId, 'icon-image', 'hover-icon');
  });
  map.on('mouseleave', layerId, () => {
    map.setLayoutProperty(layerId, 'icon-image', defaultIcon);
  });

  map.on('click', layerId, (e) => {
    const props = e.features[0].properties;
    new maplibregl.Popup()
      .setLngLat(e.lngLat)
      .setHTML(`<strong>${props.Name}</strong><br>${props.Address}`)
      .addTo(map);
  });
}

function addRegionButtons() {
  const regions = [
    { name: 'NYC', center: [-73.97, 40.77] },
    { name: 'Tokyo', center: [139.7, 35.67] },
    { name: 'Shanghai', center: [121.47, 31.23] },
    { name: 'Los Angeles', center: [-118.24, 34.05] }
  ];

  const nav = document.createElement('div');
  nav.style.position = 'absolute';
  nav.style.top = '10px';
  nav.style.left = '10px';
  nav.style.background = 'white';
  nav.style.padding = '10px';
  nav.style.borderRadius = '8px';
  nav.style.zIndex = 1;

  regions.forEach(region => {
    const btn = document.createElement('button');
    btn.innerText = region.name;
    btn.style.margin = '5px';
    btn.onclick = () => {
      map.flyTo({ center: region.center, zoom: 13 });
    };
    nav.appendChild(btn);
  });

  document.body.appendChild(nav);
}
