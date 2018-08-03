<template>

<div>

<button class="ui positive button" @click="goBack" v-if="store.state.isPage" style="width:100%;margin:20px"> Go back</button>
<package-page :packagename="store.state.package.name" :packageid="store.state.package.id" v-if="store.state.isPage"></package-page>

<div class="right floated background-gray switch-command">
    <div class="ui toggle checkbox">
      <input name="public" type="checkbox" v-model="showCommandLine">
      <label>Enable fast installation</label>
    </div>
</div>

<div class="ui container fluid left">

        <div class="featured-items twentyfivepx">
            <div class="featured-header-text">
                <h2>Featured today</h2>
            </div>

            <div class="featured-item-list">
                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>

                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>

                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>

                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>

                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>

                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>

                <a class="featured-item" style='background-image: linear-gradient(to top, black, transparent), url("https://media.npr.org/assets/img/2016/05/19/invisibiliapodcast_icon_hotpink-01_sq-2359778531d9733109e3674a5cecf5a711aa511f.jpg?s=200");'>
                    <h1>People In Tech</h1>
                    <p></p>
                    <label> podcast </label>
                </a>
            </div>
        </div>
    </div>

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
                        <div class="ui attached segment listings" v-for="package in store.state.package_page.packages" @click="showPage(package.packageName, package.id)">
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
            <div class="inner-section">
                <div class="ui segments panel">
                    <div class="ui segment panel-header">
                        <p class="bold">Recent Episodes</p>
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
<!-- <div v-else>
  <div class="alert alert-info">
      No packages found <b v-if="search_key">{{ search_key }}</b>
  </div>
</div> -->




<div aria-label="Pagination Navigation" role="navigation" class="ui pagination pointing secondary menu">
  <a class="item" v-if="packages.previous != null" @click="getPackages(previousUrl)">⟨</a>
  <a class="item" v-for="(num, pages) in countPageNumber" @click="getPackages('http://localhost:8000/api/packages/?limit=10&offset='+num)">{{ pages }}</a>
  <a class="item" v-if="packages.next != null" @click="getPackages(nextUrl)">⟩</a>
</div>

</div>
</div>
</template>

<script>
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
      search_key: "",
      showCommandLine: false,
      store: null
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
    this.getPackages();
    this.countPageNumber;
  },

  methods: {
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
    }
  }
};
</script>
