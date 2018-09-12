let mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */
mix.disableSuccessNotifications();
mix.setPublicPath("packages")
.js('packages/static/js/uncompiled/app.js', 'packages/static/js/app.js')
.sass('packages/static/css/uncompiled/main.scss', 'packages/static/css/main.css')

mix.options({
    uglify: false,
})
