<template>
<div>
  <header class="header">
    <div class="container">
      <div class="b_left">
        <router-link :to="{name: 'language'}">
          <img class="logo" src="/static/img/logo_old.jpg">
        </router-link>
      </div>
      <div class="b_right">
        <ul class="nav nav_bio">
          <li>
            <router-link :to="{name: 'inicio'}">
              <span>INICIO</span>
            </router-link>
          </li>
          <li>
            <router-link :to="{name: 'nosotros'}">
              <span>NOSOTROS</span>
            </router-link>
          </li>
          <li>
            <router-link :to="{name: 'productos'}">
              <span>PRODUCTOS</span>
            </router-link>
          </li>
          <li>
            <router-link :to="{name: 'servicios'}">
              <span>SERVICIOS</span>
            </router-link>
          </li>
          <li>
            <router-link :to="{name: 'contacto'}">
              <span>CONTACTO</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </header>
  <div class="content-main">
    <router-view></router-view>
  </div>
  <footer class="footer">
    <div class="b_top">
      <div class="text-center">
        <div class="clearfix">
          <ul class="nav nav_contact">
            <li>
              <i class="fa fa-mobile" aria-hidden="true"></i>
              <p>+(51) 94920-6077 &nbsp;/&nbsp; +(51) 94514-3317</p>
            </li>
            <li>
              <i class="fa fa-phone" aria-hidden="true"></i>
              <p>+(01) 575-1856</p>
            </li>
            <li>
              <i class="fa fa-envelope-o" aria-hidden="true"></i>
              <p>ventas@bioserviceclab.com</p>
              <p>logistica@bioserviceclab.com</p>
            </li>
          </ul>
        </div>
        <ul class="nav nav_social">
          <li>
            <a href="" target="_blank">
              <span><i class="fa fa-facebook" aria-hidden="true"></i></span>
            </a>
          </li>
          <li>
            <a href="" target="_blank">
              <span><i class="fa fa-twitter" aria-hidden="true"></i></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="b_bottom">
      <p><a href="" target="_blank">AntonioV</a> © 2015. Privacy Policy</p>
    </div>
  </footer>
</div>
</template>

<script>
  import mixinsGlobals from '../mixins/globals'

  export default {
    name: 'BaseLayout',
    mixins: [mixinsGlobals],
    data () {
      return {
        flagNav: false
      }
    }
  }
</script>
