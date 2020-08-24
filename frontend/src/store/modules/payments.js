import api from '@/api'

const state = {
  server_host: '',
}

const getters = {
}

const actions = {

  btcpaySetupAction(context, data){
    return api.payments.btcPayServerSetup(data)
      .then(response => {
        context.commit('loginSuccess', response.data.token)
      })
      .catch(error => {
        console.log(error) // eslint-disable-line no-console
      })
  },

  getUserPaymentServer(context, data){
    return api.payments.fetchUserPaymentServer(data.username)
  },
}

const mutations = {
  getUserPayServerSuccessCommit(state, payload) {
    state['server_host'] = payload['server_host']
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
