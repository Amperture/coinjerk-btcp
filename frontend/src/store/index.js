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
        loginLoading(state) {
            state.status = 'loading'
        },
        loginSuccess(state, payload) {
            localStorage.setItem('user-token', payload)
            state.token = payload
            state.status = 'success'
            axios.defaults.headers.common['Authorization'] = payload
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
                    context.commit('loginSuccess', response.data.token)
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
                    console.log(error.data) // eslint-disable-line no-console
                    context.commit('loginFail')
                })
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,
        authStatus: state => state.status,
    },
})
