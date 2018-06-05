import request from '@/utils/request'

export function fetchList(params) {
  return request({
    url: '/api/problem/list',
    method: 'get',
    params
  })
}

export function fetchProblem(name) {
  return request({
    url: '/api/problem',
    method: 'get',
    params: { name }
  })
}

export function putProblem(content) {
  return request({
    url: '/api/problem',
    method: 'put',
    params: { content }
  })
}

export function createArticle(data) {
  return request({
    url: '/article/create',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: '/article/update',
    method: 'post',
    data
  })
}
