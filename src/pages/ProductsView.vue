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
    <!-- h1>Confesión #1</h1>
    <p>Pa eso!</p -->
    <div class="b_center">
      <div class="container">
        <div class="b_l">
          <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
            <div class="panel" v-for="(item, index) in categories" :key="index">
              <button type="button" class="btn-panel" :class="{'in': index === activeCollapse}" @click="onCollapseIn(index)" :href="'#cate'+index">
                {{ (lang=='es')? item.title : item.eng_title }} <span class="ico-btn"></span>
              </button>
              <div :id="'#cate'+index" class="panel-collapse collapse" :class="{'in': index === activeCollapse}">
                <div class="panel-body">
                  <ul class="nav nav-tabs" role="tablist">
                    <li v-for="(item1, index1) in item.subcategories" :key="index1">
                      <a :class="[(activeSub==item1.slug)?'active':'']" href="#" @click.prevent="selectCategory(item1.slug,item1.products)">{{ (lang=='es')? item1.title : item1.eng_title }}</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="b_r">
          <div class="content_list_products">
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane fade in active" id="div1">
                <template v-if="activeSub==''">
                  <div class="text-center">
                    <h5>SELECCIONE UNA CATEGORIA PARA VER SUS PRODUCTOS</h5>
                  </div>
                </template>
                <template v-else>
                  <template v-if="products.length == 0">
                    <div class="text-center">
                      <h5>{{ (lang=='es')? 'NO HAY PRODUCTOS': 'NO PRODUCTS' }}</h5>
                    </div>
                  </template>
                  <template v-else>
                    <template v-if="flagResponse">
                      <ul class="nav nav_list_products">
                        <li v-for="(product, index) in products" :key="index">
                          <content-placeholders :animated="true">
                            <div class="product--item item--placeholder">
                              <div class="product--inner">
                                <div class="product--head">
                                  <div class="vertical-center">
                                    <div class="b-cell">
                                      <content-placeholders-img />
                                    </div>
                                  </div>
                                </div>
                                <div class="product--body">
                                  <span class="title"><content-placeholders-text :lines="2" /></span>
                                </div>
                              </div>
                            </div>
                          </content-placeholders>
                        </li>
                      </ul>
                    </template>
                    <template v-else>
                      <div class="row">
                        <div class="col-xs-6">
                          Total: {{products.length}}
                        </div>
                        <div class="col-xs-6">
                          
                        </div>
                      </div>
                      <ul class="nav nav_list_products">
                        <li v-for="(product, index) in products" :key="index">
                          <div class="product--item">
                            <router-link class="product--inner" :to="{name: 'producto', params: { id: product.slug }}">
                              <div class="product--head">
                                <div class="vertical-center">
                                  <div class="b-cell">
                                    <img :src="completeUrl(product.image_1)" alt="product">
                                  </div>
                                </div>
                              </div>
                              <div class="product--body">
                                <span class="title">{{ (lang=='es')? product.name : product.eng_name }}<br>{{ (lang=='es')? 'Código: ' : 'Code: ' }}<b>{{product.code}}</b></span>
                                <span class="btn-style"><i class="fa fa-long-arrow-right" aria-hidden="true"></i></span>
                              </div>
                            </router-link>
                          </div>
                        </li>
                      </ul>
                    </template>
                  </template>
                </template>
              </div>
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
    name: 'ProductsView',
    data () {
      return {
        categories: [],
        products: [],
        activeSub: '',
        activeCollapse: 0,
        flagResponse: false
      }
    },
    created () {
      this.getCategories()
    },
    methods: {
      completeUrl (img) {
        return `${BASE_URL}:8000${img}`
      },
      onCollapseIn (index) {
        this.activeCollapse = index
      },
      getCategories () {
        this.axios.get('/api/v1/categories/')
        .then(response => {
          let data = response.data
          this.categories = data
          // console.log(data)
        })
      },
      selectCategory (slug, products) {
        this.flagResponse = true
        this.activeSub = slug
        this.products = []
        this.products = products
        setTimeout(() => {
          this.flagResponse = false
        }, 400)
      }
    }
  }
</script>