import { createApp } from 'vue'
import { default as store } from '@/build/global'
import { hasElement } from '@/helpers'

const addModule = (ref, Module) => {
  const isThere = hasElement(ref)

  if (isThere) {
    const app = createApp(Module)
    app.use(store)
    app.mount(ref)
  }
}

export default addModule
