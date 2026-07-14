<template>

  <div class="d-flex flex-column min-vh-100">
  
      <CompanyNavbar />
  
      <div class="container my-5 flex-grow-1">
  
          <h2 class="text-center mb-4">
            Welcome, {{ dashboard.company_name }}
          </h2>
  
          <hr>
  
          <div class="row g-4">
  
              <div class="col-md-3">
  
                  <div class="card text-center shadow">
  
                      <div class="card-body">
  
                          <h5>Total Jobs</h5>
  
                          <h2>{{ dashboard.total_jobs }}</h2>
  
                      </div>
  
                  </div>
  
              </div>
  
              <div class="col-md-3">
  
                  <div class="card text-center shadow">
  
                      <div class="card-body">
  
                          <h5>Total Applications</h5>
  
                          <h2>{{ dashboard.total_applications }}</h2>
  
                      </div>
  
                  </div>
  
              </div>
  
              <div class="col-md-3">
  
                  <div class="card text-center shadow">
  
                      <div class="card-body">
  
                          <h5>Shortlisted</h5>
  
                          <h2>{{ dashboard.shortlisted }}</h2>
  
                      </div>
  
                  </div>
  
              </div>
  
              <div class="col-md-3">
  
                  <div class="card text-center shadow">
  
                      <div class="card-body">
  
                          <h5>Selected</h5>
  
                          <h2>{{ dashboard.selected }}</h2>
  
                      </div>
  
                  </div>
  
              </div>
  
          </div>
  
          <div class="d-flex justify-content-between align-items-center mb-3">

<h4 class="mb-0">My Job Postings</h4>

<button
    class="btn btn-success"
    @click="exportCSV"
>
    Export Application History (CSV)
</button>

</div>

          <table class="table table-bordered">
  
              <thead>
  
                  <tr>
  
                      <th>SL</th>
                      <th>Job Title</th>
                      <th>Deadline</th>
                      <th>Status</th>
                      <th>Applicants</th>
                      <th>Action</th>
  
                  </tr>
  
              </thead>
  
              <tbody>

                <tr v-if="recentJobs.length==0">
                  <td
                  colspan="6"
                  class="text-center text-muted"
                  >
                  No job postings found.
                </td>
              </tr>
  
                  <tr
                      v-for="(job,index) in recentJobs"
                      :key="job.id"
                  >
  
                      <td>{{ index+1 }}</td>
  
                      <td>{{ job.title }}</td>
  
                      <td>{{ job.deadline }}</td>
  
                      <td>
  
                          <span
                              class="badge bg-success"
                              v-if="job.status=='active'"
                          >
                              Active
                          </span>
  
                          <span
                              class="badge bg-secondary"
                              v-else
                          >
                              Inactive
                          </span>
  
                      </td>
  
                      <td>{{ job.applicants }}</td>
  
                      <td>
  
                          <button
                              class="btn btn-primary btn-sm"
                              @click="viewJob(job.id)"
                          >
                              View Details
                          </button>
  
                      </td>
  
                  </tr>
  
              </tbody>
  
          </table>
  
      </div>
  
  </div>
  
  </template>

<script setup>

import CompanyNavbar from "../components/CompanyNavbar.vue"
import { ref, onMounted } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const dashboard = ref({})
const recentJobs = ref([])

const exportCSV = async () => {

try {

    await axios.get(
        "http://127.0.0.1:5000/api/company/export-csv",
        {
            headers: {
                Authorization:
                    "Bearer " + localStorage.getItem("token")
            }
        }
    )

    alert(
        "CSV export started. You will receive an email shortly."
    )

}

catch (err) {

    alert(err.response.data.message)

}

}

async function getDashboard() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            "http://127.0.0.1:5000/api/company/dashboard",

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        dashboard.value = response.data
        recentJobs.value = response.data.recent_jobs

    }

    catch(error) {

        console.log(error.response)

    }

}

function viewJob(id) {

    router.push("/company/job/" + id)

}

onMounted(() => {

    getDashboard()

})

</script>