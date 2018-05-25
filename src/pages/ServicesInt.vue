<template>
<div>
  <div class="section-products">
    <div class="section__banner" style="background-image: url(/static/img/banner_service.jpg)">
      <div class="b_table">
        <div class="b_cell">
          <h1>{{ (lang=='es')? 'SERVICIOS' : 'SERVICES' }}</h1>
        </div>
      </div>
    </div>
    <div class="b_center">
      <div class="container">
        <div class="row">
          <div class="col-xs-12 col-md-6">
            <div class="content_detail">
              <h3>Nombre del servicio</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
              tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
              quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
              consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
              cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
              proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
              tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
              quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
              consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
              cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
              proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
              <router-link class="btn-back" :to="{name: 'servicios', params: { id: 1 }}"><i class="fa fa-angle-left" aria-hidden="true"></i>Atras</router-link>
            </div>
          </div>
          <div class="col-xs-12 col-md-6">
            <div class="content_slider">
              <span class="cr1"></span>
              <span class="cr2"></span>
              <span class="cr3"></span>
              <span class="cr4"></span>
              <ul class="bxslider">
                <li><img src="/static/img/productos/producto3.jpg"/></li>
                <li><img src="/static/img/productos/producto2.jpg"/></li>
                <li><img src="/static/img/productos/producto5.jpg"/></li>
              </ul>
              <span class="control-slider ctrl-left" id="slider-prev"></span>
              <span class="control-slider ctrl-right" id="slider-next"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    name: 'ServiceInt',
    /*
    route:{
      data: function(transition){
        this.deviceCode = transition.to.params.deviceCode;
      }
    },
    */
    data () {
      return {
      }
    },
    mounted () {
      this.initSlider()
    },
    methods: {
      initSlider () {
        this.$nextTick(() => {
          $('.bxslider').bxSlider({
            mode: 'fade',
            captions: false,
            controls: true,
            pager: false,
            auto: true,
            nextSelector: '#slider-next',
            prevSelector: '#slider-prev',
            nextText: '<i class="fa fa-chevron-right" aria-hidden="true"></i>',
            prevText: '<i class="fa fa-chevron-left" aria-hidden="true"></i>'
          })
        })
      }
    }
  }
</script>