export default {
  namespaced: true,
  state: {
    pageContent: null
  },
  mutations: {
    SET_PAGE_CONTENT(state, content) {
      state.pageContent = content
    }
  },
  actions: {
    setPageContent({ commit }, content) {
      commit('SET_PAGE_CONTENT', content)
    }
  },
  getters: {
    getPageContent: (state) => state.pageContent
  }
}
