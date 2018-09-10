<template>
<div>
    <div class="section twentyfivepx column">
        <a href="all" class="header-text bold removelink">
            <h2 class="left-floated">Editor Picks</h2>
            <label class="view-all unbold right-floated"> View all
                <i class="angle right icon"></i>
            </label>
        </a>
        <div class="inner-section">
            <div class="ui segments panel">
                <div class="ui segment panel-header">
                    <p class="bold">Most Popular Softwares</p>
                </div>
                <div class="ui secondary segment panel-content">
                    <div v-if="loading">
                        <div class="ui attached segment loading"><br></div>
                    </div>
                    <div class="ui attached segment listings" v-for="package in pickedPopulars.slice(0, 5)" @click="showPage(package.packageName, package.id)">
                        <div class="topla" >
                            <img class="ui avatar image remove-circle" :src="package.server.icon" alt="">
                            <span class="text">{{ package.packageName }}</span>
                            <span class="right-floated day"><timeago :since="package.updated_at"></timeago></span>
                        </div>
                    </div>
                </div>
                <div class="ui panel-footer column">
                    <a class="removelink loadMoreBtn" href="popular">
                        <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                        <!-- TODO: create popular packages section for recent packages -->
                    </a>
                </div>
            </div>
        </div>

        <div class="inner-section">
            <div class="ui segments panel">
                <div class="ui segment panel-header">
                    <p class="bold">Other Softwares</p>
                </div>
                <div class="ui secondary segment panel-content">
                    <div v-if="loading">
                        <div class="ui attached segment loading"><br></div>
                    </div>
                    <div class="ui attached segment listings" v-for="package in pickedPackages.slice(0, 5)" @click="showPage(package.packageName, package.id)">

                        <div class="topla" >
                            <img class="ui avatar image remove-circle" :src="package.server.icon" alt="">
                            <span class="text">{{ package.packageName }}</span>
                            <span class="right-floated day"><timeago :since="package.updated_at"></timeago></span>
                        </div>
                    </div>
                </div>
                <div class="ui panel-footer column">
                    <a class="removelink loadMoreBtn" href="all">
                        <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                        <!-- TODO: create recent packages section for recent packages -->
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
      store: null,
      loading: true,
      pickedPackages: {},
      pickedPopulars: {}
    };
  },
  mounted: function() {
    this.getPicked();
    this.getPopularPicked();
  },
  beforeMount: function() {
    this.store = store;
  },
  methods: {
    showPage: function(packageName, packageId) {
      this.packageName = packageName;
      store.state.package.name = packageName;
      store.state.package.id = packageId;
      this.packageId = packageId;
      this.store.state.isPage = true;
      this.loading = false;
    },
    category_url: function(category_name) {
      var slugged = Vue.options.filters.slugify(category_name);
      return "/packages/category/" + slugged;
    },
    getPicked: function() {
      var url = "/api/packages/?showcase=true";
      axios
        .get(url)
        .then(response => {
          this.pickedPackages = response.data.results;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    getPopularPicked() {
      var url = "/api/packages/?showcase=true&ordering=-download_count";
      axios
        .get(url)
        .then(response => {
          this.pickedPopulars = response.data.results;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style>
</style>
