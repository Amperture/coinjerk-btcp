import Vue from 'vue'
import Vuex from 'vuex'

import * as api from '@/api'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {}

  },

  mutations: {
    setUser(state, payload) {
      console.log("is the exception in the mutation?")
      state.user = payload.user
    }

  },

  actions: {

    login(context, data){
      return api.userLogin(data)
        .then(response => {
          console.log("action succ")
          console.log(response)
          context.commit('setUser', { user: response.user })
        })
        .catch(error => {
          throw error;
        })
    },

  },
  getters: {

  },
})
