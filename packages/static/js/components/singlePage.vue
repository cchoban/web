<template>
    <div class="ui container grid">
      <div class="ui segment fifteen column row">
        <div class="ui medium three wide image column">
          <img :src="package.server.icon" alt="">
        </div>

        <div class="ui content twelve wide column right floated">
          <label class="ui green label">Download count: {{ package.download_count }}</label>
          <label class="ui yellow label">View count: {{ package.view_count }}</label>
          <label class="ui gray label">Last update: <timeago :since="package.updated_at"></timeago> </label>
          <label class="ui blue label">Submitted at: <timeago :since="package.created_at"></timeago></label>

          <div class="ui segments">
            <div class="ui segment">
              <p>Package name: {{ package.packageName }}</p>
            </div>
            <div class="ui segment">
              <p>Description: {{ package.packageArgs.description }}</p>
            </div>
            <div class="ui segment">
              <p>Version: {{ package.packageArgs.version }}</p>
            </div>
            <div class="ui segment">
              <p>Published by: {{ package.user_name }}</p>
            </div>
            <div class="ui segment" v-if="package.category_name">
              <p>Category:
                <a :href="category_url(package.category_name)"> {{ package.category_name }}</a>
              </p>
            </div>
            <div class="ui segment">
              <p>
                <installCommand :packagename="package.packageName"></installCommand>
              </p>
            </div>
          </div>
        </div>

        <div class="ui twelve wide column left floated">
          <button class="ui positive button" @click.prevent="showIcerik('install')">
            Insallation Script
          </button>
          <button class="ui danger button" @click.prevent="showIcerik('uninstall')">
            Uninstallation Script
          </button>

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
    </div>
    </div>
  </div>

</template>

<script>
var hljs = require("highlight.js");
export default {
  props: ["packagename", "packageid"],
  data: function() {
    return {
      package: [],
      loading: true,
      isPage: false,
      storeman: store,
      active: false
    };
  },
  mounted: function() {
    hljs.initHighlightingOnLoad();
    this.getPackage(this.packageid);
    this.pushState();
  },
  methods: {
    getPackage(id) {
      axios
        .get(`/api/packages/` + id)
        .then(response => {
          this.package = response.data;
          this.loading = false;
          return true;
        })
        .catch(err => {
          this.loading = false;
          return false;
        });
    },

    showIcerik(todo) {
      if (this.active == todo) {
        this.active = false;
        return true;
      }

      this.active = todo;
    },

    pushState() {
      store.state.history.push(this.packagename);
      history.pushState(null, null, "/packages/" + this.packagename);
    },
    category_url: function (category_name) {
      return '/packages/category/'+Vue.options.filters.slugify(category_name)
    }
  }
};
</script>

<style scoped>
.content {
  width: 59%;
  float: right;
  margin-bottom: 50px !important;
}
</style>
