<template>
    <div class="fields">
      <div class="field full">
        <a class="field-subtitle">{{ field_name }}*</a>
        <svg class="svg-localizacao" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M19.75 18.5828L15.267 14.0998C16.1469 13.0328 16.757 11.7697 17.0459 10.4172C17.3348 9.06475 17.2939 7.66261 16.9268 6.32925C16.5597 4.99589 15.877 3.77047 14.9366 2.7565C13.9961 1.74252 12.8254 0.96978 11.5234 0.503537C10.2214 0.0372939 8.82626 -0.108752 7.45591 0.0777351C6.08556 0.264222 4.78022 0.777764 3.65014 1.57498C2.52007 2.3722 1.59845 3.42968 0.963141 4.6581C0.32783 5.88652 -0.00251287 7.2498 1.43923e-05 8.63277C0.0063478 10.9204 0.917927 13.1126 2.53556 14.7302C4.15319 16.3479 6.34535 17.2594 8.63301 17.2658C10.6329 17.2578 12.567 16.5502 14.1 15.2658L18.583 19.7488C18.737 19.9054 18.9464 19.9952 19.166 19.9988C19.3292 19.9966 19.4882 19.9466 19.6232 19.8549C19.7582 19.7631 19.8633 19.6337 19.9254 19.4828C19.9875 19.3318 20.0039 19.166 19.9726 19.0058C19.9412 18.8456 19.8635 18.6982 19.749 18.5818L19.75 18.5828ZM1.66701 8.63277C1.66701 7.25479 2.07565 5.90775 2.84124 4.76201C3.60682 3.61627 4.69498 2.7233 5.96809 2.19601C7.2412 1.66872 8.64208 1.53081 9.99358 1.79972C11.3451 2.06862 12.5865 2.73226 13.5608 3.70671C14.5351 4.68117 15.1986 5.92266 15.4673 7.27419C15.736 8.62572 15.5979 10.0266 15.0704 11.2996C14.5429 12.5727 13.6498 13.6607 12.5039 14.4261C11.3581 15.1915 10.011 15.6 8.63301 15.5998C6.78689 15.5948 5.01782 14.8591 3.7125 13.5536C2.40717 12.2481 1.67177 10.4789 1.66701 8.63277Z" fill="#AFAFAF"/>
        </svg>
        <input ref="autocompleteInput" type="text" id="endereco" v-bind:placeholder="placeholder" />
      </div>
    </div>
  </template>
  
  <script>
  import { Loader } from "@googlemaps/js-api-loader";
  
  export default {
    name: "Autocomplete",
    components: {},
    props: {
      field_name: String,
      placeholder: String,
    },
    data() {
      return {
        autocomplete: null,
        endereco: {
          logradouro: null,
          numero: null,
          cidade: null,
          CEP: null,
          estado: null,
          pais: null,
          bairro: null, // Adicione o campo de bairro
          latitude: null,
          longitude: null,
        },
      };
    },
    methods: {
      placeChanged() {
        const place = this.autocomplete.getPlace();
        if (place.geometry) {
          if (this.extractAddressComponent(place, "street_number") === "") {
            // ID padrão para o campo do Google Maps
            document.getElementById("endereco").value = null;
            alert("Por favor, insira o número do endereço.");
            return; // Pare o processamento se o número não estiver preenchido
          }
  
          // Logradouro (Rua)
          const streetAddress = this.extractStreetAddress(place);
          this.endereco["logradouro"] = streetAddress;
  
          // Número
          const streetNumber = this.extractAddressComponent(place, "street_number");
          this.endereco["numero"] = streetNumber;
  
          // Cidade (Localidade)
          const city =
            this.extractAddressComponent(place, "locality") ||
            this.extractAddressComponent(place, "administrative_area_level_2");
          this.endereco["cidade"] = city;
  
          // CEP
          const postalCode = this.extractAddressComponent(place, "postal_code");
          this.endereco["CEP"] = postalCode;
  
          // Estado
          const stateComponent = place.address_components.find((component) => {
            return component.types.includes("administrative_area_level_1");
          });

          if (stateComponent) {
            this.endereco["estado"] = stateComponent.short_name; // Use stateComponent.short_name para a sigla
          } else {
            // Caso a sigla do estado não esteja disponível, você pode usar o nome completo do estado
            const state = this.extractAddressComponent(place, "administrative_area_level_1");
            this.endereco["estado"] = state;
          }

          // País
          const country = this.extractAddressComponent(place, "country");
          this.endereco["pais"] = country;
  
          // Bairro
          const neighborhood = this.extractAddressComponent(place, "sublocality");
          this.endereco["bairro"] = neighborhood;
  
          // Latitude e Longitude
          const latitude = place.geometry.location.lat();
          const longitude = place.geometry.location.lng();
          this.endereco["latitude"] = latitude;
          this.endereco["longitude"] = longitude;
  
          this.$parent.endereco = this.endereco;
        }
      },
  
      extractStreetAddress(place) {
        const addressComponents = place.address_components;
        for (let i = 0; i < addressComponents.length; i++) {
          for (let j = 0; j < addressComponents[i].types.length; j++) {
            if (addressComponents[i].types[j] === "route") {
              return addressComponents[i].long_name;
            }
          }
        }
        return "";
      },
  
      extractAddressComponent(place, componentType) {
        for (const component of place.address_components) {
          for (const type of component.types) {
            if (type === componentType) {
              return component.long_name;
            }
          }
        }
        return "";
      },
    },
    async mounted() {
      const rawResponse = await fetch(`/google-maps-key`, {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      const content = await rawResponse.json();
  
      const api_key = content["api_key"];
  
      const loader = new Loader({
        apiKey: api_key,
        libraries: ["places"], // Carregue a biblioteca 'places'
        language: "pt"
      });
  
      loader.load().then(() => {
        this.autocomplete = new google.maps.places.Autocomplete(
          this.$refs.autocompleteInput,
          {
            // Opções do Autocomplete
          }
        );
  
        this.autocomplete.addListener("place_changed", this.placeChanged);
  
        this.$refs.autocompleteInput.addEventListener("input", () => {
          // Atualize o objeto this.endereco sempre que o valor do campo mudar
          this.endereco = {
            logradouro: null,
            numero: null,
            cidade: null,
            CEP: null,
            estado: null,
            pais: null,
            bairro: null, // Adicione o campo de bairro
            latitude: null,
            longitude: null,
          };
        });
      });
    },
  };
  </script>
  
  <style lang="scss" scoped>
  @import "../../styles/pages/cadastrarImovel";
  </style>
  