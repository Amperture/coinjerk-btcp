import axios from 'axios'
import * as auth from '@/api/auth'
import * as payments from '@/api/payments'
import * as alerts from '@/api/alerts'

// eslint-disable-next-line no-unused-vars
export const API_URL = '//localhost:5000'

axios.defaults.headers.common['Authorization'] =
  localStorage.getItem('user-token')

export default {
  auth,
  payments,
  alerts
}
