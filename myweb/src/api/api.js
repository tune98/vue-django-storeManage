import http from './http'
import axios from 'axios'

// get请求
export function getAPI (url, params = null) {
  return http.get(url, params)
}

// post请求
export function postAPI (url, params = null) {
  return axios.post(url, params)
}

// put 请求
export function putAPI (url, params = null) {
  return http.put(url, params)
}

// delete 请求
export function deleteAPI (url, params = null) {
  return http.delete(url, params)
}