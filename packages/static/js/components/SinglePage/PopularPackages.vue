<template>
<div class="ui container">
    <div class="ui segment loading" v-if="store.state.loading">
        <br>
    </div>
    <div v-else>
        <Pagination :maxentry="maxentry" extra_queries="&ordering=-download_count"></Pagination>
        <table class="ui table">
            <thead>
                <tr>
                    <th>Popular packages</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="package in store.state.package_page.packages">
                <td>
                    <h4 class="ui image header">
                    <img :src="package.server.icon" class="ui mini rounded image">
                    <div class="content package-specifics">
                        <a :href="package.packageName" class="removelink"> {{  package.packageName }} </a>
                        <div class="sub header">
                            <a href="#" class="removelink"> {{  package.packageArgs.description }} </a> 
                        </div>
                    </div>
                </h4>
                </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
export default {
  props: ["maxentry"],
  data: function() {
    return {
      packages: [],
      nextUrl: null,
      previousUrl: null,
      image: "",
      store: null,
      count: null
    };
  },
  beforeMount: function() {
    this.store = store;
    $(".root").addClass("index");
  },
  mounted: function() {
    this.grabPackages();
  },

  methods: {
    grabPackages: function() {
      var url = "/api/packages/?ordering=-download_count";
      axios.get(url).then(response => {
        this.packages = response.data.results;
        this.count = response.data.count;
        this.selectRandomImage();
        this.store.state.loading = false;
        this.store.state.package_page.packages = response.data.results;
        this.store.state.package_page.count = response.data.count;
        this.store.state.package_page.nextUrl = response.data.next;
        this.store.state.package_page.previousUrl = response.data.previous;
      })
      .catch(response => {
          console.log('error')
      });
    },
    selectRandomImage: function() {
      var i;
      var rand = this.packages[this.getRandomInt(0, this.packages.length)];
      if (rand) {
        this.image = rand.server.icon;
      }
    },
    getRandomInt: function(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }
  }
};
</script>

<style lang="scss" scoped>
.content {
  .posts {
    width: inherit !important;
  }
}

.package-specifics {
    width: 86%;
}
</style>
