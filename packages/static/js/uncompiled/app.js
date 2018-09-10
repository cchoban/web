window.Vue = require('vue');
window.axios = require('axios');
let Vuex = require('vuex')
let VueDisqus = require('vue-disqus')
import VueTimeago from 'vue-timeago';


// Config
let disqus_shortname = 'test-q7dfbf8l5p'

function is_logged() {
    axios
        .get("/islogged")
        .then(response => {
            if (response.data.auth) {
                return true
            }
        })
        .catch(err => {
            this.loading = false;
            console.log(err);
        });
}

let csrf_token = document.querySelector("meta[name='csrf-token']").getAttribute("content")
const site_url = document.querySelector("meta[name='site_url']").getAttribute("content")
const login_url = document.querySelector('meta[name="login_url"]').getAttribute('content')
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
window.axios.defaults.headers.common['X-CSRFToken'] = csrf_token;
window.logged = is_logged()



const swal = require('sweetalert2')
window.messages = function (message) {
    swal.queue(message)
}

// PackageList.vue Components
Vue.component('PopularPackages', require('../components/PackageListComponents/FeaturedToday.vue'));
Vue.component('PackagesSection', require('../components/PackageListComponents/PackagesSection.vue'));
Vue.component('Pagination', require('../components/PackageListComponents/Pagination.vue'))


// Index
Vue.component('popular-page', require('../components/SinglePage/PopularPackages.vue'))
Vue.component('packages-list', require('../components/PackagesList.vue'));
Vue.component('package-page', require('../components/singlePage.vue'));
Vue.component('category-page', require('../components/SinglePage/CategoryPage.vue'));
Vue.component('Packages', require('../components/SinglePage/Packages.vue'));
Vue.component('Picks', require('../components/SinglePage/EditorPicks.vue'));

;
Vue.component('readMore', require('../components/readMore.vue'));
Vue.component('installCommand', require('../components/installCommandLine.vue'));
Vue.component('apikey', require('../components/api_key.vue'));
Vue.component('search-package', require('../components/Search.vue'));
Vue.component('login', require('../components/Login.vue'));
Vue.component('userAccount', require('../components/userAccount.vue'));
Vue.component('app', require('../components/app.vue'));



Vue.use(Vuex)
Vue.use(VueDisqus)
Vue.use(VueTimeago, {
    name: 'Timeago', // Component name, `Timeago` by default
    locale: null, // Default locale
    locales: {
        'zh-CN': require('date-fns/locale/zh_cn'),
        'ja': require('date-fns/locale/ja'),
    }
})

window.store = new Vuex.Store({
    state: {
        package_page: {
            packages: null,
            count: null,
            nextUrl: null,
            previousUrl: null
        },
        search_key: "",
        isPage: false,
        package: {
            name: "",
            id: null
        },
        history: [],
        reload: true,
        user: user_preferences,
        logged_in: logged_in,
        loading: true,
        api_urls: {
            "packages": `${site_url}/api/packages`,
            'login': `${login_url}`
        },
        title: "",
        disqus_shortname: disqus_shortname
    },
    mutations: {
        logged_in: function (state, isit = false) {
            state.logged_in = isit
        }
    }
})

const app = new Vue({
    el: '#app'
});

require("./vue-directives.js")
