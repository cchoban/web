<template>
    <div>

    <div class="buttons column">
        <div class="bttns menu">
            <a class="ui button loginBtn" @click="showAccountMenu">
                <i class="user circle icon"></i>
                <span>{{ user.username }}</span>
            </a>
        </div>
    </div>

    <div class="ui modal accountModal">
        <i class="close icon"></i>
        <div class="header">
        Profile Picture
        </div>
        <div class="image content">
        <div class="ui medium image">
            <img :src="user.profilePicture">
        </div>
        <div class="description">
            <div class="ui header">Account configuration</div>
            <br>
            <div class="ui green button" @click="redirect('/account/token')">
                Get API token
            </div>
        </div>
        </div>
        <div class="actions">
        <div class="ui deny right labeled icon button">
            Done
            <i class="checkmark icon"></i>
        </div>
        </div>
    </div>

</div>


</template>

<script>
export default {
  data: function() {
    return {
      user: store.state.user
    };
  },
  mounted: function() {
    //
  },
  methods: {
    showAccountMenu: function() {
      $(".accountModal").modal("show");
    },

    redirect: function(url) {
      if (url != "") {
        window.location.href = url;
      }
    }
  }
};
</script>

<style>
</style>
