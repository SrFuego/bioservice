<template>
<section class="section_home">
  <div class="content_slider">
    <slider animation="fade" height="600px" :interval="16000" :speed="1000" :auto="false" indicators="left" :control-btn="false">
      <slider-item v-for="(i, index) in list" :key="index">
        <div class="slider-bg" :style="i.style">
          <div class="item_bg">
            <h5 v-html="i.text.title"></h5>
            <p>{{i.text.description}}</p>
          </div>
        </div>
      </slider-item>
    </slider>
  </div>
  <div class="content_tri">
    <div class="container">
      <div class="b_text">
        <p>Somos una empresa peruana dedicada a la fabricación de equipos de monitoreo Hidrobiológico, y servicios de Ensayos, Muestreos y Asesoría en temas ambientales, farmacéuticos y de alimentos a los diversos sectores productivos del país y del exterior.</p>
      </div>
      <div class="b_links">
        <div class="link-item">
          <div class="ico-img">
            <img src="/static/img/ico-scientist-w.png">
          </div>
          <h2>{{ (lang=='es')?'NOSOTROS':'ABOUT US' }}</h2>
          <router-link :to="{name: 'nosotros'}"><span>{{ (lang=='es')?'Ver más':'View more' }}</span></router-link>
        </div>
        <div class="link-item">
          <div class="ico-img">
            <img src="/static/img/ico-test-tubes-w.png">
          </div>
          <h2>{{ (lang=='es')?'PRODUCTOS':'PRODUCTS' }}</h2>
          <router-link :to="{name: 'productos'}"><span>{{ (lang=='es')?'Ver más':'View more' }}</span></router-link>
        </div>
        <div class="link-item">
          <div class="ico-img">
            <img src="/static/img/ico-report-w.png">
          </div>
          <h2>{{ (lang=='es')?'SERVICIOS':'SERVICES' }}</h2>
          <router-link :to="{name: 'servicios'}"><span>{{ (lang=='es')?'Ver más':'View more' }}</span></router-link>
        </div>
      </div>
    </div>
  </div>
  <div class="content_up" style="background-image: url(/static/img/bg_index2.jpg)">
    <div class="b_table">
      <div class="b_cell">
        <div class="container">
          <ul class="nav nav_countUp">
            <li>
              <span class="counter-numb">240</span>
              <h5>Clientes</h5>
            </li>
            <li>
              <span class="counter-numb">1003</span>
              <h5>Productos</h5>
            </li>
            <li>
              <span class="counter-numb">198</span>
              <h5>Servicios</h5>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="b_testimonials" v-if="testimonials.length > 0">
    <div class="container">
      <h3 class="title">Testimonios</h3>
      <p class="subti">{{ lang === 'es' ? 'Aquí está lo que algunos de nuestros clientes dicen' : 'Here\'s what some of our customers say'}}</p>
      <template v-if="testimonials.length > 0">
        <div class="slider_testimonials">
          <img class="img_quote" src="/static/img/quote-icon.svg">
          <slider animation="fade" height="200px" :speed="500" :auto="false" indicators="center" :control-btn="false">
            <slider-item v-for="(i, index) in testimonials" :key="index">
              <div class="slider-bg">
                <div class="item_bg">
                  <div class="message">{{ (lang=='es')? i.description : i.description_eng }}</div>
                  <h5 class="name">{{ (lang=='es')? i.name : i.name_eng }}</h5>
                  <p class="area">{{ (lang=='es')? i.area : i.area_eng }}</p>
                </div>
              </div>
            </slider-item>
          </slider>
        </div>
      </template>
    </div>
  </div>
  <div class="b_message_1">
    <div class="b_table">
      <div class="b_cell">
        <div class="container">
          <div class="b_text">
            <h4>CONTÁCTANOS</h4>
            <p>Nos enorgullece construir relaciones duraderas con nuestros proveedores y clientes, cualquiera que sea el mercado.</p>
            <router-link class="btn-viewmore" :to="{name: 'contacto'}">
              <span>{{ (lang=='es')?'CONTÁCTANOS AHORA':'CONTACT US NOW' }}</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>
<script>
  // let IMAGE_BANNER = 'url(/static/img/all/banner_01.jpg)'
  import { Slider, SliderItem } from 'vue-easy-slider'
  export default {
    components: {
      Slider,
      SliderItem
    },
    data () {
      return {
        list: [
          {
            style: {
              backgroundImage: 'url(/static/img/head_index.jpg)'
            },
            text: {
              title: 'Monitoreo Ambiental',
              description: 'Cuidamos el medio ambiente. Cuidamos de ti.'
            }
          },
          {
            style: {
              backgroundImage: 'url(/static/img/index22_bg.png)'
            },
            text: {
              title: 'Fabricación de Equipos e<br>instrumentos a diseño',
              description: 'Usted los imagina, nosotros lo fabricamos.'
            }
          },
          {
            style: {
              backgroundImage: 'url(/static/img/index3.jpg)'
            },
            text: {
              title: 'Centro de Capacitaciones',
              description: 'El conocimiento es poder.'
            }
          },
          {
            style: {
              backgroundImage: 'url(/static/img/index1.jpg)'
            },
            text: {
              title: 'Laboratorio de Análisis',
              description: 'Veracidad y Confidencialidad a tu servicio.'
            }
          }
        ],
        testimonials: []
      }
    },
    created () {
      this.getTestimony()
    },
    mounted () {
      // this.initSlider()
      this.initCountUp()
    },
    methods: {
      getTestimony () {
        this.axios.get('/api/v1/testimonials/').then(success => {
          console.log('testimonios', success.data)
          this.testimonials = success.data
        }).catch(e => {
          console.log('error', e)
        })
      },
      initCountUp () {
        $('.counter-numb').counterUp({
          delay: 100,
          time: 1200
        })
      }
    }
  }
</script>
<style>
  .slider{
    width: 100% !important;
  }
  .slider-item{
    width: 100% !important;
  }
  .slider-item .bg_slider{
    width: 100%;
    height: 600px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
  }
</style>