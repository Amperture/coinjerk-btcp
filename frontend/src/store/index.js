import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

import * as api from '@/api'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('user-token') || '',
    status: '',
    user: {}
  },

  mutations: {
    getUserSuccessCommit(state, payload) {
      state.user = payload
    },
    getUserPayServerSuccessCommit(state, payload) {
      state.user['payserver'] = payload
    },
    loginLoading(state) {
      state.status = 'loading'
    },
    loginSuccess(state, payload) {
      localStorage.setItem('user-token', payload)
      state.token = payload
      state.status = 'success'
    },
    loginFail(state) {
      localStorage.removeItem('user-token')
      state.token = ''
      state.status = 'error'
    },
  },

  actions: {
    login(context, payload){
      context.commit('loginLoading')
      return api.userLogin(payload)
        .then(response => {
          axios.defaults.headers.common['Authorization'] = response.data.token
          context.commit('loginSuccess', response.data.token)
        })
        .catch(error => {
          console.log(error.data) // eslint-disable-line no-console
          context.commit('loginFail')
        })
    },

    register(context, data){
      context.commit('loginLoading')
      return api.userRegister(data)
        .then(response => {
          axios.defaults.headers.common['Authorization'] = response.data.token
          context.commit('loginSuccess', response.data.token)
        })
        .catch(error => {
          console.log(error.data) // eslint-disable-line no-console
          context.commit('loginFail')
        })
    },

    getUserAction(context){
      return api.fetchUser()
        .then(response => {
          context.commit('getUserSuccessCommit', response.data)
        })
        .catch(error => {
          console.log(error.data) // eslint-disable-line no-console
          context.commit('loginFail')
        })
    },

    getUserPayServerAction(context){
      return api.fetchUserPayServer()
        .then(response => {
          context.commit('getUserPayServerSuccessCommit', response.data)
        })
        .catch(error => {
          console.log(error.data) // eslint-disable-line no-console
          context.commit('loginFail')
        })
    },

    btcpaySetup(context, data){
      return api.btcPayServerSetup(data)
        .then(response => {
          context.commit('loginSuccess', response.data.token)
        })
        .catch(error => {
          console.log(error) // eslint-disable-line no-console
        })
    }
  },
  getters: {
    isAuthenticated: state => !!state.token,
    authStatus: state => state.status,
  },
})
