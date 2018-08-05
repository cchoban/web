<template>
    <div class="push">
        <div class="window-title column">
                <a href="#" class="removelink"> title </a>
            </div>
            <div class="ui menu header-navbar">
                <div class="ui two column container fluid ">

                    <div class="buttons column">
                        <div class="backBtn bttns" @click="goBack">
                            <i class="angle left icon"></i>
                        </div>

                        <div class="forwardBtn bttns" @click="goForward">
                            <i class="angle right icon"></i>
                        </div>

                        <div class="homeBtn bttns" @click="refresh">
                            <i class="redo icon"></i>
                        </div>

                        <div class="reloadBtn bttns" @click="goHome">
                            <i class="home icon"></i>
                        </div>
                    </div>


                    <search-package></search-package>
                    <login v-if="!logged_in"></login>
                    <div v-else>
                      <userAccount></userAccount>
                    </div>

                </div>
            </div>

    </div>
</template>

<script>
export default {
  data: function() {
    return {
      logged_in: store.state.logged_in
    };
  },
  mounted: function() {
    //
  },
  methods: {
    goBack: function() {
      if (this.onPackagePage()) {
        store.state.isPage = false;
        history.pushState(null, null, "/packages");
      } else {
        if (this.isPackagePage()) {
          store.state.isPage = true;
        }else {
          history.back();
        }
      }
    },

    goForward: function() {
      if(this.isPackagePage()){
        store.state.isPage = true;
      }
      history.forward();
    },

    goHome: function() {
      if (this.onPackagePage()) {
        store.state.isPage = false;
        history.pushState(null, null, "/packages");
      } else {
        window.location.href = "/packages";
      }
    },

    refresh: function() {
      window.location.reload();
    },

    onPackagePage: function() {
      if (store.state.isPage == true) {
        return true;
      } else {
        return false;
      }
    },

    isPackagePage: function() {
      var urlToGoBack = store.state.history[store.state.history.length - 2];
      if (urlToGoBack) {
        store.state.isPage = true;
        return true;
      } else {
        var urlToGoBack = store.state.history[store.state.history.length - 1];
        if(urlToGoBack){
          store.state.isPage = true;
          return true;
        }
        return false
      }

    }
  }
};
</script>

<style type="scss" scoped>
.push {
  margin-bottom: 50px;
}
</style>
