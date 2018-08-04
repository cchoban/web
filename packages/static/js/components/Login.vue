<template>
    <div>
        <div class="buttons column">
            <div class="bttns menu">
                <a class="ui button loginBtn" @click="showModal">
                    <i class="user circle icon"></i>
                    <span>Login</span>
                </a>
            </div>
        </div>

        <div class="ui modal loginModal">
            <i class="close icon"></i>
            <div class="header">
                Login to Choban
            </div>
            <form class="ui form segment attached">
                <div id="div_id_username" class="field">
                    <label for="id_username" class="requiredField">
                        Username<span class="asteriskField">*</span></label>
                    <input name="username" autofocus="autofocus" maxlength="254" required="required" id="id_username" class="textinput textInput" type="text" v-model="username">
                </div>
                <div id="div_id_password" class="field">
                    <label for="id_password" class="requiredField">
                        Password<span class="asteriskField">*</span></label>
                    <input name="password" required="required" id="id_password" class="textinput textInput" type="password" v-model="password" @keyup.enter.prevent="login">
                </div>
            </form>
            <div class="actions">
                <div class="ui black deny button">
                Nope
                </div>
                <div class="ui positive right labeled icon button" @click="login">
                Yep, that's me. Login
                <i class="checkmark icon"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
var swal = require("sweetalert2");
export default {
  data: function() {
    return {
      username: null,
      password: null
    };
  },
  methods: {
    showModal: function() {
      $(".loginModal").modal("show");
    },

    login: function() {
      var url = "/login";
      var data = new FormData();
      data.append("username", this.username);
      data.append("password", this.password);

      if (this.validated_forms()) {
        axios
          .post(url, data)
          .then(response => {
            if (response.data.status) {
              swal("Yess!", response.data.message, "success");
              store.commit('logged_in', true);
            } else {
              swal("Oops!", response.data.message, "error");
            }
          })
          .catch(err => {
            swal(
              "Oops!",
              "Could not login right now. Please try again later.",
              "error"
            );
          });
      } else {
        console.log("Verify your form.");
      }
    },

    validated_forms: function() {
      if (this.username == null || this.password == null) {
        swal(
          "Oops!",
          "You have empty field(s). Please fill them if you want to contiune",
          "error"
        );

        return false;
      } else {
        return true;
      }
    }
  }
};
</script>

<style>
</style>
