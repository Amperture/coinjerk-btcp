import axios from 'axios'

const API_URL = process.env.API_URL || '//localhost:5000'


axios.defaults.headers.common['Authorization'] = localStorage.getItem('user-token')

export function userLogin(loginData){
  return axios.post(
    `${API_URL}/auth/login`,
    loginData
  )
}

export function userRegister(newUserData){
  return axios.post(
    `${API_URL}/auth/register`,
    newUserData
  )
}

export function btcPayServerSetup(setupData){
  return axios.post(
    `${API_URL}/api/connectors/btcpay`,
    setupData
  )
}

export function fetchUser(){
  return axios.get(
    `${API_URL}/user`,
  )
}

export function fetchUserPayServer(){
  return axios.get(
    `${API_URL}/user/payserver`,
  )
}
