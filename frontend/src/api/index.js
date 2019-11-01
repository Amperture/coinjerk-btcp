import axios from 'axios'

const API_URL = process.env.API_URL

export function userLogin(loginData){
  return axios.post(
    `${BASE_URL}/auth/login/`,
    loginData
  )
}

export function userRegister(newUserData){
  return axios.post(
    `${BASE_URL}/auth/register/`,
    newUserData
  )
}
