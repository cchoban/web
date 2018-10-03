<template>
    <div>
        <div class="section twentyfivepx column">
            <a href="all" class="header-text bold removelink">
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
                        <div class="ui attached segment listings" v-for="package in popularPackages" @click="showPage(package.packageName, package.id)">
                            <div class="topla" >
                                <span v-lazy-container="{ selector: 'img' }">
                                    <img class="ui avatar image remove-circle" :data-src="package.server.icon" alt="">
                                </span>
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
                        <p class="bold">Recent Packages</p>
                    </div>
                    <div class="ui secondary segment panel-content">
                        <div v-if="loading">
                            <div class="ui attached segment loading"><br></div>
                        </div>
                        <div class="ui attached segment listings" v-for="package in recentPackages" @click="showPage(package.packageName, package.id)">

                            <div class="topla" >
                                <span v-lazy-container="{ selector: 'img' }">
                                    <img class="ui avatar image remove-circle" :data-src="package.server.icon" alt="">
                                 </span>
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
      popularPackages: [],
      recentPackages: [],
      loading: true,
      store: null
    };
  },
  beforeMount() {
    this.store = store;
  },
  mounted: function() {
    this.getPopular();
    this.getRecent();
  },
  methods: {
    showPage: function(packageName, packageId) {
      this.packageName = packageName;
      store.state.package.name = packageName;
      store.state.package.id = packageId;
      this.packageId = packageId;
      this.store.state.isPage = true;
    },
    getPopular: function() {
      var url = "/api/packages/?ordering=-download_count";
      axios
        .get(url)
        .then(response => {
          this.popularPackages = response.data.results.slice(0,5);
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
          this.recentPackages = response.data.results.slice(0,5);
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
