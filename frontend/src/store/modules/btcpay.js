import api from '@/api'

const state = {
  server_host: '',
}

const getters = {
}

const actions = {

  btcpaySetupAction(context, data){
    return api.btcpay.btcPayServerSetup(data)
      .then(response => {
        context.commit('loginSuccess', response.data.token)
      })
      .catch(error => {
        console.log(error) // eslint-disable-line no-console
      })
  },

  getBTCPayServer(context){
    return api.btcpay.fetchUserPayServer()
      .then(response => {
        context.commit('getUserPayServerSuccessCommit', response.data)
      })
      .catch(error => {
        console.log(error.data) // eslint-disable-line no-console
      })
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
