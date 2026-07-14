<template>
  <div class="d-flex flex-column min-vh-100">

    <StudentNavbar />

    <div class="container my-5 flex-grow-1">

      <h2 class="mb-1">
        Hi, {{ student.first_name }} 👋
      </h2>

      <p class="text-muted mb-4">
        Welcome back to the Placement Portal.
      </p>

      <div class="row">

        <div class="col-md-4 mb-4">

          <div class="card shadow h-100">

            <div class="card-header bg-dark text-white">
              Dashboard Summary
            </div>

            <div class="card-body">

              <p><strong>Available Jobs:</strong> {{ summary.available_jobs }}</p>

              <p><strong>Applied Jobs:</strong> {{ summary.applied_jobs }}</p>

              <p><strong>Selected:</strong> {{ summary.selected }}</p>

              <p><strong>Rejected:</strong> {{ summary.rejected }}</p>

            </div>

          </div>

        </div>

        <div class="col-md-8 mb-4">

          <div class="card shadow h-100">

            <div class="card-header bg-warning">
              🔔 Notifications
            </div>

            <div class="card-body">

              <div
                v-if="notifications.length==0"
                class="text-muted"
              >
                No notifications.
              </div>

              <div
                v-for="notification in notifications"
                :key="notification.id"
                class="alert alert-light border"
              >
                {{ notification.message }}
              </div>

            </div>

          </div>

        </div>

      </div>


      <div class="row mb-3">

        <div class="mb-2 text-end">

<button

    class="btn btn-success"

    @click="exportCSV"

>

    Export Application History (CSV)

</button>

          </div>

        <div class="col-md-8">

          <input
            class="form-control"
            placeholder="Search company or job..."
            v-model="search"
            @input="fetchJobs"
          >

        </div>

        <div class="col-md-4">

          <select
            class="form-select"
            v-model="filter"
            @change="fetchJobs"
          >

            <option value="">All Jobs</option>
            <option value="not_applied">Not Applied</option>
            <option value="applied">Applied</option>
            <option value="shortlisted">Shortlisted</option>
            <option value="selected">Selected</option>
            <option value="rejected">Rejected</option>

          </select>



        </div>

      </div>

      <table class="table table-striped table-hover">

        <thead>

          <tr>

            <th>Company</th>
            <th>Position</th>
            <th>Salary</th>
            <th>Deadline</th>
            <th>Action</th>

          </tr>

        </thead>

        <tbody>

          <tr
            v-for="job in jobs"
            :key="job.id"
          >

            <td>{{ job.company }}</td>

            <td>{{ job.title }}</td>

            <td>{{ job.salary }}</td>

            <td>{{ job.deadline }}</td>

            <td>

              <button
                class="btn btn-primary btn-sm"
                @click="$router.push('/student/job/' + job.id)"
              >
                View
              </button>

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>

</template>

<script setup>

import StudentNavbar from "../components/StudentNavbar.vue"
import { ref, onMounted } from "vue"
import axios from "axios"

const student = ref({})

const summary = ref({})

const notifications = ref([])

const jobs = ref([])

const search = ref("")

const filter = ref("")

async function fetchDashboard() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            "http://127.0.0.1:5000/api/student/dashboard",

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        student.value = response.data.student

        summary.value = response.data.summary

        notifications.value = response.data.notifications

    }

    catch(error) {

        console.log(error.response)

    }

}

async function fetchJobs() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            "http://127.0.0.1:5000/api/student/jobs",

            {

                headers: {

                    Authorization: `Bearer ${token}`

                },

                params: {

                    search: search.value,

                    filter: filter.value

                }

            }

        )

        jobs.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

async function exportCSV(){

try{

    const token = localStorage.getItem("token")

    const response = await axios.post(

        "http://127.0.0.1:5000/api/student/export-csv",

        {},

        {

            headers:{

                Authorization:`Bearer ${token}`

            }

        }

    )

    alert(response.data.message)

}

catch(error){

    if(error.response){

        alert(error.response.data.message)

    }

    else{

        alert("Server Error")

    }

}

}

onMounted(() => {

    fetchDashboard()

    fetchJobs()

})

</script>

