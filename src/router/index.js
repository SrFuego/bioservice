import Vue from 'vue'
import Router from 'vue-router'
import LanguageView from '@/pages/LanguageView'
import BaseLayout from '@/pages/BaseLayout'
import HomeView from '@/pages/HomeView'
import AboutView from '@/pages/AboutView'
import ContactView from '@/pages/ContactView'
import ProductsView from '@/pages/ProductsView'
import ProductsInt from '@/pages/ProductsInt'
import ServicesView from '@/pages/ServicesView'
import ServicesInt from '@/pages/ServicesInt'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'language',
      component: LanguageView
    },
    {
      path: '/',
      name: 'base',
      component: BaseLayout,
      children: [
        {
          path: '/home',
          name: 'inicio',
          component: HomeView
        },
        {
          path: '/aboutus',
          name: 'nosotros',
          component: AboutView
        },
        {
          path: '/contact',
          name: 'contacto',
          component: ContactView
        },
        {
          path: '/products',
          name: 'productos',
          component: ProductsView
        },
        {
          path: '/products/:id',
          name: 'producto',
          component: ProductsInt
        },
        {
          path: '/services',
          name: 'servicios',
          component: ServicesView
        },
        {
          path: '/services/:id',
          name: 'servicio',
          component: ServicesInt
        }
      ]
    }
  ]
})
