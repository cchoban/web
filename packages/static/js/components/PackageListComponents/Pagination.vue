<template>
  <div aria-label="Pagination Navigation" role="navigation" class="ui pagination pointing secondary menu">
    <a class="item" v-if="previousUrl" @click="getPackages(previousUrl)">⟨</a>
    <a class="item" :class="{'active': pages == currentPage}" v-for="(num, pages) in countPageNumber" @click="getPackages('http://localhost:8000/api/packages/?limit=10&offset='+num+extra_queries, pages)">{{ pages }}</a>
    <a class="item" v-if="nextUrl" @click="getPackages(nextUrl)">⟩</a>
  </div>
</template>

<script>
export default {
  props: ["maxentry", "extra_queries"],
  data: function() {
    return {
      store: null,
      packages: null,
      nextUrl: null,
      previousUrl: null,
      count: null,
      currentPage: 1,
      offset: null,
      request_url: ""
    };
  },
  beforeMount: function() {
    this.store = store;
  },
  mounted: function() {
    this.packages = this.store.state.package_page.packages;
    this.nextUrl = this.store.state.package_page.nextUrl;
    this.previousUrl = this.store.state.package_page.previousUrl;
    this.count = this.store.state.package_page.count;
  },

  computed: {
    countPageNumber: function() {
      var totalPageNumber = Math.ceil(this.count / this.maxentry);
      var pages = {};
      var offset = -10;
      var page = 1;
      for (page; page <= totalPageNumber; page++) {
        pages[page] = offset += 10;
      }

      return pages;
    }
  },
  methods: {
    getPackages: function(url, pageNumber) {
      axios
        .get(url)
        .then(response => {
          this.packages = response.data.results;
          this.count = response.data.count;
          this.nextUrl = response.data.next;
          this.previousUrl = response.data.previous;
          this.store.state.loading = false;
          this.store.state.package_page.packages = response.data.results;
          this.store.state.package_page.count = response.data.results.count;
          this.store.state.package_page.nextUrl = response.data.results.next;
          this.store.state.package_page.previousUrl =
            response.data.results.previous;
          this.pushState(pageNumber);
        })
        .catch(response => {
          console.log("error");
        });
    },
    pushState: function(pageNumber) {
      this.currentPage = pageNumber;
    }
  }
};
</script>

<style>
</style>
