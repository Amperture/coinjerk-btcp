import Vue from 'vue'
import Vuex from 'vuex'

import auth from '@/store/modules/auth'
import payments from '@/store/modules/payments'
import streamelements from '@/store/modules/streamelements'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    payments,
    streamelements,
  },
})
