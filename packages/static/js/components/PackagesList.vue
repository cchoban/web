<template>

<div>

<button class="ui positive button" @click="goBack" v-if="store.state.isPage" style="width:100%;margin:20px"> Go back</button>
<package-page :packagename="store.state.package.name" :packageid="store.state.package.id" v-if="store.state.isPage"></package-page>

<!-- <div class="background-gray switch-command">
    <div class="ui toggle checkbox">
      <input name="public" type="checkbox" v-model="showCommandLine">
      <label>Enable fast installation</label>
    </div>
</div> -->

<div v-if="!store.state.isPage">
    <PopularPackages></PopularPackages>

    <div class="ui three column container fluid content-section">
        <div class="section twentyfivepx column">
            <a href="#" class="header-text bold removelink">
                <h2 class="left-floated">Packages</h2>
                <label class="view-all unbold right-floated"> View all
                    <i class="angle right icon"></i>
                </label>
            </a>
            <div class="inner-section">
                <div class="ui segments panel">
                    <div class="ui segment panel-header">
                        <p class="bold">Popular</p>
                    </div>
                    <div class="ui secondary segment panel-content">
                        <div v-if="loading">
                            <div class="ui attached segment loading"><br></div>
                        </div>
                        <div class="ui attached segment listings" v-for="package in popularPackages.slice(0, 5)" @click="showPage(package.packageName, package.id)">
                            <div class="topla" >
                                <img class="ui avatar image remove-circle" :src="package.server.icon" alt="">
                                <span class="text">{{ package.packageName }}</span>
                                <span class="right-floated day"><timeago :since="package.updated_at"></timeago></span>
                            </div>
                        </div>
                    </div>
                    <div class="ui panel-footer column">
                        <a class="removelink loadMoreBtn" href="popular-packages">
                            <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                            <!-- TODO: create popular packages section for recent packages -->
                        </a>
                    </div>
                </div>
            </div>
            <div class="inner-section">
                <div class="ui segments panel">
                    <div class="ui segment panel-header">
                        <p class="bold">Recent Packages</p>
                    </div>
                    <div class="ui secondary segment panel-content">
                        <div v-if="loading">
                            <div class="ui attached segment loading"><br></div>
                        </div>
                        <div class="ui attached segment listings" v-for="package in recentPackages.slice(0, 5)" @click="showPage(package.packageName, package.id)">
                            <div class="topla" >
                                <img class="ui avatar image remove-circle" :src="package.server.icon" alt="">
                                <span class="text">{{ package.packageName }}</span>
                                <span class="right-floated day"><timeago :since="package.updated_at"></timeago></span>
                            </div>
                        </div>
                    </div>
                    <div class="ui panel-footer column">
                        <a class="removelink loadMoreBtn">
                            <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                            <!-- TODO: create recent packages section for recent packages -->
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <div class="second-section column twentyfivepx clearfix">
                <a href="#" class="header-text bold removelink">
                    <h2 class="left-floated bold">RSS</h2>
                    <label class="view-all unbold right-floated"> View all
                        <i class="angle right icon"></i>
                    </label>
                </a>
                <div class="inner-section">
                    <div class="ui segments panel">
                        <div class="ui segment panel-header">
                            <p class="bold">Recent Articles</p>
                        </div>
                        <div class="ui secondary segment panel-content">
                            <div class="ui attached segment listings">
                                <div class="topla">
                                    <img class="ui avatar image remove-circle" src="https://d12xoj7p9moygp.cloudfront.net/favicon/favicon-128.png" alt="">
                                    <span class="text">This segment is attached on both sides</span>
                                    <span class="right-floated day">5 day ago</span>
                                </div>

                            </div>
                        </div>
                        <div class="ui panel-footer column">
                            <a class="removelink loadMoreBtn">
                                <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                            </a>
                        </div>
                    </div>
                </div>


                <div class="inner-section">
                    <div class="ui segments panel">
                        <div class="ui segment panel-header">
                            <p class="bold">Feeds</p>
                        </div>
                        <div class="ui secondary segment panel-content">
                            <div class="ui attached segment listings">
                                <div class="topla">
                                    <img class="ui avatar image remove-circle" src="https://d12xoj7p9moygp.cloudfront.net/favicon/favicon-128.png" alt="">
                                    <span class="text">This segment is attached on both sides</span>
                                    <span class="right-floated day"><i class="angle right icon"></i></span>
                                </div>

                            </div>
                        </div>
                        <div class="ui panel-footer column">
                            <a class="removelink loadMoreBtn">
                                <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="third-section column twentyfivepx clearfix">
                <a href="#" class="header-text bold removelink">
                    <h2 class="left-floated">Discover</h2>
                    <label class="view-all unbold right-floated"> View all
                        <i class="angle right icon"></i>
                    </label>
                </a>
                <div class="inner-section">
                    <div class="ui segments panel">
                        <div class="ui segment panel-header">
                            <p class="bold">Random Packages</p>
                        </div>
                        <div class="ui secondary segment panel-content">
                        <div v-if="loading">
                            <div class="ui attached segment loading"><br></div>
                        </div>
                        <div class="ui attached segment listings" v-for="package in discoverPackages.slice(0, 5)" @click="showPage(package.packageName, package.id)">
                            <div class="topla" >
                                <img class="ui avatar image remove-circle" :src="package.server.icon" alt="">
                                <span class="text">{{ package.packageName }}</span>
                                <span class="right-floated day"><timeago :since="package.updated_at"></timeago></span>
                            </div>
                        </div>
                    </div>
                        <div class="ui panel-footer column">
                            <a class="removelink loadMoreBtn">
                                <i class="angle down icon light" style="font-size:20px;margin:0 auto"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
const slugify = require("slugify");
export default {
  props: ["maxentry"],
  data: function() {
    return {
      message: null,
      nextUrl: null,
      previousUrl: null,
      count: null,
      packageName: store.state.package.name,
      packageId: null,
      packages: [],
      popularPackages: [],
      recentPackages: [],
      discoverPackages: [],
      search_key: "",
      showCommandLine: false,
      store: null,
      loading: true
    };
  },

  computed: {
    countPageNumber: function() {
      var totalPageNumber = Math.ceil(this.count / this.maxentry);

      var pages = {};
      var offset = -10;
      for (var page = 1; page <= totalPageNumber; page++) {
        pages[page] = offset += 10;
      }
      return pages;
    }
  },
  beforeMount: function() {
    this.store = store;
  },
  mounted: function() {
    // this.store = store;
    this.getPopular();
    this.getRecent();
    this.getDiscover();
    this.countPageNumber;
    $(".root").addClass("index");
  },

  methods: {
    getPopular: function() {
      var url = "/api/packages/?ordering=-download_count";
      axios
        .get(url)
        .then(response => {
          this.popularPackages = response.data.results;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },

    getRecent: function() {
      var url = "/api/packages/?ordering=-created_at";
      axios
        .get(url)
        .then(response => {
          this.recentPackages = response.data.results;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },

    getDiscover: function name() {
      var url = "/api/packages";
      axios
        .get(url)
        .then(response => {
          this.packages = response.data;
          this.discoverPackages = this.shuffleArray(response.data.results);
          this.count = response.data.count;
          this.nextUrl = response.data.next;
          this.previousUrl = response.data.previous;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        });
    },
    getPackages: function(url = "/api/packages") {
      axios
        .get(url)
        .then(response => {
          this.packages = response.data;
          store.state.package_page.packages = response.data.results;
          this.count = response.data.count;
          this.nextUrl = response.data.next;
          this.previousUrl = response.data.previous;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        });
    },

    showPage: function(packageName, packageId) {
      this.packageName = packageName;
      store.state.package.name = packageName;
      store.state.package.id = packageId;
      this.packageId = packageId;
      this.store.state.isPage = true;
    },

    goBack: function() {
      this.store.state.isPage = false;
      history.pushState(null, null, "/packages");
    },
    shuffleArray: function(sourceArray) {
      for (var i = 0; i < sourceArray.length - 1; i++) {
        var j = i + Math.floor(Math.random() * (sourceArray.length - i));

        var temp = sourceArray[j];
        sourceArray[j] = sourceArray[i];
        sourceArray[i] = temp;
      }
      return sourceArray;
    },
    category_url: function(category_name) {
      var slugged = Vue.options.filters.slugify(category_name);
      return "/packages/category/" + slugged;
    }
  }
};
</script>
