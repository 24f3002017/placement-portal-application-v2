<template>
    <div class="d-flex flex-column min-vh-100">
  
     
      <AdminNavbar />
  
    
      <div class="container my-5 flex-grow-1">
  
        <h2 class="text-center mb-4">Company Details</h2>
  
        <div class="card shadow-sm">
          <div class="card-body">
  
            <table class="table">

              <tbody>
  
              <tr>
                <th width="30%">Company Name</th>
                <td>{{ company.name }}</td>
              </tr>
  
              <tr>
                <th>Email</th>
                <td>{{ company.email }}</td>
              </tr>
  
              <tr>
                <th>Industry</th>
                <td>{{ company.industry }}</td>
              </tr>
  
              <tr>
                <th>Website</th>
                <td>{{ company.website }}</td>
              </tr>
  
              <tr>
                <th>HR Contact</th>
                <td>{{ company.hr_contact }}</td>
              </tr>
  
              <tr>
                <th>Status</th>
                <td>
                  <span class="badge bg-warning" v-if="company.approval_status=='pending'">Pending</span>
                  <span class="badge bg-success" v-if="company.approval_status=='approved'">Approved</span>
                  <span class="badge bg-danger" v-if="company.approval_status=='rejected'">Rejected</span>
                </td>
              </tr>

              </tbody>
  
            </table>
  
            <div class="text-center mt-4" v-if="company.approval_status=='pending'">

              <button class="btn btn-success me-2" @click="approveCompany">
                Approve
              </button>
  
              <button class="btn btn-danger" @click="rejectCompany">
                Reject
              </button>
            </div>

            <div class="text-center mt-3">
              <button
              class="btn btn-warning me-2"
              @click="deactivateCompany"
              v-if="company.status == 'active'"
              >
              Deactivate
            </button>

            <button
  class="btn btn-success me-2"
  @click="activateCompany"
  v-if="company.status == 'inactive'"
>
  Activate
</button>

<button
  class="btn btn-dark me-2"
  @click="blacklistCompany"
  v-if="company.status != 'blacklisted'"
>
  Blacklist
</button>

<button
  class="btn btn-danger"
  @click="deleteCompany"
  v-if="company.status != 'blacklisted'"
>
  Delete
</button>

</div>
  
            <div class="text-center mt-4">
              <button
                class="btn btn-secondary"
                @click="$router.push('/admin/companies')"
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
  import axios from "axios";
  import AdminNavbar from "../components/AdminNavbar.vue";
  import Footer from "../components/Footer.vue";
  
  export default {
  
    components: {
      AdminNavbar,
      Footer
    },
  
    data() {
      return {
        company: {}
      }
    },
  
    mounted() {
      this.fetchCompany();
    },
  
    methods: {

async fetchCompany() {

  const token = localStorage.getItem("token")

  const res = await axios.get(
    `http://127.0.0.1:5000/api/admin/company/${this.$route.params.id}`,
    {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }
  )
  this.company = res.data
},
  
async approveCompany() {

const token = localStorage.getItem("token")

await axios.put(
    `http://127.0.0.1:5000/api/admin/company/${this.company.id}/approve`,
    {},
    {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
)

this.fetchCompany()
},
  
async rejectCompany() {

const token = localStorage.getItem("token")

await axios.put(
    `http://127.0.0.1:5000/api/admin/company/${this.company.id}/reject`,
    {},
    {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
)

this.fetchCompany()
},

async activateCompany() {

  const token = localStorage.getItem("token")
await axios.put(
  `http://127.0.0.1:5000/api/admin/company/${this.company.id}/activate`,
  {},
    {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
)

this.fetchCompany()
},

async deactivateCompany() {

  const token = localStorage.getItem("token")

await axios.put(
  `http://127.0.0.1:5000/api/admin/company/${this.company.id}/deactivate`,
  {},
    {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
)

this.fetchCompany()
},

async blacklistCompany() {

if (!confirm("Are you sure you want to blacklist this company?")) {
  return
}

const token = localStorage.getItem("token")
await axios.put(
  `http://127.0.0.1:5000/api/admin/company/${this.company.id}/blacklist`,
  {},
    {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
)

this.fetchCompany()
},

async deleteCompany() {

if (!confirm("Delete this company permanently?")) {
  return
}

const token = localStorage.getItem("token")

await axios.delete(
  `http://127.0.0.1:5000/api/admin/company/${this.company.id}`,
    {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
)

this.$router.push("/admin/companies")
}

    }
  
  }
  </script>