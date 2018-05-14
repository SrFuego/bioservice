<template>
<div>
  <div class="section-contact">
    <div class="b_top" style="background-image: url(/static/img/banner_contact.jpg)">
      <div class="b_table">
        <div class="b_cell">
          <h1>{{ (lang=='es')? 'CONTACTO' : 'CONTACT' }}</h1>
        </div>
      </div>
    </div>
    <div class="b_center">
      <div class="container">
        <h3 class="title">DÉJANOS UN MENSAJE</h3>
        <div class="row">
          <div class="col-xs-12">
            <div class="b_form form-left">
              <h5>Contáctanos</h5>
              <div class="form-content">
                <div class="row">
                  <div class="col-xs-12">
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="Nombres y Apellidos" v-model="form1.nombres_apellidos">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-xs-12">
                    <div class="form-group">
                      <input type="email" class="form-control" placeholder="Email" v-model="form1.email">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-xs-12">
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="Teléfono" v-model="form1.telefono">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-xs-12">
                    <div class="form-group">
                      <textarea class="form-control textar" placeholder="Mensaje" v-model="form1.mensaje"></textarea>
                    </div>
                  </div>
                </div>
                <div class="text-left">
                  <ui-button @click="onSubmitContact()" :loading="loadingContact" :disabled="loadingContact" color="primary">{{ (lang=='es')? 'ENVIAR' : 'SEND' }}</ui-button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <br>
        <hr>
        <br>
        <div class="row">
          <div class="col-xs-12">
            <div class="b_form form-right">
              <h5>¿Deseas ser nuestro distribuidor?</h5>
              <div class="form-content">
                <div class="row">
                  <div class="col-xs-12">
                    <div class="form-group">
                      <input type="email" class="form-control" placeholder="Email" v-model="form2.email">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-xs-12 col-sm-6">
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="Razón Social" v-model="form2.razon_social">
                    </div>
                  </div>
                  <div class="col-xs-12 col-sm-6">
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="RUC" v-model="form2.ruc">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-xs-12 col-sm-6">
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="Dirección" v-model="form2.direccion">
                    </div>
                  </div>
                  <div class="col-xs-12 col-sm-6">
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="Teléfono" v-model="form2.telefono">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-xs-12">
                    <div class="form-group">
                      <textarea class="form-control textar" placeholder="Mensaje" v-model="form2.mensaje"></textarea>
                    </div>
                  </div>
                </div>
                <div class="text-right">
                  <ui-button @click="onSubmitDistributor()" :loading="loadingDistributor" :disabled="loadingDistributor">{{ (lang=='es')? 'ENVIAR' : 'SEND' }}</ui-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <ui-modal size="normal" class="modal-contact" ref="message" remove-close-button>
    <div slot="header">
      <span>Mensaje &nbsp;enviado</span>
    </div>
    Su mensaje ha sido enviado correctamente.
    <div slot="footer">
      <ui-button @click="closeModal()" color="shades-white-text">Cerrar</ui-button>
    </div>
  </ui-modal>
</div>
</template>
<script>
  export default {
    name: 'ContactView',
    data () {
      return {
        loadingContact: false,
        loadingDistributor: false,
        form1: {
          nombres_apellidos: '',
          email: '',
          telefono: '',
          mensaje: ''
        },
        form2: {
          ruc: '',
          razon_social: '',
          telefono: '',
          direccion: '',
          mensaje: '',
          email: ''
        }
      }
    },
    methods: {
      openModal () {
        this.$refs.message.open()
      },
      closeModal () {
        this.$refs.message.close()
        this.clearForms()
      },
      clearForms () {
        this.loadingContact = false
        this.loadingDistributor = false
        // form1
        this.form1.nombres_apellidos = ''
        this.form1.email = ''
        this.form1.telefono = ''
        this.form1.mensaje = ''
        // form2
        this.form1.ruc = ''
        this.form1.razon_social = ''
        this.form1.telefono = ''
        this.form1.direccion = ''
        this.form1.mensaje = ''
        this.form1.email = ''
      },
      onSubmitContact () {
        this.loadingContact = true
        this.axios.post('/contact-email/', this.form1)
        .then(response => {
          let data = response.data
          this.loadingContact = false
          this.openModal()
          console.log(data)
        })
      },
      onSubmitDistributor () {
        this.loadingDistributor = true
        this.axios.post('/distributor-email/', this.form2)
        .then(response => {
          let data = response.data
          this.loadingDistributor = false
          this.openModal()
          console.log(data)
        })
      }
    }
  }
</script>
