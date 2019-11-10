import axios from 'axios'

const API_URL = process.env.API_URL || '//localhost:5000'

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
