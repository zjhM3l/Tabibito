<template>
  <div class="container">
    <div class="itineraryTitle">{{ $t('projectDetailPage.itinerary.title') }}</div>
    <div class="itineraryCore">
      <div class="timeLine">
        <div v-for="(item, index) in this.itineraryData">
          <itinerary-step :item="item" :index="index"></itinerary-step>
        </div>
      </div>
      <div class="map" id="map"></div>
    </div>
  </div>
</template>

<script>
import ItineraryStep from "./itineraryStep.vue";
import {Loader} from "@googlemaps/js-api-loader";
import {useRoute} from 'vue-router';
import {ref} from 'vue';
import {useLangStore} from "../../store.js";
export default {
  name: "itineraryPart",
  components: {ItineraryStep},
  setup(){
    let project_loc = null;
    let project_zoom = 1;
    const raw_trip_data = ref([]);
    const locations = [];
    // const itineraryData = [];
    const langStore = useLangStore();
    let mapLanguage = 'en-US';
    if (langStore.language === 'zh'){
      mapLanguage = 'zh-CN'
    }
    return{
      raw_trip_data,
      project_loc,
      project_zoom,
      locations,
      // itineraryData,
      loadMap(){
        const loader = new Loader({
          apiKey: "AIzaSyBctzU8ocpP_0j4IdTRqA-GABIAnaXd0ow",
          version: "beta",
          libraries: ["marker"],
          language: mapLanguage
        });

        loader.load().then((google) => {
          const center = this.project_loc;
          let map = new google.maps.Map(document.getElementById("map"), {
            center: center,
            zoom: this.project_zoom,
            mapId: "jkhjkhkjhjkh"
          });
          const tourStops = this.locations;
          // Create an info window to share between markers.
          const infoWindow = new google.maps.InfoWindow();
          tourStops.forEach(({ position, title }, i) => {
            const pinView = new google.maps.marker.PinView({
              glyph: `${i + 1}`,
            });
            const marker = new google.maps.marker.AdvancedMarkerView({
              position,
              map,
              title: `${i + 1}. ${title}`,
              content: pinView.element,
            });

            // Add a click listener for each marker, and set up the info window.
            marker.addListener("click", ({ domEvent, latLng }) => {
              const { target } = domEvent;

              infoWindow.close();
              infoWindow.setContent(marker.title);
              infoWindow.open(marker.map, marker);
            });
          });

        });
      }
    }
  },
  created() {
    const route = useRoute();
    this.axios.post('/product/trips', {
        product_id: route.params.trip_id
      })
        .then((res) => {
          this.project_loc = {
            lat: res.data.location.map_latitude,
            lng: res.data.location.map_longitude
          }
          this.project_zoom = res.data.location.map_zoom;
          this.raw_trip_data.value = res.data.trips
          for (let i = 0; i < this.raw_trip_data.value.length; i++){
            this.locations.push({
              position: {lat: this.raw_trip_data.value[i].location.map_latitude, lng: this.raw_trip_data.value[i].location.map_longitude},
              title: this.raw_trip_data.value[i].location.exact
            });
            this.itineraryData.push({
              name: this.raw_trip_data.value[i].activity,
              time: "Day " + this.raw_trip_data.value[i].day + ", " + this.raw_trip_data.value[i].time_of_day + " " + this.raw_trip_data.value[i].time,
              description: this.raw_trip_data.value[i].location.exact,
              picture: this.raw_trip_data.value[i].picture
            })
          }
          this.loadMap();
        })
  },
  data(){
    return{
      itineraryData: []
    }
  }
}
</script>

<style scoped>
.container{
  width: 1320px;
  margin: 0 auto;
}
.itineraryTitle{
  margin-bottom: 20px;
  font-size: 22px;
  font-weight: 500;
  line-height: 1.45;
}
.itineraryCore{
  width: 100%;
  display: flex;
}
.timeLine{
  width: 560px;
  margin: 15px;
}
.map{
  width: 730px;
  margin: 15px;
  background-color: #051036;
  border-radius: 4px;
  min-height: 500px;
}

@media (min-width:576px){
  .container{
    max-width:540px
  }
  .itineraryCore{
    flex-direction: column;
  }
}
@media (min-width:768px){
  .container{
    max-width:720px
  }
}
@media (min-width:992px){
  .container{
    max-width:960px
  }
  .itineraryCore{
    flex-direction: row;
  }
}
@media (min-width:1200px){
  .container{
    max-width:1140px
  }
}
@media (min-width:1400px){
  .container{
    max-width:1320px
  }

}
</style>
