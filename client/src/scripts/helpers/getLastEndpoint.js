function getCurrentURL() {
  let url = null
  url = window.location.href.split('/')
  url = url.pop() || parts.pop()
  url = url.substring(0, url.lastIndexOf('.')) || url
  return url
}

export default getCurrentURL
