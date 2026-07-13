<template>

  <AdminNavbar />
  <div class="container mt-5 flex-grow-1">

    <h2 class="text-center mb-4">
      Admin Dashboard
    </h2>

    <div class="row">

      <div class="col-md-4 mb-3">
        <div class="card text-center shadow">
          <div class="card-body">
            <h5>Total Students</h5>
            <h2>{{ students }}</h2>

            <router-link
                to="/admin/students"
                class="btn btn-primary mt-3"
            >
                View Details
            </router-link>

          </div>
        </div>
      </div>

      <div class="col-md-4 mb-3">
        <div class="card text-center shadow">
          <div class="card-body">
            <h5>Total Companies</h5>
            <h2>{{ companies }}</h2>
            
            <router-link
                to="/admin/companies"
                class="btn btn-primary mt-3"
            >
                View Details
            </router-link>

          </div>
        </div>
      </div>

      <div class="col-md-4 mb-3">
        <div class="card text-center shadow">
          <div class="card-body">
            <h5>Total Job Postings</h5>
            <h2>{{ jobs }}</h2>

            <router-link
                to="/admin/jobs"
                class="btn btn-primary mt-3"
            >
                View Details
            </router-link>

          </div>
        </div>
      </div>

      <div class="col-md-4 mb-3">
        <div class="card text-center shadow">
          <div class="card-body">
            <h5>Total Applications</h5>
            <h2>{{ applications }}</h2>

            <router-link
                to="/admin/applications"
                class="btn btn-primary mt-3"
            >
                View Details
            </router-link>

          </div>
        </div>
      </div>

      <div class="col-md-4 mb-3">
        <div class="card text-center shadow">
          <div class="card-body">
            <h5>Total Placements</h5>
            <h2>{{ placements }}</h2>

            <router-link
                to="/admin/placements"
                class="btn btn-primary mt-3"
            >
                View Details
            </router-link>

          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>

import AdminNavbar from "../components/AdminNavbar.vue"
import { ref, onMounted } from "vue"
import axios from "axios"

const students = ref(0)
const companies = ref(0)
const jobs = ref(0)
const applications = ref(0)
const placements = ref(0)

async function getDashboard() {

try {

    const token = localStorage.getItem("token")

    const response = await axios.get(
        "http://127.0.0.1:5000/api/admin/dashboard",
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    )

    students.value = response.data.students
    companies.value = response.data.companies
    jobs.value = response.data.jobs
    applications.value = response.data.applications
    placements.value = response.data.placements

} catch (error) {

    console.log(error.response)
}

}

onMounted(() => {
getDashboard()
})

</script>