<template>
  <section class="table-flex">
    <header class="table-flex_header">
      <div v-for="(header, index) in headers" :key="index">{{ header }}</div>
    </header>
    <main>
      <div v-for="(row, rowIndex) in rows" :key="rowIndex" class="table-flex_row">
        <div v-for="(column, key) in row" :key="key" class="table-flex_col">
          {{ column }}
        </div>
      </div>
    </main>
  </section>
</template>

<script>
export default {
  props: {
    headers: {
      type: Array,
      required: true
    },
    rows: {
      type: Array
    }
  }
}
</script>
