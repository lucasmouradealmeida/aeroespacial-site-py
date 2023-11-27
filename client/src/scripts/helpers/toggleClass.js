const toggleClass = (element, className, shouldAdd) => {
  if (shouldAdd) element?.classList.add(className)
  else element?.classList.remove(className)
}

export default toggleClass
