import request from '@/utils/request'

export function getList() {
  return request({
    url: '/default/table/list',
    method: 'get'
  })
}

export function getStudent(params) {
  return request({
    url: '/api/stlist',
    method: 'get',
    params
  })
}

export function delStudent(params) {
  return request({
    url: '/api/stlist',
    method: 'delete',
    params
  })
}

export function putStudent(params) {
  return request({
    url: '/api/stlist',
    method: 'put',
    params
  })
}
