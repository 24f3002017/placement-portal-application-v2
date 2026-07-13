<template>

  <HomeNavbar />

    <div class="container mt-5 flex-grow-1">
  
      <div class="row justify-content-center">
  
        <div class="col-md-5">
  
          <div class="card shadow">
  
            <div class="card-body">
  
              <h3 class="text-center mb-4">
                Login
              </h3>
  
              <div class="mb-3">
  
                <label class="form-label">
                  Email
                </label>
  
                <input
                  type="email"
                  class="form-control"
                  v-model="email"
                >
  
              </div>
  
              <div class="mb-3">
  
                <label class="form-label">
                  Password
                </label>
  
                <input
                  type="password"
                  class="form-control"
                  v-model="password"
                >
  
              </div>
  
              <button
                class="btn btn-primary w-100"
                @click="login"
              >
                Login
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

  import HomeNavbar from "../components/HomeNavbar.vue"
  import { ref } from "vue"
  import axios from "axios"
  import { useRouter } from "vue-router"
  
  
  const email = ref("")
  const password = ref("")
  const message = ref("")

const router = useRouter()

async function login(){

    try{

        const response = await axios.post(
            "http://127.0.0.1:5000/api/login",
            {
                email: email.value,
                password: password.value
            }
        )

        localStorage.setItem("token", response.data.token)
        localStorage.setItem("role", response.data.role)

        if(response.data.role === "admin"){
            router.push("/admin-dashboard")
        }

        else if(response.data.role === "student"){
            router.push("/student-dashboard")
        }

        else{
            router.push("/company-dashboard")
        }

    }

    catch(error){

      if(error.response){
        message.value = error.response.data.message
      }
      else{
        message.value = "Server error"
      }

    }

}
  
  </script>