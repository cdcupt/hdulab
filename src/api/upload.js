import request from '@/utils/request'

export function getWork(params) {
  return request({
    url: '/api/problem/list',
    method: 'get',
    params
  })
}

export function delWork(params) {
  return request({
    url: '/api/problem',
    method: 'delete',
    params
  })
}

export function putWork(params) {
  return request({
    url: '/api/problem',
    method: 'put',
    params
  })
}
