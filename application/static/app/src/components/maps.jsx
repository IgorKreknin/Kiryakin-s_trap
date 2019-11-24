import React from 'react';
import ReactDOM from 'react-dom';
import ymaps from "ymaps";

export class MyMap extends React.Component {
	constructor() {
		const root = document.getElementById("map");
		const maps = await ymaps.load();
		new maps.Map(maps, {
      		center: [-8.369326, 115.166023],
      		zoom: 8
    		})
	}

	render() {
		return(<div></div>);
	}
}

/*
const app = document.getElementById("app");
const button = document.createElement("button");
button.innerText = "Load map";
app.appendChild(button);

button.addEventListener("click", async function() {
  button.innerText = "Loading…";
  button.disabled = true;
  try {
    const maps = await ymaps.load();
    const mapContainer = document.createElement("div");
    mapContainer.style.height = "512px";
    mapContainer.style.width = "512px";
    app.removeChild(button);
    app.appendChild(mapContainer);
    new maps.Map(mapContainer, {
      center: [-8.369326, 115.166023],
      zoom: 8
    });
  } catch (error) {
    console.error("Something went wrong", error);
  }
});
*/