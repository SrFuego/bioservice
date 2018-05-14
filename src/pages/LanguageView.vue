<template>
  <div class="section_index">
    <div class="bg_black"></div>
    <!-- ul id="sliderIndex" class="bxslider bx_index">
      <li>
        <div class="bg_slider" style="background-image: url(./dist/img/slider1.jpg)"></div>
      </li>
      <li>
        <div class="bg_slider" style="background-image: url(./dist/img/slider2.jpg)"></div>
      </li>
      <li>
        <div class="bg_slider" style="background-image: url(./dist/img/slider3.jpg)"></div>
      </li>
    </ul -->
    <div class="bg_image"></div>
    <div class="b_top clearfix">
      <img class="logo_index" src="/static/img/logo_old.jpg">
    </div>
    <div class="b_table">
      <div class="b_cell">
        <div class="btn_go">
          <!-- img class="logo_index" src="./dist/img/logo.png" alt="" -->
          <!-- h5>Bienvenidos a <br>Sinchimarka Laraos</h5 -->
          <ul class="nav nav_links">
            <!-- li><button class="btn-language" @click="selectLanguage('eng')"><span>ENTER</span></button></li -->
            <li><button class="btn-language" @click="selectLanguage('esp')"><span>{{lang==='es'?'Entrar':'Enter'}}</span></button></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="b_address">
      <ul class="nav nav_socials">
        <li><a href="https://www.facebook.com/bioserviceclab/" target="_blank"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
      </ul>
      <p>Lima</p>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'LanguageView',
    data () {
      return {
      }
    },
    mounted () {
      // this.initSlider()
    },
    methods: {
      initSlider () {
        this.$nextTick(() => {
          $('#sliderIndex').bxSlider({
            mode: 'fade',
            captions: false,
            pager: false,
            controls: false,
            auto: true,
            pause: 4000,
            easing: 'ease-in-out'
          })
        })
      },
      selectLanguage (_lang) {
        this.$router.push({ name: 'inicio' })
        // if (_lang === 'eng') {
        //   window.localStorage.setItem('lang','en')
        // } else if (_lang === 'esp') {
        //   window.localStorage.setItem('lang','es')
        // }
      }
    }
  }
</script>