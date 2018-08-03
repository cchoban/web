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

                        <div class="homeBtn bttns">
                            <i class="redo icon"></i>
                        </div>

                        <div class="reloadBtn bttns">
                            <i class="home icon"></i>
                        </div>
                    </div>


                    <search-package></search-package>

                    <div class="buttons column">
                        <div class="bttns menu">
                            <a class="ui button loginBtn">
                                <i class="user circle icon"></i>
                                <span @click="test">qwe</span>
                            </a>
                        </div>

                    </div>
                </div>
            </div>
    </div>
</template>

<script>
export default {
  data: function() {
    return {
      //
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
        history.back();
      }
    },

    goForward: function() {
      store.state.isPage = true;
      history.forward();
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
        store.state.isPage = true;
        return true;
      }

      history.back();
    }
  }
};
</script>

<style type="scss" scoped>
    .push {
        margin-bottom:50px;
    }
</style>
