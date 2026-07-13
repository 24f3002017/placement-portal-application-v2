<template>
    <div class="d-flex flex-column min-vh-100">
  
      <AdminNavbar />
  
      <div class="container my-5 flex-grow-1">
  
        <h2 class="text-center mb-4">Student Details</h2>
  
        <div class="card shadow-sm">
  
          <div class="card-body">
  
            <table class="table">
  
              <tbody>
  
                <tr>
                  <th width="30%">Student Name</th>
                  <td>{{ student.first_name }} {{ student.last_name }}</td>
                </tr>
  
                <tr>
                  <th>Roll No</th>
                  <td>{{ student.roll_no }}</td>
                </tr>
  
                <tr>
                  <th>Email</th>
                  <td>{{ student.email }}</td>
                </tr>
  
                <tr>
                  <th>CGPA</th>
                  <td>{{ student.cgpa }}</td>
                </tr>
  
                <tr>
                  <th>Skills</th>
                  <td>{{ student.skills }}</td>
                </tr>
  
                <tr>
                  <th>Experience</th>
                  <td>{{ student.experience }}</td>
                </tr>
  
                <tr>
                  <th>Education</th>
                  <td>{{ student.education }}</td>
                </tr>
  
                <tr>
                  <th>Resume</th>
                  <td>{{ student.resume }}</td>
                </tr>
  
                <tr>
                  <th>Status</th>
  
                  <td>
  
                    <span
                      class="badge bg-success"
                      v-if="student.status=='active'"
                    >
                      Active
                    </span>
  
                    <span
                      class="badge bg-warning text-dark"
                      v-if="student.status=='inactive'"
                    >
                      Inactive
                    </span>
  
                    <span
                      class="badge bg-dark"
                      v-if="student.status=='blacklisted'"
                    >
                      Blacklisted
                    </span>
  
                  </td>
  
                </tr>
  
              </tbody>
  
            </table>
  
            <div class="text-center mt-3">
  
              <button
                class="btn btn-warning me-2"
                @click="deactivateStudent"
                v-if="student.status=='active'"
              >
                Deactivate
              </button>
  
              <button
                class="btn btn-success me-2"
                @click="activateStudent"
                v-if="student.status=='inactive'"
              >
                Activate
              </button>
  
              <button
                class="btn btn-dark me-2"
                @click="blacklistStudent"
                v-if="student.status!='blacklisted'"
              >
                Blacklist
              </button>
  
              <button
                class="btn btn-danger"
                @click="deleteStudent"
                v-if="student.status!='blacklisted'"
              >
                Delete
              </button>
  
            </div>
  
            <div class="text-center mt-4">
  
              <button
                class="btn btn-secondary"
                @click="$router.push('/admin/students')"
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
  
        student: {}
  
      }
  
    },
  
    mounted() {
  
      this.fetchStudent()
  
    },
  
    methods: {
  
      async fetchStudent() {
  
        const token = localStorage.getItem("token")
  
        const res = await axios.get(
  
          `http://127.0.0.1:5000/api/admin/student/${this.$route.params.id}`,
  
          {
  
            headers: {
  
              Authorization: `Bearer ${token}`
  
            }
  
          }
  
        )
  
        this.student = res.data
  
      },
  
      async activateStudent() {
  
        const token = localStorage.getItem("token")
  
        await axios.put(
  
          `http://127.0.0.1:5000/api/admin/student/${this.student.id}/activate`,
  
          {},
  
          {
  
            headers: {
  
              Authorization: `Bearer ${token}`
  
            }
  
          }
  
        )
  
        this.fetchStudent()
  
      },
  
      async deactivateStudent() {
  
        const token = localStorage.getItem("token")
  
        await axios.put(
  
          `http://127.0.0.1:5000/api/admin/student/${this.student.id}/deactivate`,
  
          {},
  
          {
  
            headers: {
  
              Authorization: `Bearer ${token}`
  
            }
  
          }
  
        )
  
        this.fetchStudent()
  
      },
  
      async blacklistStudent() {
  
        if (!confirm("Are you sure you want to blacklist this student?")) {
  
          return
  
        }
  
        const token = localStorage.getItem("token")
  
        await axios.put(
  
          `http://127.0.0.1:5000/api/admin/student/${this.student.id}/blacklist`,
  
          {},
  
          {
  
            headers: {
  
              Authorization: `Bearer ${token}`
  
            }
  
          }
  
        )
  
        this.fetchStudent()
  
      },
  
      async deleteStudent() {
  
        if (!confirm("Delete this student permanently?")) {
  
          return
  
        }
  
        const token = localStorage.getItem("token")
  
        await axios.delete(
  
          `http://127.0.0.1:5000/api/admin/student/${this.student.id}`,
  
          {
  
            headers: {
  
              Authorization: `Bearer ${token}`
  
            }
  
          }
  
        )
  
        this.$router.push("/admin/students")
  
      }
  
    }
  
  }
  </script>