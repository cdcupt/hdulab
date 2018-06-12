import request from '@/utils/request'

export function putResult(content) {
  return request({
    url: '/api/result',
    method: 'put',
    params: { content }
  })
}

