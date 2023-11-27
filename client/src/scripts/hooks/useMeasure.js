import { debounce, throttle } from 'lodash-es'
import { onUnmounted, reactive, shallowRef, watchEffect } from 'vue'

const defaultOption = {
  wait: 333,
  type: 'debounce'
}

export default function useMeasure(...args) {
  const hasParamRef = 'value' in args?.[0]
  let option
  if (hasParamRef) option = args?.[1]
  else option = args?.[0]
  const { wait, type, callback } = { ...defaultOption, ...option }
  const targetRef = hasParamRef ? args[0] : shallowRef(null)
  const rect = reactive({ left: 0, top: 0, right: 0, bottom: 0, width: 0, height: 0, x: 0, y: 0 })

  const observerFunc = () => {
    const domRect = targetRef.value.getBoundingClientRect()
    rect.left = domRect.left
    rect.top = domRect.top
    rect.right = domRect.right
    rect.bottom = domRect.bottom
    rect.width = domRect.width
    rect.height = domRect.height
    rect.x = domRect.x
    rect.y = domRect.y
    callback?.()
  }
  let execFunc = null

  let ro = null
  const clearRo = () => {
    if (execFunc) window.removeEventListener('resize', execFunc)
    if (!ro) return
    ro.disconnect()
    ro = null
  }

  watchEffect(() => {
    if (!targetRef.value) return
    clearRo()

    execFunc = observerFunc
    if (type === 'throttle' && wait >= 4) execFunc = throttle(execFunc, wait)
    else if (type === 'debounce' && wait >= 4) execFunc = debounce(execFunc, wait)
    window.addEventListener('resize', execFunc)
    ro = new ResizeObserver(execFunc)
    ro.observe(targetRef.value)
  })

  onUnmounted(clearRo)

  if (hasParamRef) return rect
  return [targetRef, rect]
}
