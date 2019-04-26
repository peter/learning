/* eslint space-before-function-paren: "off", semi: "off" */
import { trim } from '@/lib/util'
import u from '@/lib/web-util'

// Refresher on cookies here: https://www.quirksmode.org/js/cookies.html
test('parseCookie - takes a cookie string and returns an object with key-value pairs', () => {
  const input = 'ppkcookie1=testcookie; ppkcookie2=another test'
  const output = { ppkcookie1: 'testcookie', ppkcookie2: 'another test' }
  expect(u.parseCookie(input)).toEqual(output)
})

test('parseCookie - returns empty object on null', () => {
  expect(u.parseCookie(null)).toEqual({})
  expect(u.parseCookie(undefined)).toEqual({})
})

test('parseHtmlTags - can extract inner html from script and style tags', () => {
  const script = `
    function foobar () {
      return true;
    }
  `
  const style1 = `
    .foobar {
      font-size: 15px;
    }
  `

  const style2 = `
    .foobar2 {
      font-size: 18px;
    }
  `
  const html = `
    <script id="foobar">
      ${script}
    </script>

    <style>
      ${style1}
    </style>

    <style>
      ${style2}
    </style>
    `

  expect(u.parseHtmlTags(html, 'script').map(trim)).toEqual([script].map(trim))
  expect(u.parseHtmlTags(html, 'style').map(trim)).toEqual([style1, style2].map(trim))
})

test('parseHtmlTags - can deal with no match and null', () => {
  expect(u.parseHtmlTags(null, 'foobar')).toEqual([])
  expect(u.parseHtmlTags('', 'foobar')).toEqual([])
})
