import Vue from 'vue'
import Vuex from 'vuex'

import auth from '@/store/modules/auth'
import payments from '@/store/modules/payments'
import alerts from '@/store/modules/alerts'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    payments,
    alerts,
  },
})
