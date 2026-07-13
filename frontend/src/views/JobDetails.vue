<template>

    <div class="d-flex flex-column min-vh-100">
    
    <AdminNavbar />
    
    <div class="container my-5 flex-grow-1">
    
    <h2 class="text-center mb-4">
    Job Details
    </h2>
    
    <div class="card shadow-sm">
    
    <div class="card-body">
    
    <table class="table">
    
    <tbody>
    
    <tr>
    <th width="30%">Company</th>
    <td>{{ job.company }}</td>
    </tr>
    
    <tr>
    <th>Job Title</th>
    <td>{{ job.title }}</td>
    </tr>
    
    <tr>
    <th>Description</th>
    <td>{{ job.description }}</td>
    </tr>
    
    <tr>
    <th>Eligibility</th>
    <td>{{ job.eligibility }}</td>
    </tr>
    
    <tr>
    <th>Salary</th>
    <td>{{ job.salary }}</td>
    </tr>
    
    <tr>
    <th>Skills Required</th>
    <td>{{ job.skills_req }}</td>
    </tr>
    
    <tr>
    <th>Experience Required</th>
    <td>{{ job.exp_req }}</td>
    </tr>
    
    <tr>
    <th>Deadline</th>
    <td>{{ job.deadline }}</td>
    </tr>
    
    <tr>
    <th>Approval Status</th>
    
    <td>
    
    <span
    class="badge bg-warning"
    v-if="job.approval_status=='pending'"
    >
    Pending
    </span>
    
    <span
    class="badge bg-success"
    v-if="job.approval_status=='approved'"
    >
    Approved
    </span>
    
    <span
    class="badge bg-danger"
    v-if="job.approval_status=='rejected'"
    >
    Rejected
    </span>
    
    </td>
    
    </tr>
    
    <tr>
    
    <th>Current Status</th>
    
    <td>
    
    <span
    class="badge bg-success"
    v-if="job.status=='active'"
    >
    Active
    </span>
    
    <span
    class="badge bg-secondary"
    v-if="job.status=='inactive'"
    >
    Inactive
    </span>
    
    </td>
    
    </tr>
    
    </tbody>
    
    </table>
    
    <div
    class="text-center mt-4"
    v-if="job.approval_status=='pending'"
    >
    
    <button
    class="btn btn-success me-2"
    @click="approveJob"
    >
    Approve
    </button>
    
    <button
    class="btn btn-danger"
    @click="rejectJob"
    >
    Reject
    </button>
    
    </div>
    
    <div class="text-center mt-3">
    
    <button
    class="btn btn-danger"
    @click="deleteJob"
    >
    Delete
    </button>
    
    </div>
    
    <div class="text-center mt-4">
    
    <button
    class="btn btn-secondary"
    @click="$router.push('/admin/jobs')"
    >
    Back
    </button>
    
    </div>
    
    </div>
    
    </div>
    
    </div>
    
    </div>
    
    </template>

<script>
import axios from "axios"
import AdminNavbar from "../components/AdminNavbar.vue"

export default {

  components: {
    AdminNavbar
  },

  data() {

    return {

      job: {}

    }

  },

  mounted() {

    this.fetchJob()

  },

  methods: {

    async fetchJob() {

      const token = localStorage.getItem("token")

      const res = await axios.get(

        `http://127.0.0.1:5000/api/admin/job/${this.$route.params.id}`,

        {

          headers: {

            Authorization: `Bearer ${token}`

          }

        }

      )

      this.job = res.data

    },

    async approveJob() {

      const token = localStorage.getItem("token")

      await axios.put(

        `http://127.0.0.1:5000/api/admin/job/${this.job.id}/approve`,

        {},

        {

          headers: {

            Authorization: `Bearer ${token}`

          }

        }

      )

      this.fetchJob()

    },

    async rejectJob() {

      const token = localStorage.getItem("token")

      await axios.put(

        `http://127.0.0.1:5000/api/admin/job/${this.job.id}/reject`,

        {},

        {

          headers: {

            Authorization: `Bearer ${token}`

          }

        }

      )

      this.fetchJob()

    },

    async deleteJob() {

      if (!confirm("Delete this job permanently?")) {

        return

      }

      const token = localStorage.getItem("token")

      await axios.delete(

        `http://127.0.0.1:5000/api/admin/job/${this.job.id}`,

        {

          headers: {

            Authorization: `Bearer ${token}`

          }

        }

      )

      this.$router.push("/admin/jobs")

    }

  }

}
</script>