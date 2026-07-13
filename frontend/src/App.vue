<template>
  <div class="d-flex flex-column min-vh-100">

    <RouterView />

    <Footer />

  </div>
</template>

<script setup>
import { RouterView } from "vue-router"
import Footer from "./components/Footer.vue"
</script>