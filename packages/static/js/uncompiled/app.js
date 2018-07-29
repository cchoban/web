window.Vue = require('vue');
window.axios = require('axios');
import VueTimeago from 'vue-timeago';


function is_logged(){
  axios
    .get("/islogged")
    .then(response => {
      if(response.data.auth){
        return true
      }
    })
    .catch(err => {
      this.loading = false;
      console.log(err);
    });
}

var csrf_token = document.querySelector("meta[name='csrf-token']").getAttribute("content")
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
window.axios.defaults.headers.common['X-CSRFToken'] = csrf_token;
window.logged = is_logged()

Vue.component('packages-list', require('../components/PackagesList.vue'));
Vue.component('readMore', require('../components/readMore.vue'));
Vue.component('package-page', require('../components/singlePage.vue'));
Vue.component('installCommand', require('../components/installCommandLine.vue'));
Vue.component('apikey', require('../components/api_key.vue'));
console.log(csrf_token)
Vue.use(VueTimeago, {
    name: 'Timeago', // Component name, `Timeago` by default
    locale: null, // Default locale
    locales: {
      'zh-CN': require('date-fns/locale/zh_cn'),
      'ja': require('date-fns/locale/ja'),
    }
  })
const app = new Vue({
    el: '#app'
});

require("./vue-directives.js")
