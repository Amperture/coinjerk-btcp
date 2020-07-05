import axios from 'axios'

import { API_URL } from '@/api'

export function userLogin(loginData){
  return axios.post(
    `${API_URL}/auth/login`,
    loginData
  )
}

export function userRegister(newUserData) {
  return axios.post(
    `${API_URL}/auth/register`,
    newUserData
  )
}

export function fetchUser(){
  return axios.get(
    `${API_URL}/user`,
  )
}
