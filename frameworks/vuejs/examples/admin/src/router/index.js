import Vue from 'vue'
import Router from 'vue-router'
import guards from '@/router/guards'
import Home from '@/components/Home'
import Login from '@/components/Login'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
  ]
})

guards(router)

export default router
