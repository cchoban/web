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

// mix.sass('resources/assets/sass/styles.scss', 'public/tjejerfragor/css'),
mix.setPublicPath("packages")
mix.disableSuccessNotifications();
mix.js('packages/static/js/uncompiled/app.js', 'packages/static/js/app.js')

