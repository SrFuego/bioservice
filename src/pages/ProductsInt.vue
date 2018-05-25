<template>
<div>
  <div class="section-products">
    <div class="section__banner" style="background-image: url(/static/img/banner_products.jpg)">
      <div class="b_table">
        <div class="b_cell">
          <h1>{{ (lang=='es')? 'PRODUCTOS' : 'PRODUCTS' }}</h1>
        </div>
      </div>
    </div>
    <div class="b_center">
      <div class="container">
        <div class="row">
          <div class="col-xs-12 col-md-6">
            <div class="content_detail">
              <h3>{{ (lang=='es')? product.name : product.eng_name }}</h3>
              <h5>{{ (lang=='es')? 'Código: ' : 'Code: ' }} {{ product.code }}</h5>
              <p>{{ (lang=='es')? product.description : product.eng_description }}</p>
              <router-link class="btn-back" :to="{name: 'productos'}"><i class="fa fa-angle-left" aria-hidden="true"></i>{{ (lang=='es')? 'Regresar: ' : 'Back: ' }}</router-link>
            </div>
            <br><br>
          </div>
          <div class="col-xs-12 col-md-6">
            <div class="content_slider">
              <span class="cr1"></span>
              <span class="cr2"></span>
              <span class="cr3"></span>
              <span class="cr4"></span>
              <ul class="bxslider">
                <li v-if="!isEmpty(product.image_1)">
                  <img :src="completeUrl(product.image_1)"/>
                </li>
                <li v-if="!isEmpty(product.image_2)">
                  <img :src="completeUrl(product.image_2)"/>
                </li>
                <li v-if="!isEmpty(product.image_3)">
                  <img :src="completeUrl(product.image_3)"/>
                </li>
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
  import {BASE_URL} from '../utils/variables'
  export default {
    name: 'ProductsInt',
    beforeRouteEnter (to, from, next) {
      // Código que responde al cambio
      // no olvides ejecutar next()
      next(vm => {
        // console.log(to.params)
        vm.subCategory = to.params.id
        vm.getProducts()
      })
    },
    data () {
      return {
        subCategory: '',
        product: {}
      }
    },
    mounted () {
      // this.initSlider()
    },
    methods: {
      isEmpty (obj) {
        if (obj == null) return true

        if (obj.length > 0) return false
        if (obj.length === 0) return true

        if (typeof obj !== 'object') return true

        for (var key in obj) {
          if (hasOwnProperty.call(obj, key)) return false
        }
        return true
      },
      completeUrl (img) {
        return `${BASE_URL}:8000${img}`
      },
      getProducts () {
        this.axios.get(`/api/v1/products/${this.subCategory}/`)
        .then(response => {
          let data = response.data
          this.product = data
          this.initSlider()
          // console.log(data)
        })
      },
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