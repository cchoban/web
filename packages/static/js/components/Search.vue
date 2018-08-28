<template>
      <div class="searchField column">
            <div class="ui form">
                <div class="field">
                    <input name="packageName" placeholder="Search for your favorite package" type="text" v-model="store.state.search_key" @keyup.enter.prevent="getPackages">
                </div>
            </div>
      </div>
</template>

<script>
export default {
  data: function() {
    return {
      store: null
    };
  },
  beforeMount: function() {
    this.store = store;
  },
  methods: {
    getPackages: function() {
      var url = "/api/packages/?search=" + this.store.state.search_key;

      axios
        .get(url)
        .then(response => {
          this.store.state.package_page.packages = response.data.results;
          this.store.state.package_page.count = response.data.count;
          this.store.state.package_page.nextUrl = response.data.next;
          this.store.state.package_page.previousUrl = response.data.previous;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        });
    }
  }
};
</script>

<style>
</style>
