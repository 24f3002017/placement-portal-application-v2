<template>
  <div class="container mt-5">

    <div class="row justify-content-center">

      <div class="col-md-7">

        <div class="card shadow">

          <div class="card-body">

            <h2 class="text-center mb-4">
              Company Registration
            </h2>

            <div class="mb-3">
              <label class="form-label">Company Name</label>
              <input
                type="text"
                class="form-control"
                v-model="name"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Email</label>
              <input
                type="email"
                class="form-control"
                v-model="email"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Password</label>
              <input
                type="password"
                class="form-control"
                v-model="password"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">HR Contact</label>
              <input
                type="text"
                class="form-control"
                v-model="hr_contact"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Website</label>
              <input
                type="text"
                class="form-control"
                v-model="website"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Industry</label>
              <input
                type="text"
                class="form-control"
                v-model="industry"
              >
            </div>

            <button
              class="btn btn-warning w-100"
              @click="registerCompany"
            >
              Register
            </button>

            <p class="text-danger mt-3">
              {{ message }}
            </p>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>

import { ref } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const name = ref("")
const email = ref("")
const password = ref("")
const hr_contact = ref("")
const website = ref("")
const industry = ref("")
const message = ref("")

async function registerCompany() {

  try {

    const response = await axios.post(
      "http://127.0.0.1:5000/api/company/register",
      {
        name: name.value,
        email: email.value,
        password: password.value,
        hr_contact: hr_contact.value,
        website: website.value,
        industry: industry.value
      }
    )

    alert(response.data.message)

    router.push("/login")

  }

  catch(error) {

    if(error.response){
      message.value = error.response.data.message
    }
    else{
      message.value = "Server error"
    }

  }

}

</script>