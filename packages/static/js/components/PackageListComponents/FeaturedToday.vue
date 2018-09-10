<template>
    <div class="ui container fluid left">
        <div class="featured-items twentyfivepx">
            <div class="featured-header-text">
                <h2>Featured today</h2>
            </div>

            <div class="featured-item-list">

                <div v-for="package in popularPackages" v-if="!loading">
                    <a class="featured-item" :style='"background-image: linear-gradient(to top, black, transparent), url("+package.server.icon+");"' @click="showPage(package.packageName, package.id)">
                        <h1> {{ package.packageName }} </h1>
                        <p></p>
                        <label>
                            <a :href="category_url(package.category_name)" class="removelink addCatUrl">{{ package.category_name }}</a>
                        </label>
                    </a>
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
      popularPackages: {}
    };
  },
  mounted: function() {
    this.getPopular();
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
    getPopular: function() {
      var url = "/api/packages/?ordering=-download_count";
      axios
        .get(url)
        .then(response => {
          this.popularPackages = response.data.results.slice(0, 10);
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
