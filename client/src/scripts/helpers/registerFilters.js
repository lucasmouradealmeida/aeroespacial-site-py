import * as filters from '@/helpers/filters'

export default function registerFilters(app) {
  console.log(filters)
  Object.keys(filters).forEach((filter) => {
    app.config.globalProperties.$filters[filter] = filters[filter]
  })
}
