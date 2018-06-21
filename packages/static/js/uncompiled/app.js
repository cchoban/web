import VueTimeago from 'vue-timeago'
window.Vue = require('vue');

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
/**
* Next, we will create a fresh Vue application instance and attach it to
* the page. Then, you may begin adding components to this application
* or customize the JavaScript scaffolding to fit your unique needs.
*/

Vue.component('packages-list', require('../components/PackagesList.vue'));
Vue.component('readMore', require('../components/readMore.vue'));
Vue.component('package-page', require('../components/singlePage.vue'));
Vue.component('installCommand', require('../components/installCommandLine.vue'));

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