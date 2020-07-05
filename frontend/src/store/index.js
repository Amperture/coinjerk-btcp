import Vue from 'vue'
import Vuex from 'vuex'

import auth from '@/store/modules/auth'
import btcpay from '@/store/modules/btcpay'
import streamelements from '@/store/modules/streamelements'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    btcpay,
    streamelements,
  },
})
