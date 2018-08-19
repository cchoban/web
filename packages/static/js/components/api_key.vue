<template>
<div class="ui container ">
    <div class="column">
      <h4 class="ui top attached header">API 2Key</h4>
      <div class="ui bottom attached segment">
        <p>Grab your API key to push new packages!</p>
        <p>Your API key provides you with a token that identifies you to the gallery. Keep this a secret. You can always regenerate your key at any time (invalidating previous keys) if your token is accidentally revealed. The You would pass your token like this: </p>
      
        <div class="ui form">
          <label for="apikey">
            Your API key is:
          </label>
          <br>
          <input type="text" class='form-control' id='apikey' style="width: 350px; display:inline-block" disabled v-model="api_key"> <span v-html="copy_icon" @click="copy_api"></span>
          <input type="hidden" id="copy-apikey" :value="api_key">
          <br>
          <br>
          <a href="#" class="ui button" @click="generate_token">Grab new token</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var octicons = require("octicons");
var swal = require("sweetalert2");
export default {
  data: function() {
    return {
      api_key: "",
      copy_icon: ""
    };
  },
  mounted: function() {
    this.copy_icon = octicons.clippy.toSVG();
    this.get_key();
  },
  methods: {
    get_key: function(url = "token") {
      axios
        .post(url)
        .then(response => {
          this.api_key = response.data.key;
          this.loading = false;

          if (respose.data.status == false) {
            swal("Oops!", response.data.message, "error");
          } else {
            swal("Yess!", response.data.message, "success");
          }
        })
        .catch(err => {
          this.loading = false;
        });
    },

    generate_token: function() {
      var url = "token";
      var bodyFormData = new FormData();
      bodyFormData.set("generate_new_token", true);
      axios
        .post(url, bodyFormData)
        .then(response => {
          if (response.data.status == false) {
            swal("Oops!", response.data.message, "error");
          } else {
            this.api_key = response.data.key;
            swal("Yess!", response.data.message, "success");
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
    copy_api: function() {
      let apikey = document.querySelector("#copy-apikey");
      apikey.setAttribute("type", "text");
      apikey.select();

      try {
        var successful = document.execCommand("copy");
        var msg = successful ? "successful" : "unsuccessful";
        swal({
          title: "Success",
          text: "Api key was copied " + msg,
          type: "success",
          toast: true,
          position: "bottom-end"
        });
      } catch (err) {
        console.log(err);
        alert("Oops, unable to copy");
      }

      apikey.setAttribute("type", "hidden");
      window.getSelection().removeAllRanges();
    }
  }
};
</script>

<style>
</style>
