<template>
        <div id="profile">
            <div class="card card-body mb-3">
                    <div class="row">
                      <div class="col-md-3">
                        <img class="img-fluid mb-2" :src="package.server.icon">
                        <!-- <a href="#" target="_blank" class="btn btn-danger btn-block mb-4">Profili Görüntüle</a> -->
                      </div>
                      <div class="col-md-9">
                        <span class="badge badge-primary">Download count: {{ package.download_count}} </span>
                        <span class="badge badge-secondary">Last update: <timeago :since="package.updated_at"></timeago> </span>
                        <span class="badge badge-success">Submitted at: <timeago :since="package.created_at"></timeago></span>
                        <span class="badge badge-info">Takip Edilen: </span>
                        <br><br>
                        <ul class="list-group">
                          <li class="list-group-item">Package: {{ package.packageArgs.softwareName }}</li>
                          <li class="list-group-item">Description: {{ package.packageArgs.description }}</li>
                          <li class="list-group-item">Version: {{ package.packageArgs.version }}</li>
                          <li class="list-group-item">Published by: {{ package.user }}</li>
                          <li class="list-group-item" v-if="package.packageArgs.dependencies">Dependencies: 
                            <span v-for="package in package.packageArgs.dependencies">
                                <a :href="package"> {{ package }}</a>
                            </span>
                          </li>
                          <li class="list-group-item">
                            Install: <installCommand :packagename="package.packageName"></installCommand>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="as">
                    <a href="" class="btn btn-info" @click.prevent="showIcerik('install')">Install Script</a>
                    <a href="" class="btn btn-info" @click.prevent="showIcerik('uninstall')">Uninstall Script</a>

                    <div  v-if="active == 'install'">
                      <pre v-highlightjs>
                      <code class="json">
                          {{ package.packageArgs }}
                      </code>
                      </pre>
                    </div>

                    <div  v-if="active == 'uninstall'">
                      <pre v-highlightjs>
                        <code class="json">
                          {{ package.packageUninstallArgs }}
                        </code>
                      </pre>
                    </div>
                  </div>

                  <!-- <h3 class="page-heading mb-3">En son repolar</h3>
                  <div id="repos" style ="margin-bottom: 100px;">
                        <div class="card card-body mb-2">
                                <div class="row">
                                  <div class="col-md-6">
                                    <span>Sıfırdan İleri Seviyeye Python</span>
                                    <a href="https://www.facebook.com/" target = "_blank" class = "btn btn-danger"> Repoya Git</a>
                                  </div>
                                  <div class="col-md-6">
                                  <span class="badge badge-primary">Yıldızlar:</span>
                                  <span class="badge badge-secondary">Watchers:</span>
                                  <span class="badge badge-success">Forks:</span>
                                  </div>
                                </div>
                        </div> -->

                    <!--- Repoların Gösterileceği Kısım" -->
                  <!-- </div> -->

        </div>

</template>

<script>
var hljs = require("highlight.js")
export default {
  props: ["packagename", "packageid"],
  data: function() {
    return {
      package: [],
      loading: true,
      isPage: false,
      storeman:store,
      active: false
    };
  },
  mounted: function() {
    hljs.initHighlightingOnLoad();
    this.getPackage(this.packageid);
    this.pushState()
  },
  methods: {
    getPackage(id) {
      axios
        .get(`/api/packages/` + id)
        .then(response => {
          this.package = response.data;
          this.loading = false;
          return true
        })
        .catch(err => {
          this.loading = false;
          return false
        });
    },

    showIcerik(todo){
      if (this.active == todo) {
        this.active = false
        return true
      }

      this.active = todo

    },

    pushState() {
        store.state.history.push(this.packagename)
        history.pushState(null, null, "/packages/"+this.packagename);
    }
  }
};
</script>

<style>
</style>
