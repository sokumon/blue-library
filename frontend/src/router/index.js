import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import Dashboard from '../views/Dashboard.vue'
import Books from '../views/Books.vue'
import Members from '../views/Members.vue'
import Transaction from '../views/Transaction.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/dashboard',
      name: 'Dashbord',
      component: Dashboard
    },
    {
      path: '/books',
      name:'Books',
      component: Books
    },
    {
      path: '/members',
      name:'Members',
      component: Members
    },
    {
      path: '/transactions',
      name:'Transaction',
      component: Transaction
    }
  ]
})

export default router
