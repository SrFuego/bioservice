<template>
<div>
  <div class="section-services">
    <div class="section__banner" style="background-image: url(/static/img/banner_service.jpg)">
      <div class="b_table">
        <div class="b_cell">
          <h1>{{ (lang=='es')? 'SERVICIOS' : 'SERVICES' }}</h1>
        </div>
      </div>
    </div>
    <div class="b_center">
      <div class="container">
        <div class="content_list_products">
          <ul class="nav nav_list_products">
            <li>
              <div class="item_product">
                <router-link :to="{name: 'servicio', params: { id: 1 }}">
                  <div class="head_item">
                    <img src="/static/img/servicio1.jpg">
                  </div>
                  <div class="body_item">
                    <span class="title">TITULO DEL SERVICIO 1</span>
                    <span class="btn-style"><i class="fa fa-long-arrow-right" aria-hidden="true"></i></span>
                  </div>
                </router-link>
              </div>
            </li>
            <li>
              <div class="item_product">
                <router-link :to="{name: 'servicio', params: { id: 1 }}">
                  <div class="head_item">
                    <img src="/static/img/servicio2.jpg">
                  </div>
                  <div class="body_item">
                    <span class="title">TITULO DEL SERVICIO 2</span>
                    <span class="btn-style"><i class="fa fa-long-arrow-right" aria-hidden="true"></i></span>
                  </div>
                </router-link>
              </div>
            </li>
            <li>
              <div class="item_product">
                <router-link :to="{name: 'servicio', params: { id: 1 }}">
                  <div class="head_item">
                    <img src="/static/img/diagnostic.jpg">
                  </div>
                  <div class="body_item">
                    <span class="title">TITULO DEL SERVICIO 3</span>
                    <span class="btn-style"><i class="fa fa-long-arrow-right" aria-hidden="true"></i></span>
                  </div>
                </router-link>
              </div>
            </li>
            <li>
              <div class="item_product">
                <router-link :to="{name: 'servicio', params: { id: 1 }}">
                  <div class="head_item">
                    <img src="/static/img/about.jpg">
                  </div>
                  <div class="body_item">
                    <span class="title">TITULO DEL SERVICIO 4</span>
                    <span class="btn-style"><i class="fa fa-long-arrow-right" aria-hidden="true"></i></span>
                  </div>
                </router-link>
              </div>
            </li>
            <li>
              <div class="item_product">
                <router-link :to="{name: 'servicio', params: { id: 1 }}">
                  <div class="head_item">
                    <img src="/static/img/message.jpg">
                  </div>
                  <div class="body_item">
                    <span class="title">TITULO DEL SERVICIO 5</span>
                    <span class="btn-style"><i class="fa fa-long-arrow-right" aria-hidden="true"></i></span>
                  </div>
                </router-link>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    name: 'ServiceView',
    route: {
      data (transition) {
        this.deviceCode = transition.to.params.deviceCode
      }
    },
    data () {
      return {
        services: []
      }
    },
    created () {
      // this.getServices()
    },
    methods: {
      // getServices () {
      //   this.$http({
      //     url: this.apiURL + '/api/v1/services/',
      //     method: 'GET'
      //   }).then(function(success){
      //     console.log("success",success)
      //     this.services = success.data
      //   }, (error) {
      //     console.log("error",error)
      //   })
      // }
    }
  }
</script>