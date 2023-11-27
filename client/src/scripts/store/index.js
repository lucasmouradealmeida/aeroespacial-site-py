import { createStore } from 'vuex'
import page from './page'

const store = createStore({
  modules: {
    page
  }
})

export default store
