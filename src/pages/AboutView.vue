<template>
<div>
  <div class="section-aboutus">
    <div class="b_top" style="background-image: url(/static/img/banner_us.jpg)">
      <div class="b_table">
        <div class="b_cell">
          <h1>{{ (lang=='es')? 'NOSOTROS' : 'ABOUT US' }}</h1>
        </div>
      </div>
    </div>
    <div class="b_center">
      <div class="b_text_conoc">
        <img class="ico-img" src="/static/img/molecule.png">
        <h2>{{ lang == 'es' ? about.title : about.eng_title }}</h2>
        <p>{{ lang == 'es' ? about.content : about.eng_content }}</p>
      </div>
      <div class="b_mivi">
        <div class="b_left">
          <div class="b_table">
            <div class="b_cell">
              <div class="b_text">
                <h2>{{ lang == 'es' ? mision.title : mision.eng_title }}</h2>
                <p>{{ lang == 'es' ? mision.content : mision.eng_content }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="b_right">
          <div class="b_table">
            <div class="b_cell">
              <div class="b_text">
                <h2>{{ lang == 'es' ? vision.title : vision.eng_title }}</h2>
                <p>{{ lang == 'es' ? vision.content : vision.eng_content }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="b_valor">
        <h2>{{ lang == 'es' ? valores.title : valores.eng_title }}</h2>
        <p>{{ lang == 'es' ? valores.content : valores.eng_content }}</p>
      </div>
    </div>
    <!-- div class="b_message" style="background-image: url(/static/img/head_index2.jpg)">
      <div class="b_table">
        <div class="b_cell">
          <div class="b_text">
          </div>
        </div>
      </div>
    </div -->
  </div>
</div>
</template>

<script>
  export default {
    name: 'AboutView',
    data () {
      return {
        about: {},
        mision: {},
        vision: {},
        valores: {}
      }
    },
    created () {
      this.getAbout()
    },
    methods: {
      getAbout () {
        this.axios.get('/api/v1/texts/')
        .then(response => {
          let data = response.data
          data.forEach(val => {
            if (val.slug === 'quienes-somos') {
              this.about = val
            } else if (val.slug === 'mision') {
              this.mision = val
            } else if (val.slug === 'vision') {
              this.vision = val
            } else if (val.slug === 'valores') {
              this.valores = val
            }
          })
          console.log(response)
        })
      }
    }
  }
</script>