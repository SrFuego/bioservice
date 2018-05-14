// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// axios
import axios from './http'
// ui
import Ui from './ui'
import VueContentPlaceholders from 'vue-content-placeholders'
// router
import router from './router'
import Globals from './mixins/globals'
// use- mixins
Vue.use(Ui)
Vue.use(VueContentPlaceholders)
Vue.mixin(Globals)
Vue.config.productionTip = false
import './sass/app.scss'
Vue.prototype.axios = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  template: '<App/>',
  components: { App }
})
