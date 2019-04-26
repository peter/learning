/* eslint space-before-function-paren: "off", semi: "off" */
import { empty } from '@/lib/util'

// Takes a cookie string and returns an object with key-value pairs
// May throw an error if the decoding fails.
// See: https://github.com/jkohrman/cookie-parse/blob/master/index.js
export function parseCookie (cookie) {
  if (empty(cookie)) return {}
  return cookie.split(/;\s*/).reduce((acc, item) => {
    const sepIndex = item.indexOf('=')
    const key = item.substring(0, sepIndex)
    const value = decodeURIComponent(item.substring(sepIndex + 1))
    acc[key] = value
    return acc
  }, {})
}

// Given an HTML string and an HTML tag name - return an array with innerHtml for those tags
export function parseHtmlTags (html, tagName) {
  const pattern = `<${tagName}[^>]*>(.*?)<\\/${tagName}>`
  const regex = new RegExp(pattern, 'gs')
  return ((html || '').match(regex) || []).map((tag) => {
    return tag.replace(new RegExp(`<\\/?${tagName}[^>]*>`, 'g'), '')
  })
}

export default {
  parseCookie,
  parseHtmlTags
}
