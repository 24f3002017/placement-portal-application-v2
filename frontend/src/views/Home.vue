<template>
  <HomeNavbar />
    <div class="container mt-5 flex-grow-1 text-center">
    <h1>Welcome to Placement Portal</h1>

    <router-link to="/login" class="btn btn-primary m-2">
      Login
    </router-link>

    <router-link to="/student-register" class="btn btn-success m-2">
      Student Register
    </router-link>

    <router-link to="/company-register" class="btn btn-warning m-2">
      Company Register
    </router-link>
  </div>
</template>

<script setup>

import HomeNavbar from "../components/HomeNavbar.vue"

</script>