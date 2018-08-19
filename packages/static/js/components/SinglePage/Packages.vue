<template>
<div class="ui container">
    <div class="ui segment loading" v-if="store.state.loading">
        <br>
    </div>
    <div v-else>
        <Pagination :maxentry="maxentry" extra_queries=""></Pagination>
        <table class="ui table ">
            <thead>
                <tr>
                    <th>Packages</th>
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
      store: null
    };
  },
  beforeMount: function() {
    this.store = store;
  },
  mounted: function() {
    this.getPackages();
  },
  methods: {
    getPackages: function() {
      const url = "/api/packages/";
      axios
        .get(url)
        .then(response => {
          this.packages = response.data.results;
          this.count = response.data.count;
          this.store.state.loading = false;
          this.store.state.package_page.packages = response.data.results;
          this.store.state.package_page.count = response.data.count;
          this.store.state.package_page.nextUrl = response.data.next;
          this.store.state.package_page.previousUrl = response.data.previous;
        })
        .catch(err => {
          console.log(err);
        });
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
